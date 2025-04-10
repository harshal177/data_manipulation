import pandas as pd
from collections import defaultdict

# Load Excel file instead of CSV
df = pd.read_excel("raw_data.xlsx")

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

# Sort matches by date to ensure chronological order
df = df.sort_values("Date").reset_index(drop=True)

# Stats to roll
stats_to_roll = ['FTHG', 'FTAG', 'HS', 'AS', 'HST', 'AST', 'HF', 'AF',
                 'HC', 'AC', 'HY', 'AY', 'HR', 'AR']

# Initialize a dictionary to keep match history per team
team_matches = defaultdict(list)

# Output list to collect results
output_rows = []

# Function to determine match result for a team
def get_result(row, team):
    if row['HomeTeam'] == team:
        if row['FTR'] == 'H': return 'W'
        elif row['FTR'] == 'A': return 'L'
        else: return 'D'
    else:
        if row['FTR'] == 'A': return 'W'
        elif row['FTR'] == 'H': return 'L'
        else: return 'D'

# Main processing loop
for _, row in df.iterrows():
    match_date = row['Date']
    home_team = row['HomeTeam']
    away_team = row['AwayTeam']

    row_output = {}

    for team, prefix in [(home_team, 'H'), (away_team, 'A')]:
        history_list = team_matches[team]

        # Handle case where there's no history yet
        if not history_list:
            history = pd.DataFrame(columns=['Date', 'Result'] + stats_to_roll)
        else:
            history = pd.DataFrame(history_list)
            history = history[history['Date'] < match_date].sort_values('Date', ascending=False)

        for window in [5, 15, 38]:
            window_history = history.head(window)

            # Basic stats
            for stat in stats_to_roll:
                col_name = f"{stat}_L{window}_{prefix}"
                row_output[col_name] = window_history[stat].sum()

            # Match outcomes
            result_counts = window_history['Result'].value_counts()
            row_output[f"{prefix}W_L{window}"] = result_counts.get('W', 0)
            row_output[f"{prefix}D_L{window}"] = result_counts.get('D', 0)
            row_output[f"{prefix}L_L{window}"] = result_counts.get('L', 0)

    # Append row result
    output_rows.append(row_output)

    # Store this match into history
    for team in [home_team, away_team]:
        match_info = {
            'Date': match_date,
            'Result': get_result(row, team),
        }
        for stat in stats_to_roll:
            match_info[stat] = row[stat]
        team_matches[team].append(match_info)

# Create DataFrame from output
manipulated_df = pd.DataFrame(output_rows)

# Concatenate original raw data with manipulated stats
final_df = pd.concat([df, manipulated_df], axis=1)

# Save to Excel
final_df.to_excel("manipulated_data.xlsx", index=False)

print(" Manipulated data saved as 'manipulated_data.xlsx'")

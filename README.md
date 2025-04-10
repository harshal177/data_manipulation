# 🏟️ Football Match Data Manipulation

This project focuses on manipulating historical football match data to derive team-based rolling statistics for predictive modeling, analytics, or reporting.

## 📊 Objective

To create a manipulated dataset where each match includes detailed performance summaries of both the **home** and **away** teams over their **last 5, 15, and 38 matches**.

These summaries include:
- Total goals scored and conceded
- Shots (on/off target)
- Fouls committed
- Cards (yellow/red)
- Corners
- Match outcomes (Wins, Draws, Losses)

## 🧩 How It Works

For every match in the dataset:
- Collect historical matches of the home and away team before the match date.
- Calculate rolling totals for selected statistics for the last 5, 15, and 38 games.
- Track performance regardless of whether the match was played at home or away.

## 📁 Project Structure

```bash
.
├── raw_data.xlsx         # Original football match dataset
├── eda.py                # Main script to perform data manipulation
├── manipulated_data.xlsx # Output file with all derived features
└── README.md             # This file
## 🚀 How to Run

1. **Install Required Libraries**  
   Make sure you have Python installed, then install the required libraries using pip:
   ```bash
   pip install pandas openpyxl
2.prepare the Dataset
Place your raw Excel dataset in the project directory and name it:

raw_data.xlsx

3.Run the Script
Execute the script to generate the manipulated data:

    python eda.py

4.Check Output
    After running, a new file named manipulated_data.xlsx will be created containing all the calculated statistics.


Let me know if you also want to include environment setup instructions (like using a virtualenv or Conda).



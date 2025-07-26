# Uber Fare Analysis Project

# Names & ID: BISUBUZO DANIEL JOSPIN 
# Tools Used: Python, Power BI, Pandas
# Dataset: Uber Fares Dataset on Kaggle

 # Project Overview and Problem statement 

Conduct end-to-end analysis of Uber ride fare data to: Explore ride and fare trends across time intervals
Clean, transform, and visualize the dataset
Build an interactive Power BI dashboard
Generate meaningful business insights.

## Step 1: Data Cleaning

- Loaded uber.csv using Python
-Removed 1 row with null coordinates
- Removed entries with:  Negative fares  

## Final dataset size: 199,269 rows

# Step 2: Feature Engineering
 Extracted Data from pickup_datetime:  hour , day, month and day_of_week.

 Added custom column: 🟡 is_peak → "Peak" or "Off-Peak" hours

## Saved as: uber_enhanced.csv

# Step 3–5: Visual Analytics (Power BI)

📌 Key Dashboards Created:

 Fare Patterns by Hour → Line + Bar Charts
Ride Counts by:
Hour
Day
Month
 Seasonal Trends using day_of_week
 Peak vs Off-Peak rides (Pie + Area chart)

## Interactivity:

 Slicers, filters, and tooltips enabled
✅Drill-down from month → day → hour
# Step 6: Key Insights

## Peak Ride Hours:

- 8 AM
- 6 PM
- Most Active Days:

Weekdays > Weekends
## Fare Trends:

Fares peak during rush hours
Off-peak rides dominate (~65%)

# Screenshots
<img width="960" height="491" alt="Screenshot 2025-07-26 183838" src="https://github.com/user-attachments/assets/c212d79d-dea1-4632-8b96-9bdba4a6b871" />





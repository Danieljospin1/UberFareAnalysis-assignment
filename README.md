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
<img width="960" height="477" alt="image" src="https://github.com/user-attachments/assets/2c458197-e985-45c3-bee0-45abeefb1471" />
<img width="752" height="473" alt="Screenshot 2025-07-26 193211" src="https://github.com/user-attachments/assets/46cab1c4-32ca-46c4-aa57-16792fda3a1a" />
<img width="747" height="406" alt="Screenshot 2025-07-26 193226" src="https://github.com/user-attachments/assets/e1e1683d-6778-4041-9f68-f646eee1f5e6" />
<img width="753" height="457" alt="Screenshot 2025-07-26 193257" src="https://github.com/user-attachments/assets/e29427da-53b8-4e50-806a-a7fb3b821ed1" />
<img width="751" height="487" alt="Screenshot 2025-07-26 193320" src="https://github.com/user-attachments/assets/3dee3299-1be5-45dd-b058-3ec728342268" />
<img width="603" height="465" alt="Screenshot 2025-07-26 193338" src="https://github.com/user-attachments/assets/e60ec0f8-b58b-4896-b6d9-830254a3e2aa" />











import pandas as pd

df = pd.read_csv("C:\\Users\\HP\\Desktop\\Big Data\\uber.csv")

print(df.head())

print("=== Dataset Overview ===")
print("Dataset shape:", df.shape)
print("=== Dataset Structure ===")
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print()
print("=== Data Types and Memory Info ===")
print(df.info())
print()
print("=== Missing Values Per Column ===")
print(df.isnull().sum())
print()
print("=== Check for Duplicate Rows ===")
print("Duplicates:", df.duplicated().sum())
print("=== Sample Data ===")
df_cleaned = df.dropna()
print("After dropping missing:", df_cleaned.shape)
df_cleaned = df_cleaned.drop_duplicates()
print("After dropping duplicates:", df_cleaned.shape)
df_cleaned = df_cleaned[(df_cleaned['fare_amount'] > 0) & 
                        (df_cleaned['passenger_count'] > 0)]
print("After removing invalid fare/passenger_count:", df_cleaned.shape)
print("=== Cleaned Data Sample ===")
df_cleaned.to_csv("uber_cleaned.csv", index=False)
print("Cleaned dataset saved as 'uber_cleaned.csv'")

import numpy as np

print("=== Descriptive Statistics ===")
print(df_cleaned.describe())
print("\n=== Fare Amount Statistics ===")
print("\nMedian fare:", df_cleaned['fare_amount'].median())
print("Mode fare:", df_cleaned['fare_amount'].mode()[0])
print("\nMedian passengers:", df_cleaned['passenger_count'].median())
print("Mode passengers:", df_cleaned['passenger_count'].mode()[0])
print("\n=== Fare Amount Statistics ===")
print(df_cleaned['fare_amount'].quantile([0.25, 0.5, 0.75]))
print("\n=== Passenger Count Statistics ===")
high_fares = df_cleaned[df_cleaned['fare_amount'] > 100]
print("\nHigh fare rides (> $100):", high_fares.shape[0])

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load dataset
df = pd.read_csv("uber_cleaned.csv")
print("=== Data Visualization ===")
sns.set(style="whitegrid")

# 1. Replace fare histogram with a violin plot for better distribution insight
plt.figure(figsize=(10, 6))
sns.violinplot(y=df['fare_amount'])
plt.title("Fare Amount Violin Plot")
plt.ylabel("Fare ($)")
plt.ylim(0, 100)
plt.show()

# 2. Enhanced boxplot: show by passenger count
plt.figure(figsize=(10, 6))
sns.boxplot(x='passenger_count', y='fare_amount', data=df)
plt.title("Fare Distribution per Passenger Count")
plt.xlabel("Number of Passengers")
plt.ylabel("Fare ($)")
plt.ylim(0, 100)
plt.show()

# 3. Calculate distance (as in original)
df['distance'] = np.sqrt(
    (df['dropoff_longitude'] - df['pickup_longitude'])**2 +
    (df['dropoff_latitude'] - df['pickup_latitude'])**2
)
print("Distance column added.")

# 4. Replace scatterplot with a regression line (trend)
plt.figure(figsize=(10, 6))
sns.regplot(x='distance', y='fare_amount', data=df, scatter_kws={'alpha':0.3}, line_kws={"color": "red"})
plt.title("Fare Amount vs. Distance with Trend Line")
plt.xlabel("Distance (approx.)")
plt.ylabel("Fare ($)")
plt.xlim(0, 0.3)
plt.ylim(0, 100)
plt.show()

# 5. Time-based features
df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])
df['hour'] = df['pickup_datetime'].dt.hour
df['day'] = df['pickup_datetime'].dt.day
df['month'] = df['pickup_datetime'].dt.month
df['day_of_week'] = df['pickup_datetime'].dt.dayofweek

# 6. Add Peak vs Off-Peak
def is_peak(hour):
    return (7 <= hour <= 9) or (16 <= hour <= 19)

df['is_peak'] = df['hour'].apply(lambda x: 'Peak' if is_peak(x) else 'Off-Peak')

# 7. New graph: Fare vs. Time of Day
plt.figure(figsize=(10, 6))
sns.lineplot(x='hour', y='fare_amount', data=df, ci=None)
plt.title("Average Fare by Hour of Day")
plt.xlabel("Hour")
plt.ylabel("Average Fare ($)")
plt.ylim(0, 100)
plt.show()

# 8. New graph: Fare by Peak vs Off-Peak
plt.figure(figsize=(8, 6))
sns.boxplot(x='is_peak', y='fare_amount', data=df)
plt.title("Fare Amount during Peak vs Off-Peak Hours")
plt.ylabel("Fare ($)")
plt.ylim(0, 100)
plt.show()

# Save enhanced dataset
df.to_csv("uber_enhanced.csv", index=False)
print("Enhanced dataset saved as 'uber_enhanced.csv'")

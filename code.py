import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------
# Task 1: Dataset Loading
# ---------------------------
print("Loading dataset...")
df = pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\python.py\temperature.csv")
print("\nFirst 10 rows:")
print(df.head(10))

# ---------------------------
# Task 2: Data Cleaning
# ---------------------------
print("\nChecking missing values:")
print(df.isnull().sum())

# Fill missing temperatures with mean
if "temperature" in df.columns:
    df["temperature"] = df["temperature"].fillna(df["temperature"].mean())

# Drop rows with missing dates (if any)
df = df.dropna(subset=["date"])

print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# ---------------------------
# Task 3: Line Plot
# ---------------------------
plt.figure(figsize=(10,5))
plt.plot(df["date"], df["temperature"])
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.title("Temperature Variation Over Time")
plt.tight_layout()
plt.savefig("line_plot.png")
plt.close()

print("Saved line plot as line_plot.png")

# ---------------------------
# Task 4: Bar Chart
# ---------------------------

# Group by month name
df["month"] = df["date"].dt.month_name()
monthly_avg = df.groupby("month")["temperature"].mean()

plt.figure(figsize=(10,5))
plt.bar(monthly_avg.index, monthly_avg.values)
plt.xlabel("Month")
plt.ylabel("Average Temperature")
plt.title("Average Monthly Temperature")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("bar_chart.png")
plt.close()

print("Saved bar chart as bar_chart.png")

# ---------------------------
# Bonus (Optional)
# Scatter Plot – If multiple temperature columns exist
# ---------------------------
if "min_temp" in df.columns and "max_temp" in df.columns:
    plt.figure(figsize=(8,5))
    plt.scatter(df["min_temp"], df["max_temp"])
    plt.xlabel("Minimum Temperature")
    plt.ylabel("Maximum Temperature")
    plt.title("Min vs Max Temperature")
    plt.tight_layout()
    plt.savefig("scatter_plot.png")
    plt.close()
    print("Saved scatter plot as scatter_plot.png")

print("\nAll tasks completed successfully!")

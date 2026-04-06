import pandas as pd

print("=== AI Dataset Inspection Pipeline ===")

# 1 Load CSV dataset
print("\nLoading dataset...")
df = pd.read_csv("dataset.csv")

# 2 Display first 5 rows
print("\nFirst 5 rows:")
print(df.head())

# 3 Display last 5 rows
print("\nLast 5 rows:")
print(df.tail())

# 4 Structural information
print("\nDataset Information:")
print(df.info())

# 5 Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# 6 Select single column
print("\nSelecting single column (Score):")
score_column = df["Score"]
print(score_column)

# 7 Select multiple columns
print("\nSelecting multiple columns (Name and Score):")
selected_columns = df[["Name", "Score"]]
print(selected_columns)

# 8 Filter rows based on condition
print("\nFiltered rows (Score > 80):")
filtered_data = df[df["Score"] > 80]
print(filtered_data)

print("\n=== Inspection Completed ===")
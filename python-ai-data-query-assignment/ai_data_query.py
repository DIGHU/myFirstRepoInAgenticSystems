import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "Score": [95, 92, 88, 76, 90, 84],
    "Passed": [True, True, True, False, True, True],
    "Category": ["A", "A", "B", "C", "A", "B"]
}

df = pd.DataFrame(data)

print("\nOriginal Dataset:\n")
print(df)

print("\nOnly Name Column:\n")
print(df["Name"])


print("\nName and Score Columns:\n")
new_df = df[["Name", "Score"]]
print(new_df)

print("\nFirst Three Rows using iloc:\n")
print(df.iloc[0:3])

df_indexed = df.set_index("Name")

print("\nUsing loc with Name index:\n")
print(df_indexed.loc["Alice"])

print("\nStudents with Score > 85:\n")
high_score = df[df["Score"] > 85]
print(high_score)

print("\nStudents Score > 85 and Passed:\n")
filtered = df[(df["Score"] > 85) & (df["Passed"] == True)]
print(filtered)

print("\nSorted High Performing Students:\n")
sorted_students = filtered.sort_values(by="Score", ascending=False)
print(sorted_students)

print("\nChained Filtering + Sorting:\n")
result = df[(df["Score"] > 85) & (df["Passed"] == True)].sort_values(by="Score", ascending=False)

print(result)
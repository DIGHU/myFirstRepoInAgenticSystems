import pandas as pd
import numpy as np

# Creating new sample dataset
data = {
    "Employee": [
        "Rohan", "Kavya", "Aditya", "Meera",
        "Sanjay", "Pooja", "Karan", "Nisha"
    ],
    
    "Department": [
        "Sales", "IT", "Marketing", "Finance",
        "IT", "Sales", "Finance", "Marketing"
    ],
    
    "Salary": [
        550000, 720000, np.nan, 680000,
        750000, 530000, np.nan, 610000
    ],
    
    "Temporary_Notes": [
        "Intern", "New hire", "Pending verification",
        "Contract", "On training", "Temporary staff",
        "Documents pending", "Probation"
    ]
}

df = pd.DataFrame(data)

print("\nOriginal Dataset")
print(df)

# Detect missing values
print("\nMissing Values")
print(df.isnull().sum())

# Fill missing salary with mean
mean_salary = df["Salary"].mean()
df["Salary"].fillna(mean_salary, inplace=True)

print("\nDataset After Filling Missing Salary")
print(df)

# Drop Temporary_Notes column
df = df.drop(columns=["Temporary_Notes"])

print("\nAfter Dropping Temporary Notes")
print(df)

# Rename Salary column
df = df.rename(columns={"Salary": "Annual_Salary"})

print("\nAfter Renaming Column")
print(df)

# Group by Department
summary = df.groupby("Department").agg(
    Mean_Salary=("Annual_Salary", "mean"),
    Employee_Count=("Employee", "count")
)

print("\nFinal Summary Table")
print(summary)
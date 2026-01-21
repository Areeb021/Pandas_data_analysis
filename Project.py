import pandas as pd

# =========================
# Load Data
# =========================
df = pd.read_csv("data.csv")

# =========================
# Data Cleaning
# =========================
df["Joining_Date"] = pd.to_datetime(df["Joining_Date"])

# Check duplicates (optional)
# print(df[df.duplicated()])

# =========================
# Basic Statistics
# =========================
print(f"Total employees: {df['EmployeeID'].count()}")
print(f"Average age: {df['Age'].mean():.2f}")
print(f"Average salary: {df['Salary'].mean():.2f}")

# =========================
# Department Analysis
# =========================
group = df.groupby("Department")

print("\nAverage salary per department:")
print(group["Salary"].mean())

print("\nNumber of employees per department:")
print(group["EmployeeID"].count())

# =========================
# Salary Analysis
# =========================
highest_paid_index = df["Salary"].idxmax()
print("\nHighest paid employee:")
print(df.loc[highest_paid_index, ["Name", "Salary"]])

avg_salary = df["Salary"].mean()
print("\nEmployees earning above average salary:")
print(df[df["Salary"] > avg_salary][["Name", "Salary"]])

# =========================
# Experience Analysis
# =========================
most_experienced_index = df["Experience_Years"].idxmax()
print("\nMost experienced employee:")
print(df.loc[most_experienced_index, ["Name", "Experience_Years"]])

print("\nEmployees with more than 5 years of experience:")
print(df[df["Experience_Years"] > 5][["Name", "Experience_Years"]])

print("\nAverage experience per department:")
print(group["Experience_Years"].mean())

# =========================
# Feature Engineering
# =========================
df["Salary_in_K"] = df["Salary"] / 1000
df["Senior_Level"] = df["Experience_Years"] > 5

# =========================
# Date Analysis
# =========================
df["Joining_Year"] = df["Joining_Date"].dt.year

print("\nEmployees who joined after 2020:")
print(df[df["Joining_Year"] > 2020][["Name", "Joining_Date"]])

print("\nOldest employee:")
print(df.loc[df["Joining_Date"].idxmin(), ["Name", "Joining_Date"]])

print("\nNewest employee:")
print(df.loc[df["Joining_Date"].idxmax(), ["Name", "Joining_Date"]])

# =========================
# Business Questions
# =========================
total_salary_by_dept = group["Salary"].sum()
most_expensive_dept = total_salary_by_dept.idxmax()

print("\nWhich department is the most expensive?")
print(most_expensive_dept)

total_experience_by_dept = group["Experience_Years"].sum()
most_experienced_dept = total_experience_by_dept.idxmax()

print("\nWhich department has the most experienced staff?")
print(most_experienced_dept)

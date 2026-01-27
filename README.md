📊 Employee Data Analysis Project
📌 Project Overview

This project focuses on analyzing employee data using Python, Pandas, and Matplotlib.
The goal is to clean the dataset, perform exploratory data analysis (EDA), engineer useful features, and answer real-world business questions using both statistics and visualizations.

The dataset includes employee details such as age, salary, department, experience, and joining date.

🛠️ Tools & Technologies

Python

Pandas – data cleaning, manipulation, and analysis

Matplotlib – data visualization

📂 Dataset Description

The dataset (data.csv) contains the following columns:

EmployeeID

Name

Age

Salary

Department

Experience_Years

Joining_Date

🧹 Data Cleaning

Converted Joining_Date to datetime format

Checked for duplicate records

Ensured numeric columns were ready for analysis

📈 Exploratory Data Analysis (EDA)
🔹 Basic Statistics

Total number of employees

Average age

Average salary

🔹 Department Analysis

Average salary per department

Number of employees per department

Total salary cost per department

Total experience per department

🔹 Salary Analysis

Identified the highest-paid employee

Found employees earning above the average salary

Analyzed salary distribution using a histogram

🔹 Experience Analysis

Identified the most experienced employee

Filtered employees with more than 5 years of experience

Calculated average experience per department

📊 Visualizations

Bar chart showing number of employees per department

Histogram displaying salary distribution

(Optional) Department-wise salary comparison charts

These visualizations help in understanding workforce distribution and compensation patterns.

🧠 Feature Engineering

Created Salary_in_K column for better salary readability

Added Senior_Level flag based on experience (> 5 years)

Extracted Joining_Year from joining date

❓ Business Questions Answered

Which department is the most expensive in terms of total salary?

Which department has the most experienced staff?

Who is the highest-paid employee?

How is salary distributed across the organization?

🚀 Key Insights

Certain departments have significantly higher salary costs

Experience and salary show meaningful trends

Workforce distribution varies noticeably by department

📁 Project Structure
├── data.csv
├── employee_analysis.py
└── README.md

✅ Conclusion

This project demonstrates practical use of Pandas for data analysis and Matplotlib for visualization while answering meaningful business questions.
It reflects real-world data handling and analytical thinking suitable for entry-level data analyst role

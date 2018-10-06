# Import required libraries for Data Analysis
import numpy as np
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 500 )

# Read the csv file and store the data in a dataframe
dataset = pd.read_csv("Employee_Details.csv")

# Get count of rows and columns
print(dataset.shape)

# View top few rows of data
print(dataset.head())

# Datatype of each column
print(dataset.dtypes)

# Rename columns for better readability
dataset.columns = ["satisfaction_level","last_evaluation","project_count","average_monthly_hours","exp_in_company","work_accident",
                   "left_company","promotion_last_5years","job_role","salary"]

# Change datatype of categorical data
dataset.job_role = dataset.job_role.astype("category")
dataset.salary = dataset.salary.astype("category")
print(dataset.dtypes)

# Check for columns with missing values
print(dataset.isnull().any())

# Replace missing values with zero
dataset.satisfaction_level.fillna(0)


# Summary of numeric columns
print(dataset.describe())

#Summary of categorical columns
print(dataset.salary.describe())
print(dataset.job_role.describe())

# Percentage of employee who left the company
perc_employee_left = np.sum(dataset.left_company/len(dataset.left_company))*100
print('Percentage of employee left = {0} %'.format(round(perc_employee_left)))




# Correlation Matrix
corr = dataset.corr()
print(corr)
# sns.heatmap(corr,xticklabels=corr.columns.values,yticklabels=corr.columns.values)

# Comparing satisfaction among all employees against satisfaction among employees who left the company
perc_employee_satisfaction = sum(dataset.satisfaction_level/len(dataset.satisfaction_level))*100
print("Percentage satisfaction among all employees : {0} %".format(round(perc_employee_satisfaction)))

employee_left = dataset[dataset.left_company==1]
perc_employee_left =  sum(employee_left.satisfaction_level/len(employee_left.satisfaction_level))*100
print("Percentage satisfaction among employees who left the company : {0} %".format(round(perc_employee_left)))

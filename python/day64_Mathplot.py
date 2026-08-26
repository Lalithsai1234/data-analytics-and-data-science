# Numerical plots:
# Line plot: Displays trends or changes
# Histogram: Displays frequency distribution
# Box plot: Displays data spread and outliers
# Bar chart: Compares categories
# Pie chart: Displays percentages
# Scatter plot: Shows the relationship between two variables
# Bubble plot: Scatter plot where bubble size represents another variable

# Import Matplotlib for creating charts
import matplotlib.pyplot as plt

# Import Pandas for creating and working with DataFrames
import pandas as pd


# Create a DataFrame containing salary values
# The * 2 repeats the list two times
df = pd.DataFrame({
    "salary": [
        10000, 20000, 30000, 40000, 50000,
        60000, 70000, 80000, 90000, 15000
    ] * 2
})

# Set the chart size: width = 10 inches, height = 5 inches
plt.figure(figsize=(10, 5))

# Create a line plot of salary values
# The x-axis uses the index values automatically
plt.plot(df["salary"])

# Display the chart
plt.show()


# Add a department column to the DataFrame
df["dept"] = [
    "Finance", "HR", "IT", "Finance", "HR",
    "IT", "Finance", "HR", "IT", "HR"
] * 2

# Count the number of employees in each department
count = df["dept"].value_counts()
print(count)


# Create a pie chart using department counts
# labels displays department names
# autopct displays percentages
# explode separates the IT slice
# shadow adds a shadow effect
plt.pie(
    count,
    labels=count.index,
    autopct="%1.1f%%",
    explode=(0, 0, 0.1),
    shadow=True
)

# Display the pie chart
plt.show()


# Create a bar chart showing department counts
plt.bar(
    count.index,
    count,
    color=["orange", "blue", "green"]
)

# Add labels to the axes
plt.xlabel("Department")
plt.ylabel("Employee Count")

# Display the bar chart
plt.show()


# Bivariate analysis means analyzing two variables
# Create an age column
df["age"] = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29] * 2

# Create a scatter plot to show the relationship
# between salary and age
plt.scatter(df["salary"], df["age"])

plt.xlabel("Salary")
plt.ylabel("Age")

# Display the scatter plot
plt.show()


# Create a line plot using two variables:
# salary on the x-axis and age on the y-axis
plt.plot(df["salary"], df["age"])

plt.xlabel("Salary")
plt.ylabel("Age")

# Display the line plot
plt.show()


# Filter salaries based on department
hr_sal = df[df["dept"] == "HR"]["salary"]
fin_sal = df[df["dept"] == "Finance"]["salary"]
it_sal = df[df["dept"] == "IT"]["salary"]

print("HR salaries:", hr_sal)


# Create a box plot for each department
# A box plot displays minimum, Q1, median, Q3, maximum, and outliers
plt.boxplot(
    [hr_sal, fin_sal, it_sal],
    tick_labels=["HR", "Finance", "IT"]
)

# Display grid lines
plt.grid()

# Display the box plot
plt.show()


# Calculate the average salary of each department
average_salary = [
    hr_sal.mean(),
    it_sal.mean(),
    fin_sal.mean()
]

# Create a bar chart of average salaries
plt.bar(
    ["HR", "IT", "Finance"],
    average_salary
)

plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.grid()

# Display the chart
plt.show()


# Add experience values to the DataFrame
df["Exp"] = [
    1.1, 2.2, 3.3, 4.4, 5.5,
    6.6, 7.7, 8.8, 9.9, 10.1
] * 2

# Create a bubble plot
# x-axis: age
# y-axis: salary
# s controls bubble size
# Experience is multiplied by 50 to make bubbles visible
# edgecolors adds a black border
plt.scatter(
    df["age"],
    df["salary"],
    s=df["Exp"] * 50,
    edgecolors="black"
)

plt.xlabel("Age")
plt.ylabel("Salary")
plt.title("Age vs Salary")

# Display the bubble plot
plt.show()


# Create a new DataFrame containing company information
d1 = pd.DataFrame({
    "year": [2000, 2001, 2002, 2003, 2004],
    "sales": [100, 200, 300, 400, 500],
    "exp": [50, 150, 250, 350, 450],
    "profit": [10, 20, 30, 40, 50]
})


# Plot yearly sales
plt.plot(
    d1["year"],
    d1["sales"],
    label="Yearly Sales"
)

# Plot yearly expenses
plt.plot(
    d1["year"],
    d1["exp"],
    label="Yearly Expenses"
)

# Plot yearly profit
plt.plot(
    d1["year"],
    d1["profit"],
    label="Yearly Profit"
)

plt.xlabel("Year")
plt.ylabel("Amount")

# Display labels for all lines
plt.legend()

plt.title("Company Yearly Chart")

# Display the chart
plt.show()


# Convert department names into colors
# HR = orange, IT = blue, Finance = red
department_colors = df["dept"].map({
    "HR": "orange",
    "IT": "blue",
    "Finance": "red"
})

# Create a scatter plot using DataFrame column names
# data=df tells Matplotlib to use columns from df
plt.scatter(
    "salary",
    "age",
    data=df,
    c=department_colors
)

plt.xlabel("Salary")
plt.ylabel("Age")
plt.title("Salary vs Age by Department")

# Display the final chart
plt.show()



nums=[2,1,2,0,0,1]
l=0
m=0
h=len(nums)-1
while m<=h:
    if nums[m]==2:
        nums[m], nums[h]=nums[h], nums[m]
        h-=1
    elif nums[m]==1:
        m+=1
    elif nums[m]==0:
        nums[l], nums[m]=nums[m], nums[l]
        l+=1
        m+=1
print(nums)
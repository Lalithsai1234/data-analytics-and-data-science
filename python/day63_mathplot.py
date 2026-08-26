# Import Matplotlib's pyplot module for creating charts
import matplotlib.pyplot as plt

# Import Pandas for creating and working with DataFrames
import pandas as pd


# Create a DataFrame containing salary values
df = pd.DataFrame({
    "salary": [10000, 20000, 30000, 40000, 50000,
               60000, 70000, 80000, 90000, 15000] * 2
})

# Display the DataFrame in the console
print(df)


# Create a line plot for salary values
# color='r' means red color
# marker='*' displays a star at each data point
# linewidth controls the thickness of the line
# linestyle='--' creates a dashed line
plt.plot(
    df["salary"],
    color="r",
    marker="*",
    linewidth=2,
    linestyle="--"
)

# Display grid lines
plt.grid()

# Add labels to the x-axis and y-axis
plt.xlabel("Months")
plt.ylabel("Salary")

# Add a title to the chart
plt.title("Salary Over Year")

# Display the chart
plt.show()


# Sample sales data for two companies
months = [1, 2, 3, 4, 5]
c1 = [10, 20, 30, 40, 50]
c2 = [20, 30, 40, 50, 60]

# Plot Company 1 sales
plt.plot(months, c1, label="Company-1")

# Plot Company 2 sales
plt.plot(months, c2, label="Company-2")

# Display labels for both lines
plt.legend()

# Add a title
plt.title("Companies Sales")

# Display the chart
plt.show()


# Types of data analysis:
# Univariate analysis: Analysis of one variable
# Bivariate analysis: Analysis of two variables
# Multivariate analysis: Analysis of more than two variables


# Common numerical plots:
# 1. Line plot: Shows changes or trends over time
# 2. Histogram: Shows the frequency distribution of numerical data
# 3. Box plot: Shows minimum, Q1, median, Q3, maximum, and outliers
# 4. Bar chart: Compares values between categories
# 5. Pie chart: Shows parts of a whole
# 6. Scatter plot: Shows the relationship between two variables


# Create a histogram of salaries
# bins=20 divides the salary values into 20 intervals
plt.hist(df["salary"], bins=20)

# Display the histogram
plt.show()


# Create a box plot of salaries
# A box plot helps identify the spread and outliers in the data
plt.boxplot(df["salary"])

# Display the box plot
plt.show()
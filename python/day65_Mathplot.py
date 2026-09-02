import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.DataFrame({
    "salary": [
        10000, 20000, 30000, 40000, 50000,
        60000, 70000, 80000, 90000, 15000
    ] * 2
})
df["dept"] = [
    "Finance", "HR", "IT", "Finance", "HR",
    "IT", "Finance", "HR", "IT", "HR"
] * 2
df["age"] = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29] * 2
df["Exp"] = [
    1.1, 2.2, 3.3, 4.4, 5.5,
    6.6, 7.7, 8.8, 9.9, 10.1
] * 2
print(df)
#     salary     dept  age   Exp
# 0    10000  Finance   20   1.1
# 1    20000       HR   21   2.2
# 2    30000       IT   22   3.3
# 3    40000  Finance   23   4.4
# 4    50000       HR   24   5.5
# 5    60000       IT   25   6.6
# 6    70000  Finance   26   7.7
# 7    80000       HR   27   8.8
# 8    90000       IT   28   9.9
# 9    15000       HR   29  10.1
# 10   10000  Finance   20   1.1
# 11   20000       HR   21   2.2
# 12   30000       IT   22   3.3
# 13   40000  Finance   23   4.4
# 14   50000       HR   24   5.5
# 15   60000       IT   25   6.6
# 16   70000  Finance   26   7.7
# 17   80000       HR   27   8.8
# 18   90000       IT   28   9.9
# 19   15000       HR   29  10.1


fig, axs=plt.subplots(1,3, figsize=(15,5))
axs[0].plot(df["salary"], df["age"])
axs[0].set_xlabel("Salary")
axs[0].set_ylabel("Age")
axs[0].set_title("Salary vs Age")

axs[1].hist(df["salary"], bins=10)
axs[1].set_xlabel("Salary")
axs[1].set_ylabel("Frequency")
axs[1].set_title("Salary Distribution")

axs[2].boxplot(df["salary"])
axs[2].set_xlabel("Salary")
axs[2].set_title("Salary Boxplot")
# plt.savefig("python/day65_salary_analysis.png") # to save the image of
plt.show()


ax=plt.axes(projection="3d")
ax.scatter(df["salary"], df["age"], df["Exp"])
ax.set_xlabel("Salary") 
ax.set_ylabel("Age")
ax.set_zlabel("Experience")
ax.set_title("3D Scatter Plot") 
plt.show()


import plotly.express as px
fig=px.scatter_3d(df, x="salary", y="age", z="Exp")   
fig.show()
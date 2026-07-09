#Part A

#1
import numpy as np

# 1D array
arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr1)

# 2D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", arr2)

# Using arange
arr3 = np.arange(0, 10, 2)
print("Arange Array:", arr3)

# Using linspace
arr4 = np.linspace(0, 1, 5)
print("Linspace Array:", arr4)

#2
print("First element:", arr1[0])
print("Slice:", arr1[1:4])

reshaped = arr2.reshape(3, 2)
print("Reshaped Array:\n", reshaped)

#3
arr_b = np.array([1, 2, 3])
print("Broadcasted Addition:", arr_b + 5)

#4
# Traditional loop
squares_loop = [x**2 for x in arr1]

# Vectorized
squares_vec = arr1**2

print("Loop:", squares_loop)
print("Vectorized:", squares_vec)

#5
mat = np.array([[1, 2], [3, 4]])
print("Dot Product:", np.dot(mat, mat))
print("Transpose:\n", mat.T)
print("Inverse:\n", np.linalg.inv(mat))

#Part B

import pandas as pd

# Series
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print("Series:\n", s)

# DataFrame
data = {'Name': ['Ali', 'Sara', 'John'], 'Age': [25, 30, 22]}
df = pd.DataFrame(data)
print("DataFrame:\n", df)

# Filtering
print("Age > 25:\n", df[df['Age'] > 25])

# Groupby
grouped = df.groupby('Age').size()
print("Groupby:\n", grouped)

# Merging
df2 = pd.DataFrame({'Name': ['Ali', 'Sara'], 'Score': [85, 90]})
merged = pd.merge(df, df2, on='Name')
print("Merged:\n", merged)

#Part C

# Load dataset
titanic = pd.read_csv("titanic.csv")

# Cleaning
titanic['Age'].fillna(titanic['Age'].median(), inplace=True)
titanic['Embarked'].fillna(titanic['Embarked'].mode()[0], inplace=True)

# Summary
print("Summary:\n", titanic.describe())

# Survival rate
survival_rate = titanic['Survived'].mean() * 100
print("Overall Survival Rate:", survival_rate, "%")

# Survival by class
class_survival = titanic.groupby('Pclass')['Survived'].mean() * 100
print("Survival by Class:\n", class_survival)

# Survival by gender
gender_survival = titanic.groupby('Sex')['Survived'].mean() * 100
print("Survival by Gender:\n", gender_survival)

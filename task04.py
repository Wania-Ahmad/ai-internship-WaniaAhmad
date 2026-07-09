#Part A

import numpy as np

# 1. Create arrays
arr1 = np.array([1, 2, 3, 4])              # 1D array
arr2 = np.array([[1, 2], [3, 4]])          # 2D array
arr3 = np.arange(0, 10, 2)                 # using arange
arr4 = np.linspace(0, 1, 5)                # evenly spaced values

# 2. Indexing, slicing, reshaping
print(arr1[2])                             # indexing
print(arr2[:, 1])                          # slicing column
reshaped = arr1.reshape(2, 2)              # reshape

# 3. Broadcasting
a = np.array([1, 2, 3])
b = 2
print(a + b)                               # broadcasting adds 2 to each element

# 4. Vectorized vs loops
arr = np.arange(1, 6)
squared_vec = arr ** 2                     # vectorized
squared_loop = [x**2 for x in arr]         # loop

# 5. Linear algebra
matA = np.array([[1, 2], [3, 4]])
matB = np.array([[5, 6], [7, 8]])
dot_product = np.dot(matA, matB)
transpose = matA.T
inverse = np.linalg.inv(matA)

#Part B

import pandas as pd

# 1. Create Series and DataFrame
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
df = pd.DataFrame({
    'Name': ['Ali', 'Sara', 'John'],
    'Age': [25, 30, 22],
    'Score': [85, 90, 88]
})

# 2. Indexing, filtering, sorting
print(df['Name'])                          # column selection
print(df[df['Age'] > 25])                  # filtering
print(df.sort_values(by='Score', ascending=False))

# 3. Groupby
grouped = df.groupby('Age')['Score'].mean()
print(grouped)

# 4. Merge & join
df1 = pd.DataFrame({'ID': [1, 2], 'Name': ['Ali', 'Sara']})
df2 = pd.DataFrame({'ID': [1, 2], 'Grade': ['A', 'B']})
merged = pd.merge(df1, df2, on='ID')
print(merged)

#Part C

import pandas as pd

# 1. Load dataset
df = pd.read_csv("titanic.csv")

# 2. Clean missing values
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# 3. Summary statistics
print(df.describe())

# 4. Exploratory analysis
survival_rate = df['Survived'].mean()
class_survival = df.groupby('Pclass')['Survived'].mean()
gender_survival = df.groupby('Sex')['Survived'].mean()

print("Overall survival rate:", survival_rate)
print("Survival by class:\n", class_survival)
print("Survival by gender:\n", gender_survival)






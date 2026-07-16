#Part A

#1
import pandas as pd

df = pd.read_csv("titanic.csv")

#2
# Check missing values
df.isnull().sum()

# Fill missing Age with median
df['Age'].fillna(df['Age'].median(), inplace=True)

# Fill missing Embarked with mode
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# Drop Cabin (too many missing)
df.drop(columns=['Cabin'], inplace=True)

df.drop_duplicates(inplace=True)

df = df[df['Age'] <= 80]

#Part B

import matplotlib.pyplot as plt
import seaborn as sns

# Histogram of Age
plt.hist(df['Age'], bins=20, color='skyblue')
plt.title("Age Distribution")
plt.show()

# Boxplot of Fare
sns.boxplot(x=df['Fare'])
plt.title("Fare Boxplot")
plt.show()

# Correlation Heatmap
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# Additional Visualization 1: Survival by Gender
sns.countplot(x='Sex', hue='Survived', data=df)
plt.title("Survival by Gender")
plt.show()

# Additional Visualization 2: Survival by Class
sns.countplot(x='Pclass', hue='Survived', data=df)
plt.title("Survival by Passenger Class")
plt.show()

#Part C

#2
df = pd.get_dummies(df, columns=['Sex','Embarked','Pclass'], drop_first=True)

#3
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
df[['Age','Fare']] = scaler.fit_transform(df[['Age','Fare']])

#Part D

#1
import sqlite3

conn = sqlite3.connect("titanic.db")
df.to_sql("titanic_table", conn, if_exists="replace", index=False)

#2
# SELECT
pd.read_sql("SELECT Name, Age, Sex_male FROM titanic_table LIMIT 5", conn)

# WHERE
pd.read_sql("SELECT * FROM titanic_table WHERE Age < 18", conn)

# GROUP BY
pd.read_sql("SELECT Sex_male, AVG(Survived) as survival_rate FROM titanic_table GROUP BY Sex_male", conn)

# JOIN (example with dummy table)
df_class = pd.DataFrame({'Pclass':[1,2,3],'Description':['First','Second','Third']})
df_class.to_sql("class_table", conn, if_exists="replace", index=False)

pd.read_sql("""
SELECT t.Name, c.Description 
FROM titanic_table t 
JOIN class_table c 
ON t.Pclass_2 = c.Pclass
""", conn)

#2
import sqlite3
import pandas as pd

# Step 1: Create a connection to a new SQLite database file
conn = sqlite3.connect("titanic.db")

# Step 2: Save your cleaned dataset into the database
df_encoded.to_sql("titanic_table", conn, if_exists="replace", index=False)

# Step 3: Run SQL queries and display results using pandas
# SELECT query
print(pd.read_sql("SELECT Name, Age, Fare FROM titanic_table LIMIT 5", conn))

# WHERE query
print(pd.read_sql("SELECT * FROM titanic_table WHERE Age < 18", conn))

# GROUP BY query
print(pd.read_sql("SELECT Sex_male, AVG(Survived) as survival_rate FROM titanic_table GROUP BY Sex_male", conn))

# JOIN query (create a second table and join it)
df_class = pd.DataFrame({'Pclass':[1,2,3],'Description':['First','Second','Third']})
df_class.to_sql("class_table", conn, if_exists="replace", index=False)

print(pd.read_sql("""
SELECT t.Name, t.Age, c.Description
FROM titanic_table t
JOIN class_table c
ON t.Pclass_2 = c.Pclass
LIMIT 5
""", conn))





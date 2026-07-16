#Part A

#1
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("titanic.csv")

# Preview
df.head()

#Part B

#1
df.info()
df.describe(include="all")

#2
df.isnull().sum()
df.duplicated().sum()

#3
#Survival Count
sns.countplot(x="Survived", data=df)
plt.title("Survival Count")
plt.show()
#Survival by Gender
sns.countplot(x="Sex", hue="Survived", data=df)
plt.title("Survival by Gender")
plt.show()
#Age Distribution
sns.histplot(df["Age"], bins=30, kde=True)
plt.title("Age Distribution")
plt.show()
#Survival by Passenger Class
sns.countplot(x="Pclass", hue="Survived", data=df)
plt.title("Survival by Class")
plt.show()
#Fare vs Survival
sns.boxplot(x="Survived", y="Fare", data=df)
plt.title("Fare vs Survival")
plt.show()







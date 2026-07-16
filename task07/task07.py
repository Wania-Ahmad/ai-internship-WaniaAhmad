#Deliverable 1
import sklearn
import pandas as pd
import numpy as np
import matplotlib

print("scikit-learn version:", sklearn.__version__)
print("pandas version:", pd.__version__)
print("numpy version:", np.__version__)
print("matplotlib version:", matplotlib.__version__)

#Deliverable 2

#Part A

#3
from sklearn.model_selection import train_test_split
import numpy as np

# Example dataset
X = np.arange(10).reshape(-1, 1)   # Features
y = np.arange(10)                  # Labels

# Split into train and test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Train shape:", X_train.shape, "Test shape:", X_test.shape)

#Part B
 
#4
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Generate synthetic data
np.random.seed(42)
X = np.sort(np.random.rand(30, 1))
y = np.sin(2 * np.pi * X).ravel() + np.random.randn(30) * 0.1

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

train_errors, test_errors, degrees = [], [], range(1, 10)

for d in degrees:
    poly = PolynomialFeatures(degree=d)
    X_train_poly = poly.fit_transform(X_train)
    X_test_poly = poly.transform(X_test)
    
    model = LinearRegression().fit(X_train_poly, y_train)
    y_train_pred = model.predict(X_train_poly)
    y_test_pred = model.predict(X_test_poly)
    
    train_errors.append(mean_squared_error(y_train, y_train_pred))
    test_errors.append(mean_squared_error(y_test, y_test_pred))

plt.plot(degrees, train_errors, label="Train Error", marker="o")
plt.plot(degrees, test_errors, label="Test Error", marker="o")
plt.xlabel("Model Complexity (Polynomial Degree)")
plt.ylabel("Mean Squared Error")
plt.title("Bias-Variance Tradeoff")
plt.legend()
plt.show()

#Part C

#3
from sklearn.datasets import load_diabetes
import pandas as pd

data = load_diabetes()
X, y = data.data, data.target

print("Features shape:", X.shape)
print("Target shape:", y.shape)

#4
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)

#5
from sklearn.metrics import mean_squared_error, r2_score

y_pred = model.predict(X_test)

print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))

#6
import matplotlib.pyplot as plt

plt.scatter(y_test, y_pred, color="blue")
plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.title("Linear Regression Predictions")
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.show()

#Part D

#1
import pandas as pd

# Load dataset (replace with your own CSV file)
df = pd.read_csv("your_dataset.csv")

# Handle missing values (numerical: fill with mean, categorical: fill with mode)
df.fillna(df.mean(numeric_only=True), inplace=True)
for col in df.select_dtypes(include=['object']).columns:
    df[col].fillna(df[col].mode()[0], inplace=True)

# Encode categorical columns
df = pd.get_dummies(df, drop_first=True)

print(df.head())

#2
from sklearn.model_selection import train_test_split

def split_data(X, y, test_size=0.2):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=42
    )
    print("Train shape:", X_train.shape, "Test shape:", X_test.shape)
    return X_train, X_test, y_train, y_test

#3
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

X = df.drop("target_column", axis=1)   # replace with your target column
y = df["target_column"]

ratios = [0.4, 0.2, 0.1]
results = []

for r in ratios:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=r, random_state=42)
    model = LinearRegression().fit(X_train, y_train)
    y_pred = model.predict(X_test)
    results.append((f"{int((1-r)*100)}/{int(r*100)}", 
                    mean_squared_error(y_test, y_pred), 
                    r2_score(y_test, y_pred)))

print("Split | MSE | R²")
for res in results:
    print(res)

#4
from sklearn.model_selection import cross_val_score

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=5, scoring="r2")
print("Cross-validation scores:", scores)
print("Average CV Score:", scores.mean())

#5
from sklearn.model_selection import learning_curve
import matplotlib.pyplot as plt
import numpy as np

train_sizes, train_scores, test_scores = learning_curve(
    LinearRegression(), X, y, cv=5, scoring="r2", 
    train_sizes=np.linspace(0.1, 1.0, 10)
)

plt.plot(train_sizes, train_scores.mean(axis=1), label="Train Score")
plt.plot(train_sizes, test_scores.mean(axis=1), label="Test Score")
plt.xlabel("Training Set Size")
plt.ylabel("R² Score")
plt.title("Learning Curve")
plt.legend()
plt.show()

#6
def load_data(path, target):
    df = pd.read_csv(path)
    df.fillna(df.mean(numeric_only=True), inplace=True)
    for col in df.select_dtypes(include=['object']).columns:
        df[col].fillna(df[col].mode()[0], inplace=True)
    df = pd.get_dummies(df, drop_first=True)
    X = df.drop(target, axis=1)
    y = df[target]
    return X, y

def train_model(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    return mean_squared_error(y_test, y_pred), r2_score(y_test, y_pred)

#Bonus Task
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Polynomial transformation (degree 2 or 3)
poly = PolynomialFeatures(degree=3)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

# Train polynomial regression model
model_poly = LinearRegression()
model_poly.fit(X_train_poly, y_train)

# Predictions
y_pred_poly = model_poly.predict(X_test_poly)

# Evaluation
print("Polynomial MSE:", mean_squared_error(y_test, y_pred_poly))
print("Polynomial R²:", r2_score(y_test, y_pred_poly))

# Plain linear regression results (from Part C)
print("Linear MSE:", mean_squared_error(y_test, y_pred))
print("Linear R²:", r2_score(y_test, y_pred))

# Polynomial regression results (from above)
print("Polynomial MSE:", mean_squared_error(y_test, y_pred_poly))
print("Polynomial R²:", r2_score(y_test, y_pred_poly))

import matplotlib.pyplot as plt

plt.scatter(y_test, y_pred, color="blue", label="Linear")
plt.scatter(y_test, y_pred_poly, color="green", label="Polynomial (deg=3)")
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.title("Linear vs Polynomial Regression")
plt.legend()
plt.show()

#Deliverable 4
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.datasets import load_diabetes

# Load dataset
data = load_diabetes()
X, y = data.data, data.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))

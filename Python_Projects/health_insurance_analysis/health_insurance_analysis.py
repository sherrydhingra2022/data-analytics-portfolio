# 1. Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 2. Load Data
df = pd.read_csv('health_insurance_data.csv')

# 3. Data Overview
df.info()
df.describe()

# 4. Visualizations
sns.boxplot(data=df, x='smoker', y='charges')
sns.barplot(data=df, x='region', y='charges')
sns.scatterplot(data=df, x='bmi', y='charges', hue='smoker')

# 5. Optional: Predictive Model
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Encode categorical variables
df['smoker'] = LabelEncoder().fit_transform(df['smoker'])
df['gender'] = LabelEncoder().fit_transform(df['gender'])
df['region'] = LabelEncoder().fit_transform(df['region'])

# Model
X = df[['age', 'bmi', 'children', 'smoker']]
y = df['charges']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = LinearRegression().fit(X_train, y_train)
print("Model score:", model.score(X_test, y_test))

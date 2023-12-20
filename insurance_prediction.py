# -*- coding: utf-8 -*-
"""Insurance_prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WFPaQJhv1OB2ldV6blnBDYicCysEvdQd
"""

import pandas as pd
import numpy as np
import matplotlib as plot
import seaborn as sns

"""# **Data Preprocessing**"""

insurance = pd.read_csv("insurance.csv")

insurance.head()

insurance.tail()

insurance.shape

print("number of rows----->>>", insurance.shape[0])
print("number of columns----->>>", insurance.shape[1])

insurance.info()

insurance.isnull().sum()

insurance.describe()#(include="all")

"""# **EDA**"""

import matplotlib.pyplot as plt

# Distribution plot for 'age'
sns.histplot(insurance['age'], kde=True)
plt.title('Distribution of Age')
plt.show()

# Distribution plot for 'bmi'
sns.histplot(insurance['bmi'], kde=True)
plt.title('Distribution of BMI')
plt.show()

# Distribution plot for 'children'
sns.histplot(insurance['children'], kde=True)
plt.title('Distribution of Children')
plt.show()

# Distribution plot for 'charges'
sns.histplot(insurance['charges'], kde=True)
plt.title('Distribution of Charges')
plt.show()

# Scatter plot for 'age' vs 'charges'
sns.scatterplot(x='age', y='charges', data=insurance)
plt.title('Age vs Charges')
plt.show()

# Scatter plot for 'bmi' vs 'charges'
sns.scatterplot(x='bmi', y='charges', data=insurance)
plt.title('BMI vs Charges')
plt.show()

# Scatter plot for 'children' vs 'charges'
sns.scatterplot(x='children', y='charges', data=insurance)
plt.title('Children vs Charges')
plt.show()


# Bar plot for 'sex' vs 'charges'
sns.barplot(x='sex', y='charges', data=insurance)
plt.title('Sex vs Charges')
plt.show()

# Bar plot for 'smoker' vs 'charges'
sns.barplot(x='smoker', y='charges', data=insurance)
plt.title('Smoker vs Charges')
plt.show()

# Bar plot for 'region' vs 'charges'
sns.barplot(x='region', y='charges', data=insurance)
plt.title('Region vs Charges')
plt.show()

"""# **Encoding**"""

insurance.sex.value_counts()

insurance['sex'] = insurance['sex'].map({'female':0, 'male':1})

insurance.smoker.value_counts()

insurance['smoker'] = insurance['smoker'].map({'yes':0, 'no':1})

insurance.region.value_counts()

insurance['region'] = insurance['region'].map({'southeast': 1, 'southwest': 2, 'northwest': 3, 'northeast': 4})

"""# **split the data**"""

X = insurance.drop(['charges'], axis = 1)
y = insurance['charges']

from sklearn.model_selection import train_test_split

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

X_train,
#y_train

# Support Vector Machines (SVM)
from sklearn.svm import SVR

# Linear Regression
from sklearn.linear_model import LinearRegression

# Random Forest
from sklearn.ensemble import RandomForestRegressor

# Gradient Boosting Regressor
from sklearn.ensemble import GradientBoostingRegressor

# Create an SVM model
svm_model = SVR()
svm_model.fit(X_train, y_train)

# Create a Linear Regression model
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

# Create a Random Forest model
random_forest_model = RandomForestRegressor()
random_forest_model.fit(X_train, y_train)

# Create a Gradient Boosting Regressor model
gradient_boosting_model = GradientBoostingRegressor()
gradient_boosting_model.fit(X_train, y_train)

y_pred1 = svm_model.predict(X_test)
y_pred2 = linear_model.predict(X_test)
y_pred3 = random_forest_model.predict(X_test)
y_pred4 = gradient_boosting_model.predict(X_test)

df1 = pd.DataFrame({'Actual': y_test,
                    'svm_model': y_pred1,
                    'linear_model': y_pred2,
                    'random_forest': y_pred3,
                    'gradient_boosting': y_pred4})

df1

plt.subplot(221)
plt.plot(df1['Actual'].iloc[0:11], label = 'Actual')
plt.plot(df1['svm_model'].iloc[0:11], label = 'svm_model')
plt.legend()

plt.subplot(221)
plt.plot(df1['Actual'].iloc[0:11], label = 'Actual')
plt.plot(df1['svm_model'].iloc[0:11], label = 'svm_model')
plt.legend()

plt.subplot(222)
plt.plot(df1['Actual'].iloc[0:11], label = 'Actual')
plt.plot(df1['linear_model'].iloc[0:11], label = 'linear_model')
plt.legend()

plt.subplot(223)
plt.plot(df1['Actual'].iloc[0:11], label = 'Actual')
plt.plot(df1['random_forest'].iloc[0:11], label = 'random_forest')
plt.legend()

plt.subplot(224)
plt.plot(df1['Actual'].iloc[0:11], label = 'Actual')
plt.plot(df1['gradient_boosting'].iloc[0:11], label = 'gradient_boosting')
plt.legend()

plt.plot(df1['linear_model'], label = 'linear_model')
plt.plot(df1['random_forest'], label = 'random_forest')
plt.plot(df1['gradient_boosting'], label = 'gradient_boosting')

import matplotlib.pyplot as plt

plt.subplot(221)
plt.plot(df1['Actual'].iloc[0:11], label='Actual')
plt.plot(df1['svm_model'].iloc[0:11], label='svm_model')
plt.legend()
plt.title('Actual vs svm_model')
plt.xlabel('Index')
plt.ylabel('Values')

# If you want to show the plot
plt.show()

# Create subplots
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))

# Subplot for SVM model
axes[0, 0].scatter(df1['Actual'], df1['svm_model'], label='SVM Model', alpha=0.7)
axes[0, 0].plot(df1['Actual'], df1['Actual'], color='red', linestyle='--', label='Perfect Prediction')
axes[0, 0].set_title('SVM Model')
axes[0, 0].set_xlabel('Actual Values')
axes[0, 0].set_ylabel('Predicted Values')
axes[0, 0].legend()

# Subplot for Linear Regression model
axes[0, 1].scatter(df1['Actual'], df1['linear_model'], label='Linear Model', alpha=0.7)
axes[0, 1].plot(df1['Actual'], df1['Actual'], color='red', linestyle='--', label='Perfect Prediction')
axes[0, 1].set_title('Linear Regression Model')
axes[0, 1].set_xlabel('Actual Values')
axes[0, 1].set_ylabel('Predicted Values')
axes[0, 1].legend()

# Subplot for Random Forest model
axes[1, 0].scatter(df1['Actual'], df1['random_forest'], label='Random Forest Model', alpha=0.7)
axes[1, 0].plot(df1['Actual'], df1['Actual'], color='red', linestyle='--', label='Perfect Prediction')
axes[1, 0].set_title('Random Forest Model')
axes[1, 0].set_xlabel('Actual Values')
axes[1, 0].set_ylabel('Predicted Values')
axes[1, 0].legend()

# Subplot for Gradient Boosting model
axes[1, 1].scatter(df1['Actual'], df1['gradient_boosting'], label='Gradient Boosting Model', alpha=0.7)
axes[1, 1].plot(df1['Actual'], df1['Actual'], color='red', linestyle='--', label='Perfect Prediction')
axes[1, 1].set_title('Gradient Boosting Model')
axes[1, 1].set_xlabel('Actual Values')
axes[1, 1].set_ylabel('Predicted Values')
axes[1, 1].legend()

# Adjust layout
plt.tight_layout()
plt.show()

"""# **Evaluvation metrics**"""

from sklearn import metrics

score1 = metrics.r2_score(y_test, y_pred1)
score2 = metrics.r2_score(y_test, y_pred2)
score3 = metrics.r2_score(y_test, y_pred3)
score4 = metrics.r2_score(y_test, y_pred4)

print(score1, score2, score3, score4)

m1 = metrics.mean_absolute_error(y_test, y_pred1)
m2 = metrics.mean_absolute_error(y_test, y_pred2)
m3 = metrics.mean_absolute_error(y_test, y_pred3)
m4 = metrics.mean_absolute_error(y_test, y_pred4)

print(m1, m2, m3, m4)

"""**PREDICT NEWCUSTOMER**"""

data = {'age' : 28,
        'sex' : 1,
        'bmi' : 42.60,
        'children' : 4,
        'smoker' : 1,
        'region' : 2
        }

df = pd.DataFrame(data, index = [0])
df

new_cus = gradient_boosting_model.predict(df)
new_cus

"""**SAVE MODEL**"""

xgb = GradientBoostingRegressor()
xgb.fit(X, y)

import joblib

joblib.dump(xgb,'model_joblib_xgb')

model = joblib.load('model_joblib_xgb')

model.predict(df)

"""# **GUI**"""

from tkinter import *

import joblib

import tkinter as tk
from tkinter import ttk
import pandas as pd
# Assuming you have already trained your models (svm_model, linear_model, random_forest_model, gradient_boosting_model)

# Create a sample DataFrame for input features
sample_data = {'age': [28],
               'sex': [1],
               'bmi': [42.60],
               'children': [4],
               'smoker': [1],
               'region': [2]}

df_input = pd.DataFrame(sample_data)

# Function to get predictions
def get_predictions():
    input_values = {
        'age': int(age_var.get()),
        'sex': int(sex_var.get()),
        'bmi': float(bmi_var.get()),
        'children': int(children_var.get()),
        'smoker': int(smoker_var.get()),
        'region': int(region_var.get())
    }

    # Create a DataFrame with the input values
    input_df = pd.DataFrame(input_values, index=[0])

    # Make predictions using the trained models
    svm_prediction = svm_model.predict(input_df)
    linear_prediction = linear_model.predict(input_df)
    random_forest_prediction = random_forest_model.predict(input_df)
    gradient_boosting_prediction = gradient_boosting_model.predict(input_df)

    # Update the result labels
    result_label_svm.config(text=f"SVM Prediction: {svm_prediction[0]:.2f}")
    result_label_linear.config(text=f"Linear Prediction: {linear_prediction[0]:.2f}")
    result_label_rf.config(text=f"Random Forest Prediction: {random_forest_prediction[0]:.2f}")
    result_label_gb.config(text=f"Gradient Boosting Prediction: {gradient_boosting_prediction[0]:.2f}")

# Create Tkinter window
window = tk.Tk()
window.title("Model Predictions")

# Create labels and entry widgets for input features
labels = ['Age:', 'Sex:', 'BMI:', 'Children:', 'Smoker:', 'Region:']
entries = []

for i, label_text in enumerate(labels):
    label = ttk.Label(window, text=label_text)
    label.grid(row=i, column=0, padx=5, pady=5, sticky='e')

    entry = ttk.Entry(window)
    entry.grid(row=i, column=1, padx=5, pady=5)
    entries.append(entry)

# Set default values in entry widgets
entries[0].insert(0, '28')
entries[1].insert(0, '1')
entries[2].insert(0, '42.60')
entries[3].insert(0, '4')
entries[4].insert(0, '1')
entries[5].insert(0, '2')

# Button to get predictions
predict_button = ttk.Button(window, text='Get Predictions', command=get_predictions)
predict_button.grid(row=len(labels), column=0, columnspan=2, pady=10)

# Labels to display predictions
result_label_svm = ttk.Label(window, text="SVM Prediction: ")
result_label_svm.grid(row=len(labels) + 1, column=0, columnspan=2)

result_label_linear = ttk.Label(window, text="Linear Prediction: ")
result_label_linear.grid(row=len(labels) + 2, column=0, columnspan=2)

result_label_rf = ttk.Label(window, text="Random Forest Prediction: ")
result_label_rf.grid(row=len(labels) + 3, column=0, columnspan=2)

result_label_gb = ttk.Label(window, text="Gradient Boosting Prediction: ")
result_label_gb.grid(row=len(labels) + 4, column=0, columnspan=2)

# Run the Tkinter event loop
window.mainloop()








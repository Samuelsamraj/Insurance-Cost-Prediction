
# Insurance Prediction Project

This project involves predicting insurance charges using machine learning models. The dataset used in this project includes information about individuals such as age, sex, BMI, number of children, smoking status, and region. Various machine learning models, including Support Vector Machines (SVM), Linear Regression, Random Forest, and Gradient Boosting Regressor, were used for prediction.

## Contents
- [Data Preprocessing](#data-preprocessing)
- [Exploratory Data Analysis (EDA)](#eda)
- [Encoding Categorical Variables](#encoding)
- [Splitting the Data](#splitting-the-data)
- [Model Training](#model-training)
- [Model Evaluation](#model-evaluation)
- [Predicting for New Customer](#predicting-for-new-customer)
- [Saving the Model](#saving-the-model)
- [Graphical User Interface (GUI)](#gui)

## Data Preprocessing

The dataset (`insurance.csv`) is loaded and explored to understand its structure and contents. The dataset is then preprocessed, including handling missing values and checking for outliers.

## Exploratory Data Analysis (EDA)

Exploratory Data Analysis is performed to understand the distribution of variables and relationships between them. Various plots such as histograms and scatter plots are created for visualizing the data.

## Encoding Categorical Variables

Categorical variables like 'sex', 'smoker', and 'region' are encoded for better compatibility with machine learning models.

## Splitting the Data

The dataset is split into training and testing sets using the `train_test_split` function from scikit-learn.

## Model Training

Four machine learning models (SVM, Linear Regression, Random Forest, Gradient Boosting Regressor) are trained using the training data.

## Model Evaluation

The models are evaluated using metrics such as R-squared and mean absolute error. The evaluation results provide insights into the performance of each model.

## Predicting for New Customer

A new customer's information is provided, and the trained model predicts the insurance charges for that individual.

## Saving the Model

The Gradient Boosting Regressor model is saved using the `joblib` library. This saved model can be used for future predictions without retraining.

## Graphical User Interface (GUI)

A simple Tkinter-based GUI is provided for user interaction. Users can input values for different features, and the GUI displays predictions from the trained models.

Feel free to clone or download the repository and explore the code!

## Requirements

- Python 3.x
- Required Python libraries (pandas, numpy, matplotlib, seaborn, scikit-learn)


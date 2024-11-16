# Customer Churn Prediction with Machine Learning
This project focuses on predicting customer churn using machine learning techniques. The goal is to identify customers who are likely to leave a service based on their behavior and interactions. The dataset used in this project is from the Telco Customer Churn dataset, available on Kaggle.

The models implemented and compared include:

Random Forest |
XGBoost |
Gradient Boosting |
AdaBoost

Each model is evaluated on various metrics, including accuracy, precision, recall, and F1-score. The best-performing model, Random Forest, is saved for future predictions.

## Table of Contents
Introduction

Dataset

Setup Instructions

Model Comparison

Flask Application

Results

Conclusion

## Introduction
Customer churn prediction is essential for businesses that rely on subscription models. It helps organizations proactively engage with customers who are likely to leave, offering promotions or improved services to retain them.

This project demonstrates how to:

Preprocess the data

Perform exploratory data analysis

Build multiple machine learning models to predict churn

Compare the models and save the best one

## Dataset
The dataset used in this project is the Telco Customer Churn dataset from Kaggle. It includes various features such as customer demographics, service usage, and billing information, and the target variable indicates whether a customer has churned.

Key columns in the dataset:

customerID: Unique identifier for each customer

Churn: The target variable (1 for churn, 0 for no churn)

MonthlyCharges: Monthly charges for the customer

tenure: Number of months the customer has been with the company

Other demographic and service usage columns

## Setup Instructions
Prerequisites

Before running the code, make sure you have the following libraries installed:

pandas,
numpy,
matplotlib,
seaborn,
scikit-learn,
xgboost,
imblearn,
pickle

#### Running the Model
Load the dataset.

Perform data preprocessing (encoding categorical variables, handling missing data, etc.).

Split the data into training and testing sets.

Train and evaluate multiple machine learning models, including Random Forest, XGBoost, Gradient Boosting, and AdaBoost.

## Model Comparison
The following models were evaluated for churn prediction:

Model	Accuracy:|	Precision |	Recall |	F1-Score |	Precision |	Recall |	F1-Score |

Random Forest:   |	0.78|	0.76|	0.82|	0.79|	0.80|	0.72|	0.76|

XGBoost:	   | 0.80|	0.78|	0.84|	0.81|	0.83|	0.74|	0.78|

Gradient Boosting:    |	0.77|	0.74|	0.79|	0.76|	0.78|	0.71|	0.74|

AdaBoost:    |	0.75|	0.73|	0.77|	0.75|	0.75|	0.69|	0.72|

#### Final Model Selection:
Given its strong performance across all metrics, the Random Forest model was selected as the final model for deployment

## Flask Application
The Flask application serves the Random Forest model and allows users to input new customer data through a form. The model predicts whether the customer is likely to churn based on their input features.

## Results
After training and comparing different machine learning models (Random Forest, XGBoost, Gradient Boosting, and AdaBoost), the Random Forest model was selected as the best-performing model based on several metrics such as accuracy, precision, recall, and F1-score.

##### Key Insights:
The Random Forest model had the highest accuracy (78%) and performed well in terms of recall, precision, and F1-score for both classes (churn and not churn).

XGBoost and Gradient Boosting models had slightly lower accuracy but still showed strong performance.

AdaBoost performed the worst, with the lowest overall accuracy and F1-scores.

## Conclusion
This project demonstrated how to build and deploy a customer churn prediction system using machine learning and Flask. The following key steps were covered:

Data Preprocessing: cleaned and prepared the data, including handling missing values and encoding categorical variables.

Model Training and Evaluation: Multiple machine learning models were trained, evaluated, and compared. The Random Forest model showed the best performance and was chosen as the final model.

Model Deployment with Flask: The trained Random Forest model was saved using pickle and deployed as a Flask web application, allowing users to input customer data and receive real-time churn predictions.

<img width="1440" alt="output3" src="https://github.com/user-attachments/assets/43a0cd00-2f71-4288-8d40-83a13e1ebcf9">
<img width="1440" alt="output2" src="https://github.com/user-attachments/assets/8e9f84fc-8479-431d-9775-17c736e51576">
<img width="1440" alt="output1" src="https://github.com/user-attachments/assets/ef59da63-1387-435f-805e-b2fc978dc974">

# Big-Mart-sales-prediction-system

🛒 Big Mart Sales Prediction System
📌 Project Overview

The Big Mart Sales Prediction System is a Machine Learning project that predicts the sales of products in different Big Mart outlets based on various product and store attributes. The objective of this project is to build a predictive model that helps businesses estimate product sales using historical data and improve inventory planning and decision-making.

The model analyzes factors such as product type, weight, visibility, outlet size, outlet location, and item category to predict the Item Outlet Sales.

🎯 Objectives

Analyze Big Mart sales data using Exploratory Data Analysis (EDA)
Perform data preprocessing and feature engineering
Train machine learning models to predict product sales
Evaluate the model using appropriate metrics
Build a system that can accurately predict future sales

📂 Dataset

The dataset contains information about products sold at different Big Mart outlets.
Important Features:

Item Identifier – Unique ID of the product
Item Weight – Weight of the product
Item Fat Content – Low Fat or Regular
Item Visibility – Percentage of total display area allocated to the product
Item Type – Category of the product
Item MRP – Maximum Retail Price of the product
Outlet Identifier – Unique store ID
Outlet Size – Size of the store (Small/Medium/High)
Outlet Location Type – Tier of the city
Outlet Type – Type of outlet (Supermarket/Grocery Store)
Item Outlet Sales – Target variable (sales of the product)

⚙️ Technologies Used

Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
Jupyter Notebook

🔍 Project Workflow

1️⃣ Data Collection
Import the Big Mart dataset containing product and outlet information.

2️⃣ Data Preprocessing

Handle missing values
Encode categorical variables
Feature transformation
Data cleaning

3️⃣ Exploratory Data Analysis (EDA)

Analyze correlations between features
Visualize sales trends
Identify patterns in product categories and outlets

4️⃣ Model Training

Machine Learning models are trained to predict sales. Common models include:
Linear Regression
Random Forest Regressor
Decision Tree Regressor

5️⃣ Model Evaluation

Models are evaluated using:
R² Score
Mean Absolute Error
Mean Squared Error

6️⃣ Prediction
The trained model predicts Item Outlet Sales based on input features.

📊 Results
The trained model successfully predicts sales based on product and outlet attributes. Feature importance analysis helps identify the key factors affecting product sales such as Item MRP, Outlet Type, and Product Category.

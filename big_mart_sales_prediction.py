# -*- coding: utf-8 -*-
#importing the dependencies

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from xgboost import XGBRFRegressor
from sklearn import metrics

"""Data collection and analysis

"""

# loading the dataset from csv to pandas

big_mart = pd.read_csv("/content/sample_data/bigmart.csv")

big_mart.head()

#number of data points and number of features

big_mart.shape

#getting some information about the data set

big_mart.info()

"""Categorical features:
1.Item_Identifier            
2.Item_Fat_Content
3.Item_Type
4.Outlet_Identifier
5.Outlet_Location_Type
6.Outlet_Type
"""

big_mart.isnull().sum()

"""Handling missing values"""

#mean value of item weight column
big_mart["Item_Weight"].mean()

#filling the missing values in "item-weight" column with "Mean" Value

big_mart["Item_Weight"].fillna(big_mart["Item_Weight"].mean(),inplace=True)

big_mart.isnull().sum()

"""replacing the missing values in "outlet-size with mode"""

mode_of_outlet_size = big_mart.pivot_table(values="Outlet_Size",columns="Outlet_Type",aggfunc=(lambda x:x.mode()[0]))

print(mode_of_outlet_size)

missing_values = big_mart["Outlet_Size"].isnull()

print(missing_values)

big_mart.loc[missing_values, "Outlet_Size"] = big_mart.loc[missing_values, "Outlet_Type"].apply(
    lambda x: mode_of_outlet_size[x])

big_mart.isnull().sum()

# data analysis
#statistical measures about the data
big_mart.describe()

"""Numerical Features"""

sns.set()

#item weight distribution
plt.figure(figsize=(6,6))
sns.distplot(big_mart['Item_Weight']) #distribution plot
plt.show(block=True)

#item weight distribution
plt.figure(figsize=(6,6))
sns.distplot(big_mart['Item_Visibility']) #distribution plot
plt.show(block=True)

#item weight distribution
plt.figure(figsize=(6,6))
sns.distplot(big_mart['Item_MRP']) #distribution plot
plt.show(block=True)

#item weight distribution
plt.figure(figsize=(6,6))
sns.countplot(x='Outlet_Establishment_Year',data=big_mart) #count distribution plot
plt.show(block=True)

#item weight distribution
plt.figure(figsize=(6,6))
sns.distplot(big_mart['Item_Outlet_Sales']) #distribution plot
plt.show(block=True)


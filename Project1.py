# Renewable Energy is a Time Series Problem because it depends upon wind energy and wind direction.
# Data PreProcessing 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math 
import xgboost as xgt
# XGBoost extends traditional gradient boosting by including regularization elements in the objective function, XGBoost improves generalization and prevents overfitting.

# Reading Dataset

data = pd.read_csv("Turbine_Data.csv" , parse_dates = ['Unnamed:0'] , index_col = ['Unnamed:0'])
data_index = pd.to_datetime(data.index)
print(data.head())
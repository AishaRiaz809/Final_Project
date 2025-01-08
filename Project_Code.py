# Final Project

# Importing Python libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Function for importing first dataset

def data_load(file_path):
    return pd.read_csv(file_path)

# Function for importing second dataset

def data_load2(file_path):
    return pd.read_csv(file_path)

# Loading in first dataset

file_path = "Data/Spending_TestScores.csv" 
education_data = data_load(file_path)
print(education_data.head())

# Loading in second dataset

file_path = "Data/Education_Spending.csv"
gdp_data = data_load2(file_path)
print(gdp_data.head())

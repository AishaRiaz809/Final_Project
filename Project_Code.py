# Final Project

# Importing Python libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Function for importing data

def data_load(file_path):
    return pd.read_csv(file_path)

# Loading in first dataset

file_path = "Data/Education_Spending.csv" 
education_data = data_load(file_path)
print(education_data.head())

# Loading in second dataset

file_path = "Data/Spending_TestScore.csv"
testscore_data = data_load(file_path)
print(testscore_data.head())



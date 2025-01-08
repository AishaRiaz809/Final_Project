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

# Merging 'Public spending on education as a share of GDP' from Education_Spending into Spending_TestScores

def merge_datasets(education_data, gdp_data):
    merged_data = pd.merge(
    education_data,
    gdp_data[['Entity', 'Year', 'Public spending on education as a share of GDP']], # columns I want to keep
    on = ['Entity', 'Year'], # Same column names from the first and second dataset
    how = 'left' # Merged column will be added to the left side of the dataset
    )
    return merged_data

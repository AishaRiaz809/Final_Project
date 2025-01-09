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
# print(education_data.head())

# Loading in second dataset

file_path = "Data/Education_Spending.csv"
gdp_data = data_load2(file_path)
# print(gdp_data.head())

# Checking how many columns are in education_data and gdp_data

# print("Columns in education_data:", education_data.columns)
# print("Columns in gdp_data:", gdp_data.columns)

# Merging 'Public spending on education as a share of GDP' from Education_Spending into Spending_TestScores

def merge_datasets(education_data, gdp_data):
    merged_data = pd.merge(
    education_data,
    gdp_data[['Entity', 'Year', 'Public spending on education as a share of GDP']], # columns I want to keep
    on = ['Entity', 'Year'], # Same column names from the first and second dataset
    how = 'left' # Merged column will be added to the left side of the dataset
    )
    return merged_data


# Checking columns in merged_data

merged_data = merge_datasets(education_data, gdp_data)
print("Columns in merged_data:", merged_data.columns)
print("Number of columns inmerged_data:", len(merged_data.columns))

# Renaming the columns

merged_data.columns = [
    'Country',
    'Country_Code',
    'Year',
    'Test_Scores',
    'Government_Expenditure',
    'World_Regions',
    'Public_Spending'
]

# print(merged_data.columns)

# Function for bar chart for harmonised test scores

def plot_barscores(merged_data):
    
    # Filter for correct years and countries
    years_filtered = [2010, 2017, 2018, 2020]
    filtered_data = merged_data[merged_data['Country'].isin(['United States', 'Finland']) & merged_data['Year'].isin(years_filtered)]

    pivot_data = filtered_data.pivot(index = 'Year', columns = 'Country', values = 'Test_Scores')

    x = np.arange(len(pivot_data))

    bar_width = 0.4

    # Plotting the graph
    fig, ax = plt.subplots(figsize = (10, 6))

    ax.bar(x-bar_width/2, pivot_data['United States'], bar_width, label = 'United States', color = 'blue')
    ax.bar(x+bar_width/2, pivot_data['Finland'], bar_width, label = 'Finland')

    # Labelling the graph
    ax.set_xlabel('Year')
    ax.set_ylabel('Test Scores')
    ax.set_title('Test Scores by Country (United States and Finland)')
    ax.set_xticks(x)
    ax.set_xticklabels(pivot_data.index)
    ax.legend()
    
    plt.show()

# Calling the function to print the graph
plot_barscores(merged_data)


# Function for dual axis bar chart for Government Expenditure and Harmonsied Test Scores
def plot_dualbar(merged_data):

    # Filtering the data
    years_filtered = [2010, 2017, 2018, 2020]
    filtered_data = merged_data[merged_data['Country'].isin(['United States', 'Finland']) & merged_data['Year'].isin(years_filtered)
    ]

    pivot_data = filtered_data.pivot(index = 'Year', columns = 'Country', values = 'Test_Scores')
    pivot_expenditure = filtered_data.pivot(index = 'Year', columns = 'Country', values = 'Government_Expenditure')

    x = np.arange(len(pivot_data))

    bar_width = 0.4

    # Plotting the graphs
    fig, ax1 = plt.subplots(figsize = (10, 6))

    ax1.bar(x-bar_width/2, pivot_data['United States'], bar_width, label = 'United States', color = '#4E79A7')
    ax1.bar(x+bar_width/2, pivot_data['Finland'], bar_width, label = 'Finland', color = '#A0CBE8')

    # Labelling the graphs
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Test Scores')
    ax1.set_title('Test Scores and Government Expenditure for the United States and Finland')
    ax1.set_xticks(x)
    ax1.set_xticklabels(pivot_data.index)
    ax1.legend(loc = 'center left')

    # Second y-axis
    ax2 = ax1.twinx()

    ax2.plot(x, pivot_expenditure['United States'], label = 'United States', color = 'red')
    ax2.plot(x, pivot_expenditure['Finland'], label = 'Finland', color = 'blue')

    # Labelling the second y-axis
    ax2.set_ylabel('Government Expenditure on Education in millions ($)')
    ax2.legend(loc = 'center right')

    plt.show()

# Calling the function to plot the graph
plot_dualbar(merged_data)

# Function for line graph

def plot_linegraph(merged_data):

    # Filtering for specific years and countries (countries that are considered to have highly successful education systems)
    years_filtered = merged_data[merged_data['Year'].isin([2015, 2016, 2017, 2018, 2019, 2020, 2021])]
    countries_filtered = years_filtered[years_filtered['Country'].isin(['United States', 'Finland', 'Japan', 'Sweden', 'Norway', 'Netherlands'])]
    # Ordering the points
    countries_filtered = countries_filtered.sort_values(by = 'Year')

    # Calcualting the average percentage
    avg_spending = merged_data[merged_data['Year'].isin([2015, 2016, 2017, 2018, 2019, 2020, 2021])]['Public_Spending'].mean()

    # Plotting the graph
    plt.figure(figsize = (10, 6))

    for country in ['United States', 'Finland', 'Japan', 'Sweden', 'Norway', 'Netherlands']:
        countries_data = countries_filtered[countries_filtered['Country'] == country]
        plt.plot(countries_data['Year'], countries_data['Public_Spending'], label = country)

    # Average line
    plt.axhline(avg_spending, color = 'red', linestyle = '--', label = f'Average Public Spending ({avg_spending:.2f})')

    # Labelling the graph
    plt.title('Public Spending as a share of GDP (%) for the United States and Finland from 2018-2021')
    plt.xlabel('Year')
    plt.ylabel('Public Spending on Education as a share of GDP (%)')
    plt.xticks([2015, 2016, 2017, 2018, 2019, 2020, 2021])
    plt.legend(loc = 'lower left')

    plt.show()

plot_linegraph(merged_data)
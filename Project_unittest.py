import unittest
import pandas as pd
from Project_Code import data_load
from Project_Code import data_load2
from Project_Code import merge_datasets
from Project_Code import plot_barscores
from Project_Code import plot_dualbar
from Project_Code import plot_linegraph

class TestDataLoad(unittest.TestCase):

    # Test to check first dataset is loaded in correctly
    def test_file_load(self):
        file_path = "Data/Spending_TestScores.csv"
        data = data_load(file_path)
        self.assertIsInstance(data, pd.DataFrame)

    # Test to check the first datset has the correct number of columns - 6
    def test_data_columns(self):
        file_path = "Data/Spending_TestScores.csv"
        data = data_load(file_path)
        self.assertEqual(len(data.columns), 6)

    # Test to check that 'Year', 'Harmonised Test Scores' and 'Government Expenditure on Education' are numeric
    def test_numeric_columns(self):
        file_path = "Data/Spending_TestScores.csv"
        data = data_load(file_path)
        numeric_columns = ['Year', 'Harmonized test scores', 'Government expenditure on education, PPP$ (millions)']
        for col in numeric_columns:
            self.assertTrue(pd.api.types.is_numeric_dtype(data[col])), f"{col} is not numeric"

    # Test to check the second dataset is loaded in correctly
    def test_file_load2(self):
        file_path2 = "Data/Education_Spending.csv"
        data2 = data_load2(file_path2)
        self.assertIsInstance(data2, pd.DataFrame)

    # Test to check the second dataset has the correct number of columns - 4
    def test_data_columns2(self):
        file_path2 = "Data/Education_Spending.csv"
        data2 = data_load2(file_path2)
        self.assertEqual(len(data2.columns), 4)

    # Test to check that 'Year' and 'Public Spending as percent of GDP' are numeric
    def test_numeric_columns2(self):
        file_path2 = "Data/Education_Spending.csv"
        data2 = data_load2(file_path2)
        numeric_columns2 = ['Year', 'Public spending on education as a share of GDP']
        for col2 in numeric_columns2:
            self.assertTrue(pd.api.types.is_numeric_dtype(data2[col2]), f"{col2} is not numeric")

    # Test to check the number of columns in the merged dataset
    def test_merged_data(self):
        file_path = "Data/Spending_TestScores.csv"
        education_data = data_load(file_path)
        file_path2 = "Data/Education_Spending.csv"
        gdp_data = data_load2(file_path2)
        merged_data_test = merge_datasets(education_data, gdp_data)
        self.assertEqual(len(merged_data_test.columns), 7)

    # Merging data to use for unittests for graphs
    def setUp(self):
        file_path1 = "Data/Spending_TestScores.csv"
        file_path2 = "Data/Education_Spending.csv"

        data1 = data_load(file_path1)
        data2 = data_load(file_path2)

        self.merged_data = merge_datasets(data1, data2)

        self.merged_data.rename(columns={
            'Harmonized test scores': 'Test_Scores',
            'Government expenditure on education, PPP$ (millions)': 'Government_Expenditure',
            'Public spending on education as a share of GDP': 'Public_Spending',
            'Entity': 'Country'
        }, inplace=True)

    def test_manual_setup_call(self):
        self.setUp()
        self.assertIsNotNone(self.merged_data, "Merged data should not be None")
    
    # Test to check that the columns 'Year and 'Test_Scores' are numeric in plot_barscores
    def test_datatypes_barscores(self):
        #print(f"self.merged_data in test_datatypes_barscores: {self.merged_data}")
        self.assertTrue(pd.api.types.is_numeric_dtype(self.merged_data['Year']), "Year column is not numeric")
        self.assertTrue(pd.api.types.is_numeric_dtype(self.merged_data['Test_Scores']), "Test_Scores column is not numeric")

    # Test to check the data has been correctly pivoted for the plot_barscores graph
    def test_pivot_barscores(self):
        years_filtered = [2010, 2017, 2018, 2020]
        countries_filtered = ['United States', 'Finland']
        filtered_data = self.merged_data[
            self.merged_data['Country'].isin(countries_filtered) & self.merged_data['Year'].isin(years_filtered)
        ]
        pivot_data = filtered_data.pivot(index = 'Year', columns = 'Country', values = 'Test_Scores')
        self.assertTrue('United States' in pivot_data.columns, "United States column missing in pivot")
        self.assertTrue('Finland' in pivot_data.columns, "Finland column missing in pivot")
        self.assertEqual(len(pivot_data), len(years_filtered), "Pivot table has incorrect number of rows")

    # Test that filtering works correctly for graph plot_baracores
    def test_filtering_dualbar(self):
        years_filtered = [2010, 2017, 2018, 2020]
        countries_filtered = ['United States', 'Finland']
        filtered_data = self.merged_data[self.merged_data['Country'].isin(countries_filtered) & self.merged_data['Year'].isin(years_filtered)]
        self.assertFalse(filtered_data.empty, "Filtered data is empty")
        self.assertTrue(all(filtered_data['Year'].isin(years_filtered)), "Year filtering failed")
        self.assertTrue(all(filtered_data['Country'].isin(countries_filtered)), "Country filtering failed")
    
    # Test that 'Test_Scores' and 'Government_Expenditure' are numeric
    def test_numeric_dualbar(self):
        numeric_columns = ['Test_Scores', 'Government_Expenditure']
        for col in numeric_columns:
            self.assertTrue(pd.api.types.is_numeric_dtype(self.merged_data[col]), f"{col} is not numeric")

    # Test for average public spending calculation in graph plot_linegraph
    def test_avg_publicspending(self):
        years_filtered = [2015, 2016, 2017, 2018, 2019, 2020, 2021]
        avg_spending = self.merged_data[self.merged_data['Year'].isin(years_filtered)]['Public_Spending'].mean()
        self.assertIsInstance(avg_spending, float, "Average public spending is not a float")
        self.assertGreater(avg_spending, 0, "Average public spending should be greater than 0")

if __name__ == '__main__':
    unittest.main()
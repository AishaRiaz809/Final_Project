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
        merged_data = merge_datasets(education_data, gdp_data)
        self.assertEqual(len(merged_data.columns), 7)

    # Test to check that the columns 'Year and 'Test_Scores' are numeric in plot_barscores
    # FAILEDD
    def test_datatypes_barscores(self):
        merged_data = self.test_merged_data()
        self.assertTrue(pd.api.types.is_numeric_dtype(self.merged_data['Year']))
        self.assertTrue(pd.api.types.is_numeric_dtype(self.merged_data['Test_Scores']))

    # Test to check

if __name__ == '__main__':
    unittest.main()
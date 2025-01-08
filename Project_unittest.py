import unittest
import pandas as pd
from Project_Code import data_load
from Project_Code import data_load2

class TestDataLoad(unittest.TestCase):

    # Test to check first dataset is loaded in correctly
    def test_file_load(self):
        file_path = "Data/Spending_TestScores.csv"
        data = data_load(file_path)
        self.assertIsInstance(data, pd.DataFrame)

    # Test to check that first datset has the correct number of columns - 6
    def test_data_columns(self):
        file_path = "Data/Spending_TestScores.csv"
        data = data_load(file_path)
        self.assertEqual(len(data.columns), 6)

    # Test to check the second dataset is loaded in correctly
    def test_file_load2(self):
        file_path2 = "Data/Education_Spending.csv"
        data2 = data_load2(file_path2)
        self.assertIsInstance(data2, pd.DataFrame)

if __name__ == '__main__':
    unittest.main()
import unittest
import pandas as pd
from Project_Code import data_load

class TestDataLoad(unittest.TestCase):

    def test_file_load(self):
        file_path = "Data/Spending_TestScores.csv"
        data = data_load(file_path)
        self.assertIsInstance(data, pd.DataFrame)

    def test_data_columns(self):
        file_path = "Data/Spending_TestScores.csv"
        data = data_load(file_path)
        self.assertEqual(len(data.columns), 6)

if __name__ == '__main__':
    unittest.main()
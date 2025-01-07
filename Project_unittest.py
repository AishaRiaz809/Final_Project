import unittest
import pandas as pd
from Project_Code import data_load

class TestDataLoad(unittest.TestCase):

    def test_file_load(self):
        file_path = "Data/Education_Spending.csv"
        data = data_load(file_path)
        self.assertIsInstance(data, pd.DataFrame)

if __name__ == '__main__':
    unittest.main()
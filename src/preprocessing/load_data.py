

"""
Pandas library is used to read the Excel file and load it into a DataFrame for further processing. 
The function `load_data` takes the file path as input and returns the loaded DataFrame.

"""

import pandas as pd

def load_data(file_path):
    """
    Reads an Excel file and returns a pandas DataFrame.
    
    Parameters:
        file_path (str): Path to the Excel file.
        
    Returns:
        pd.DataFrame
    """
    return pd.read_excel(file_path)
  
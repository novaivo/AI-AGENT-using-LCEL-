from langchain.tools import tool
import pandas as pd
import os

@tool
def get_csv_stats(filepath:str)-> str:
    """
    u have to get statistics of stats from the file 
    
    Args:
        filepath (str): the path to the csv file 
    returns:
      str: statistics of the csv file.    
    """

    if not os.path.exists(filepath):
        return f"file not found at{filepath}"
    
    try: 
        df = pd.read_csv(filepath)
        shape_info =  f"✅ shape: {df.shape[0]} rows x {df.shape[1]} columns"
        column_types = df.dtypes.to_string()
        nulls = df.isnull().sum().to_string()
        description = df.describe(include='all').to_string()
    
        return f"{shape_info} \n\n  📊column types: {column_types}\n\n ❓ missing values: {nulls}\n\n  📈stats:\n{description}"
    except Exception as e:
        return f" ❌ Error reading the file: {str(e)}"



import pandas as pd

def load_player_data(filepath):
    """
    Load player data from a CSV file using pandas.
    
    Parameters:
        filepath (str): Relative path to the CSV file
    
    Returns:
        pd.DataFrame: DataFrame containing player data
    """
    try:
        df = pd.read_csv(filepath)
        return df
    except FileNotFoundError:
        print("❌ Data file not found. Check your file path and name.")
        return None

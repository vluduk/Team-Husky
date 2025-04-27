import pandas as pd
import numpy as np


def get_data():
    # Load the dataset
    df = pd.read_csv('X.csv')
    # Drop rows with missing values
    return df

print(get_data().isna().sum().any())
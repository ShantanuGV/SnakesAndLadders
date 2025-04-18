import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data (Replace with actual file path)
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print("Data loaded successfully!")
        print(data.head())

        
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Data Cleaning and Preprocessing
def clean_data(data):
    print("Cleaning data...")
    data = data.dropna()
    print(f"Data after cleaning: {data.shape}")
    return data

# Exploratory Data Analysis
def exploratory_analysis(data):
    print("Performing Exploratory Data Analysis...")
    print(data.describe())
    sns.pairplot(data)
    plt.show()

# Data Visualization
def visualize_data(data, x_col, y_col):
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=x_col, y=y_col, data=data)
    plt.title(f'{y_col} over {x_col}')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.show()

# Main Function
def main():
    file_path = 'data.csv'  # Replace with actual path
    data = load_data(file_path)
    if data is not None:
        data = clean_data(data)
        exploratory_analysis(data)
        # Example visualization (Replace 'Year' and 'GDP' with actual columns)
        visualize_data(data, x_col='Year', y_col='GDP')

if __name__ == "__main__":
    main()

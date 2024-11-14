import pandas as pd
import numpy as np

# Load the data and inspect for issues
data = pd.read_csv('./DCOILWTICO.csv', parse_dates=['DATE'], index_col='DATE')

# Rename columns if necessary
data.columns = data.columns.str.strip()  # Remove any extra whitespace in column names
price_column = 'DCOILWTICO'  # Replace with actual price column name identified earlier

# Convert the Price column to numeric, coercing errors
data[price_column] = pd.to_numeric(data[price_column], errors='coerce')

# Drop rows with NaN in the price column after conversion
data = data.dropna(subset=[price_column])

# Define the window and step size for hopping window
window_size = 7  # 7 days for weekly
step_size = 1    # 1 day for hopping

# Initialize lists to store results
dates = []
mean_prices = []
max_prices = []

# Implement hopping window strategy
for start in range(0, len(data) - window_size + 1, step_size):
    end = start + window_size
    window = data.iloc[start:end]
    dates.append(window.index[-1])  # Use the last date in the window
    mean_prices.append(window[price_column].mean())
    max_prices.append(window[price_column].max())

# Create a DataFrame for the result
result = pd.DataFrame({'Date': dates, 'Weekly Mean Price': mean_prices, 'Weekly Max Price': max_prices})

# Print and save the result
print(result)
result.to_csv('./weekly_crude_oil_stats.csv', index=False)
print("Weekly stats have been saved to 'weekly_crude_oil_stats.csv'")

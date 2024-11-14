import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load and preprocess the data
data = pd.read_csv('./DCOILWTICO.csv', parse_dates=['DATE'], index_col='DATE')
data.columns = data.columns.str.strip()  # Remove any extra whitespace in column names
price_column = 'DCOILWTICO'  # Replace with actual price column name identified earlier
data[price_column] = pd.to_numeric(data[price_column], errors='coerce')
data = data.dropna(subset=[price_column])

# Hopping window calculation
window_size = 7  # 7 days for weekly
step_size = 1    # 1 day for hopping
dates = []
mean_prices = []
max_prices = []

for start in range(0, len(data) - window_size + 1, step_size):
    end = start + window_size
    window = data.iloc[start:end]
    dates.append(window.index[-1])  # Use the last date in the window
    mean_prices.append(window[price_column].mean())
    max_prices.append(window[price_column].max())

# Create a result DataFrame
result = pd.DataFrame({'Date': dates, 'Weekly Mean Price': mean_prices, 'Weekly Max Price': max_prices})

# Plot the result
plt.figure(figsize=(10, 6))
plt.plot(result['Date'], result['Weekly Mean Price'], label='Weekly Mean Price', marker='o')
plt.plot(result['Date'], result['Weekly Max Price'], label='Weekly Max Price', marker='x')
plt.xlabel('Date')
plt.ylabel('Price (Dollars per Barrel)')
plt.title('Weekly Mean and Max Crude Oil Prices (Hopping Window)')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()

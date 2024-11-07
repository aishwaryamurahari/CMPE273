import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a sample time series dataframe
data = {
    'timestamp': pd.date_range(start='2024-01-01', periods=100, freq='H'),
    'value': np.random.randint(1, 10, 100)
}
df = pd.DataFrame(data)

# Set the timestamp as the index
df.set_index('timestamp', inplace=True)

# Define window size and hop size in terms of rows
window_size = 3  # Window duration in number of rows (e.g., 3 hours)
hop_size = 1     # Hop interval in number of rows (e.g., 1 hour)

# Calculate hopping mean using a rolling window
df['hopping_mean'] = df['value'].rolling(window=window_size, min_periods=1).mean()

# Plot the results
df.reset_index(inplace=True)
plt.plot(df['timestamp'], df['value'], label='Original Data')
plt.plot(df['timestamp'], df['hopping_mean'], label='Hopping Mean', linestyle='--')
plt.legend()
plt.show()


import matplotlib
matplotlib.use('Agg')  # Use the Agg backend for non-GUI rendering
import matplotlib.pyplot as plt
import os

def generate_report(data, output_path):
    for reservoir, records in data.items():
        if not records:
            print(f"No data available for {reservoir}")
            continue

        # Extract data with available keys: Date and TAF (Total Acre-Feet)
        dates = [record.get('Date', 'Unknown') for record in records]
        storage_levels = [record.get('TAF', 0) for record in records]  # Using TAF as storage level

        # Plot the data
        plt.figure(figsize=(10, 6))
        plt.bar(dates, storage_levels, label="Current Storage (TAF)", color="blue")
        plt.title(f"{reservoir} Reservoir Storage")
        plt.xlabel("Date")
        plt.ylabel("Storage Level (TAF)")
        plt.legend()

        # Save plot directly to file without displaying it
        os.makedirs(output_path, exist_ok=True)
        plt.savefig(f"{output_path}/{reservoir}_report.png")
        plt.close()  # Close the figure to release memory
        print(f"Report generated for {reservoir}")

    output_path = "./data/daily_reports"
    os.makedirs(output_path, exist_ok=True)
    generate_report(reservoir_data, output_path)


import json
from apscheduler.schedulers.blocking import BlockingScheduler
from mqtt_subscriber import start_subscriber
from report_generator import generate_report
import os

scheduler = BlockingScheduler()

# Start subscriber to collect data
start_subscriber()

def load_data_from_file():
    try:
        with open("reservoir_data.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"oroville": [], "shasta": [], "sonoma": []}

@scheduler.scheduled_job('interval', seconds=10)
def scheduled_job():
    # Load data from file
    reservoir_data = load_data_from_file()
    print("Loaded data in scheduler:", reservoir_data)

    # Generate report if there's data
    if any(reservoir_data.values()):
        output_path = "./data/daily_reports"
        os.makedirs(output_path, exist_ok=True)
        generate_report(reservoir_data, output_path)
        print("Report generated.")
    else:
        print("No data collected for report generation.")

if __name__ == "__main__":
    print("Scheduler started. Waiting for the next scheduled task...")
    scheduler.start()

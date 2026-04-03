import csv
from datetime import datetime

def log_data(location, status):
    with open("../results/test_results.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), location["lat"], location["lon"], status])
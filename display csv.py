import os
import csv
import config

# Function to read and display data from the CSV file
def display_csv_data(csv_file_path):
    if not os.path.exists(csv_file_path):
        print("CSV file not found.")
        return

    with open(csv_file_path, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(', '.join(row))

# Read and display the data from the CSV file using the path from config.py
display_csv_data(config.CSV_FILE_PATH)

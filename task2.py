import csv
import os

def process_and_display(filename):
    records = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            records.append(row)
            print(row)

    positive = sum(1 for r in records if r["Label"].lower() == "positive")
    negative = sum(1 for r in records if r["Label"].lower() == "negative")
    print(f"Positive cases: {positive}, Negative cases: {negative}")

    threshold = 140
    high_glucose = [r for r in records if float(r["Glucose"]) > threshold]
    print(f"Patients with glucose > {threshold}: {len(high_glucose)}")

    avg_bmi = sum(float(r["BMI"]) for r in records) / len(records)
    avg_glucose = sum(float(r["Glucose"]) for r in records) / len(records)
    print(f"Average BMI: {avg_bmi:.2f}, Average Glucose: {avg_glucose:.2f}")

def add_record(filename, record):
    with open(filename, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(record)

def update_record(filename, rec_id, updated_record):
    records = []
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        records.append(header)
        for row in reader:
            if row[0] == str(rec_id):
                records.append(updated_record)
            else:
                records.append(row)
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(records)

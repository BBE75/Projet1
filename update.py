import csv

def update(username)
    data = {}
    with open(CSV_FILE) as fin:
        reader = csv.reader(fin, skipinitialspace=True, quotechar="'")
        for row in reader:
            data[row[0]] = row[1:]


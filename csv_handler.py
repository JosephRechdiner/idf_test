import csv

def convert_csv(file):
    csvreader = csv.reader(file)

    header = next()
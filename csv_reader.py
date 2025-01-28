# handles csv reading

import csv

FILE_PREFIX = "./data/"

# gets a csv from a given filename, returns as a list of dicts
def get_csv(file_name):
    with open(FILE_PREFIX + file_name, newline='') as csv_file:
        csv_data = list(csv.DictReader(csv_file))
    return csv_data



import csv

def write_data (file, fieldnames, data):
    ''' fieldnames parameter is a list, data parameter is a list of dictionaries , each list item is a row'''
    with open(file, mode="w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, lineterminator = '\n')
        writer.writeheader()
        for dict in data:
            writer.writerow(dict)
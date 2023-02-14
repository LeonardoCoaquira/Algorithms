import csv

def readAll(file):
    with open(file, 'r') as file:
        reader = csv.reader(file)
        values = [row for row in reader]
    return values


def readColumn(file,column):
    with open(file, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        column_index = header.index(column)
        column_values = [int(row[column_index]) for row in reader]
    return column_values
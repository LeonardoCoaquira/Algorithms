import csv
ls = []
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    ls = [row for row in reader]

print(ls)
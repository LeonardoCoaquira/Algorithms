import csv
from BSTNode import BSTNode
from BSTNode import insertMany, orderAll

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)
    column_index = header.index('Elo')
    column_values = [int(row[column_index]) for row in reader]

print(column_values)
root = BSTNode(column_values[0])
for i in column_values:
    insertMany(root, BSTNode(i))

result = []
orderAll(root, result, 'PRE')
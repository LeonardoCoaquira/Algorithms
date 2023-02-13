import csv
from BSTNode import BSTNode
from BSTNode import insertMany, orderAll, indexMap, map

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)
    column_index = header.index('Elo')
    column_values = [int(row[column_index]) for row in reader]

print(column_values)
root = BSTNode(column_values[0])
for i in column_values:
    insertMany(root, BSTNode(i))

resPre, resIn, resPs = [], [], []
preOr, preIn, prePs = orderAll(root, resPre, 'PRE'), orderAll(root, resIn, 'IN'), orderAll(root, resPs, 'POST')

vert = {}
map(resPre)
indexMap(resIn, resPre,vert)

print("PreOrder: ",resPre)
print("InOrder: ",resIn)
print("PostOrder: ",resPs)

for x in vert:
    for y in vert[x]:
        ls = ['']*len(vert)
        if x == vert[x][vert[x].index(y)]:
            ls[vert[x].index(y)] = x
            print(ls)
        
        ls = []
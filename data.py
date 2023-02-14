from BSTNode import *
from CSVReader import *

ls = readColumn('data.csv','Elo')

root = BSTNode(ls[0])

insertMany(root, ls)

resPre, resIn, resPs = [], [], []
preOr, preIn, prePs = orderAll(root, resPre, 'PRE'), orderAll(root, resIn, 'IN'), orderAll(root, resPs, 'POST')

vert = {}
map(resPre)
indexMap(resIn, resPre,vert)

print("PreOrder: ",resPre)
print("InOrder: ",resIn)
print("PostOrder: ",resPs,"\n")

printMap(vert)
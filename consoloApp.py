from BSTNode import *

'''ls = readColumn('data.csv','Elo')

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

printMap(vert)'''

vert = {}
print("Bienvenido")
rootText = input("Ingrese el nodo raíz: ")
root = BSTNode(rootText)
var1 = input("Dame otro numero: ")
var2 = input("Dame otro numero: ")
var3 = input("Dame otro numero: ")
var4 = input("Dame otro numero: ")

ls = [var1,var2,var3,var4]
print("Values: ",ls)
insertMany(root, ls)

resPre, resIn, resPs = [], [], []
preOr, preIn, prePs = orderAll(root, resPre, 'PRE'), orderAll(root, resIn, 'IN'), orderAll(root, resPs, 'POST')

map(resPre)
indexMap(resIn, resPre,vert)


printMap(vert)


class BSTNode:
    '''
    Node BST definition
    '''
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        

'''#Creation manual of nodes
node4 = BSTNode(4)
node10 = BSTNode(10)
node12 = BSTNode(12)
node14 = BSTNode(14)
node16= BSTNode(16)
node20 = BSTNode(20)

node9 = BSTNode(9)
node9.left = node4
node9.right = node10

node13 = BSTNode(13)
node13.left = node12
node13.right = node14

node17 = BSTNode(17)
node17.left = node16

node19 = BSTNode(19)
node19.right = node20

node11 = BSTNode(11)
node11.left = node9
node11.right = node13

node18 = BSTNode(18)
node18.left = node17
node18.right = node19

node15 = BSTNode(15)
node15.left = node11
node15.right = node18'''

'''
                15
           /          \ 
          /            \
        11              18
      /    \          /   \
     9      13      17     19
    / \    /  \     /       \
   4  10  12  14   16        20
'''

# Imprime el arbol en inOrder
def inOrder(root, result):
  if not root:
    return
  inOrder(root.left,result)
  result.append(root.data)
  inOrder(root.right,result)

def preOrder(root, result):
  if not root:
    return
  result.append(root.data)
  preOrder(root.left,result)
  preOrder(root.right,result)

def postOrder(root, result):
  if not root:
    return
  postOrder(root.left,result)
  postOrder(root.right,result)
  result.append(root.data)
# Elimina los nodos mandados
def deleteNode(root,dataDel):
  if not root:
    return
  if root.data in dataDel:
    if ((root.left==None) ^ (root.right==None)):
      try:
        root.data = root.left.data
      except: pass
      try:
        root.data = root.right.data
      except: pass
    else:
        try:
            root.data = root.left.data
            root.left.data = None
        except:
            root.data = None
  deleteNode(root.left,dataDel)
  deleteNode(root.right,dataDel)
'''
res = []
inOrder(node15, res)
deleteNode(node15,[12])
print(res)
'''

def insertMany(root, obj):
  if root == None or root.data == obj.data:
    return   
  if obj.data > root.data:
    if root.right != None:
      insertMany(root.right,obj)
    else:
      root.right = obj
  else:
    if root.left != None:
      insertMany(root.left,obj)
    else:
      root.left = obj
      

nodes = [15,10,2,4,1,3,5,30,25,27,32,40,50]
raiz = BSTNode(nodes[0])
for x in nodes:
  insertMany(raiz, BSTNode(x))  


resI = []
resPr = []
resPo = []

inOrder(raiz,resI)
preOrder(raiz,resPr)
postOrder(raiz,resPo)

# Eliminar nodos 4 , 10 , 12, 14 ,16 o 20
#deleteNode(node15, [4 , 10 , 12, 14 ,16, 20])
#xTraversal(node15)

# Eliminar nodos 17 o 19
#deleteNode(node15, [17, 19])
#xTraversal(node15)

#Eliminar cualquier nodo, colocar dentro de la lista
#deleteNode(node15, [13])
#xTraversal(node15)

'''print(resPr)
print(resI)
print(resPo)'''

def mapa(row,column):
  for i in range(len(resPr)):
    for j in range(len(resPr)):
        row.append(resPr[j])     
    column.append(row)
    row = []

def indexMapa(hrz, vert):
  for x in range(len(resI)):
    hrz.append(resI[x])
  for x in range(len(resPr)):
    vert[resPr[x]] = hrz

hrz = []
vert = {}
row = []
column = []
mapa(row, column)
indexMapa(hrz,vert)
#print(hrz)
#print(vert)
'''for x in column:
  print(column.index(x))
  for y in x:
    print(x.index(y))
  print()
'''
for x in vert:
  for y in vert[x]:
      ls = ['']*len(vert)
      if x == vert[x][vert[x].index(y)]:
        ls[vert[x].index(y)] = x
        print(ls)
      
      ls = []
'''
                15
           /          \ 
          /            \
        11              18
      /    \          /   \
     9      13      17     19
    / \    /  \     /       \
   4  10  12  14   16        20
'''

print(raiz.right.data)
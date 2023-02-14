class BSTNode:
    '''
    Create a Node
    '''
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

# Print in different Ordes

def orderAll(root, result, order):
    if root:
        if order == 'PRE':
            result.append(root.data)

        orderAll(root.left, result, order)
        
        if order == 'IN':
            result.append(root.data)

        orderAll(root.right, result, order)
        
        if order == 'POST':
            result.append(root.data)

# Remove submitted nodes in a list
def deleteNode(root,dataDel):
    """
    Delete a Node if exists in dataDel
    """
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

def insertList(root, obj):
    if root == None or root.data == obj.data:
        return
    if obj.data > root.data:
        if root.right != None:
            insertList(root.right,obj)
        else:
            root.right = obj
    else:
        if root.left != None:
            insertList(root.left,obj)
        else:
            root.left = obj

# Create a map with nodes
def map(preOrder,row=[],column=[]):
    """
    Mapping the nodes
    PreOrder given like a list
    """
    for i in range(len(preOrder)):
        for j in range(len(preOrder)):
            row.append(preOrder[j])     
        column.append(row)
        row = []

def indexMap(inOrder, preOrder, vert,hrz=[]):
    for x in range(len(inOrder)):
        hrz.append(inOrder[x])
    for x in range(len(preOrder)):
        vert[preOrder[x]] = hrz

def printMap(data):
    for x in data:
        for y in data[x]:
            ls = ['']*len(data)
            if x == data[x][data[x].index(y)]:
                ls[data[x].index(y)] = x
                print(ls)
            
            ls = []

def printMapTwo(data):
    for x in data:
        for y in data[x]:
            ls = ['']*len(data)
            if x == data[x][data[x].index(y)]:
                ls[data[x].index(y)] = x
                print(ls)
            
            ls = []

def insertMany(firstNode, listNodes):
    for i in listNodes:
        insertList(firstNode, BSTNode(i))
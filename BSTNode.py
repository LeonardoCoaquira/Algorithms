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

# Create a map with nodes
def map(row,column):
  for i in range(len(resPr)):
    for j in range(len(resPr)):
        row.append(resPr[j])     
    column.append(row)
    row = []

def indexMap(hrz, vert):
  for x in range(len(resI)):
    hrz.append(resI[x])
  for x in range(len(resPr)):
    vert[resPr[x]] = hrz
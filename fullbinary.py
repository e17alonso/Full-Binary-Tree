
class Node:

    def __init__(self, item):
        self.item = item
        self.leftChild = None
        self.rightChild = None

def isFullTree(root):
    if root is None:
        return True
    if root.leftChild is None and root.rightChild is None:
        return True

    if root.leftChild is not None and root.rightChild is not None:
        return (isFullTree(root.leftChild) and isFullTree(root.rightChild))

    return False


root = Node(1)
root.rightChild = Node(3)
root.leftChild = Node(2)

if isFullTree(root):
    print("El arbol es un full binary tree")
else:
    print("El arbol no es un full binary tree")

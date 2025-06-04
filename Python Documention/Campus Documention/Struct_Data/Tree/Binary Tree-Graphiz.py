import graphviz as gv
from IPython.display import Image

class Node:
    def __init__(self, data):
        self.data   = data
        self.parent = None
        self.left   = None  # Left child node
        self.right  = None  # Right child node

class BinaryTree:
    def __init__(self):
        self.root = None  # Root node of the tree

    def insert(self,data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            print(f"{new_node.data}: ditempatkan sebagai ROOT")
            return
        else:
            currentNode = self.root
            while True:
                # Left-to-Right
                if data < currentNode.data:
                    if currentNode.left is None:
                        currentNode.left = new_node
                        currentNode.left.parent = currentNode
                        print(f"{new_node.data}: ditempatkan sebagai LEFT {currentNode.data}")
                        return
                    currentNode = currentNode.left
                else:
                    if currentNode.right is None:
                        currentNode.right = new_node
                        currentNode.right.parent = currentNode
                        print(f"{new_node.data}: ditempatkan sebagai RIGHT {currentNode.data}")
                        return
                    currentNode = currentNode.right
                    
    def inOrderTrav(self, trav):
        if trav:
            self.inOrderTrav(trav.left)
            print(trav.data, end = ' | ')
            self.inOrderTrav(trav.right)
        
    def deleteNode(self, travCell, hapus, deleteCell):
        if deleteCell is None:
            if travCell:
                if travCell.data == hapus:
                    self.deleteNode(travCell, hapus, travCell)
                    return True
                if self.deleteNode(travCell.left, hapus, None):
                    return True
                if self.deleteNode(travCell.right, hapus, None):
                    return True
            else:
                return False
        else:
            if deleteCell.right is None:
                if deleteCell.parent is None:
                    self.root =  deleteCell.left
                else:
                    if deleteCell.parent.left == deleteCell:
                        deleteCell.parent.left = deleteCell.left
                    elif deleteCell.parent.right == deleteCell:
                        deleteCell.parent.right = deleteCell.left
            elif deleteCell.left is None:
                if deleteCell.parent is None:
                    self.root = deleteCell.right
                else:
                    if deleteCell.parent.left == deleteCell:
                        deleteCell.parent.left = deleteCell.right
                    elif deleteCell.parent.right == deleteCell:
                        deleteCell.parent.right = deleteCell.right
            else:
                if deleteCell.parent.left == deleteCell:
                    deleteCell.parent.left = deleteCell.left
                else:
                    deleteCell.parent.right = deleteCell.left
                travCell = deleteCell.left
                travCell.parent = deleteCell.parent
                while travCell.right:
                    travCell = travCell.right
                travCell.right = deleteCell.right
                travCell.right.parent = travCell
                
    def visualize_tree(self, root, name):
        if root is None:
            return
        
        graph = gv.Digraph(format='png')
        
        def add_node(node):
            if node:
                graph.node(str(node.data), label=str(node.data))
                add_node(node.left)
                add_node(node.rigt)
                
        def add_edges(node):
            if node:
                if node.left:
                    graph.edge(str(node.data), str(node.left.data))
                if node.right:
                    graph.edge(str(node.data), str(node.right.data))
                add_edges(node.left)
                add_edges(node.right)
        add_node(root)
        add_edges(root)
        graph.render('binary tree', view = True)
                    
btree = BinaryTree()

btree.insert(35)
btree.insert(25)
btree.insert(40)
btree.insert(15)
btree.insert(30)
btree.insert(36)
btree.insert(45)
btree.insert(10)
btree.insert(20)
btree.insert(27)
btree.insert(32)
btree.insert(42)
btree.insert(18)
btree.insert(29)

#btree.insert("T")
#btree.insert("E")
#btree.insert("Y")
#btree.insert("A")
#btree.insert("M")
#btree.insert("U")
#btree.insert("D")
#btree.insert("I")
#btree.insert("S")

print('In-order-traversal before delete : ')
btree.inOrderTrav(btree.root)
print()
if btree.deleteNode(btree.root, 25, None):
    print('In-order-traversal after delete : ')
    btree.inOrderTrav(btree.root)
else:
    print('Node not find')
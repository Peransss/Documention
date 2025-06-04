class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class Tree:
    def __init__(self):
        self.root = None
        
    def isEmpty(self):
        return self.root is None
    
    def Insert(self, data):
        smp = Node(data)
        if self.isEmpty():
            self.root = smp
        else:
            self.InsertRecursive(self.root, data)
            
    def InsertRecursive(self, current, data):
        smp = Node(data)
        if data < current.data:
            if current.left is None:
                current.left = smp
            else:
                self.InsertRecursive(current.left, data)
        else:
            if current.right is None:
                current.right = smp
            else:
                self.InsertRecursive(current.right, data)
                
    def inorder(self):
        self._inorder_recursive(self.root)

    def _inorder_recursive(self, node):
        if node:
            self._inorder_recursive(node.left)
            print(node.data, end=" ")
            self._inorder_recursive(node.right)
            
    def preorder(self):
        self._preorder_recursive(self.root)
        
    def _preorder_recursive(self, node):
        if node:
            print(node.data, end = ' ')
            self._preorder_recursive(node.left)
            self._preorder_recursive(node.right)
            
    def postorder(self):
        self._postorder_recursive(self.root)
        
    def _postorder_recursive(self, node):
        if node:
            self._preorder_recursive(node.left)
            self._preorder_recursive(node.right)
            print(node.data, end = ' ')
                    
tree = Tree()
tree.Insert(50)
tree.Insert(30)
tree.Insert(5)
tree.Insert(15)

tree.inorder()
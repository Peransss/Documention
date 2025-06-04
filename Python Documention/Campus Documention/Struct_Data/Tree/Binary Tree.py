class Node:
    def __init__(self, data):
        self.data   = data
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
                        print(f"{new_node.data}: ditempatkan sebagai LEFT {currentNode.data}")
                        return
                    currentNode = currentNode.left
                else:
                    if currentNode.right is None:
                        currentNode.right = new_node
                        print(f"{new_node.data}: ditempatkan sebagai RIGHT {currentNode.data}")
                        return
                    currentNode = currentNode.right
                    
    def binarySearch(self, trav, cari):
        if trav:
            if trav.data == cari:
                return True
            if self.binarySearch(trav.left, cari):
                return True
            if self.binarySearch(trav.right, cari):
                return True
        else:
            return False
        
    def rightMost(self, node):
        while node.right:
            node = node.right
        return node
    
    def leftMost(self, node):
        while node.left:
            node = node.left
        return node
    
    def findPred_Suc(self, ptr, key):
        pre, suc = None, None
        while ptr:
            if ptr.data < key:
                pre = ptr.data
                ptr = ptr.right
            elif ptr.data > key:
                suc = ptr.data
                ptr = ptr.left
            else:
                if ptr.left:
                    pre = self.rightMost(ptr.left).data
                if ptr.right:
                    suc = self.leftMost(ptr.right).data
                break
        return pre, suc
    
    def deleteNodeM(self, travCell, hapus, deleteCell):
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
                
    def deleteNodeC(self, travCell, hapus):
        if travCell:
            if hapus < travCell.data:
                travCell.left = self.deleteNodeC(travCell.left, hapus)
            elif hapus > travCell.data:
                travCell.right = self.deleteNodeC(travCell.right, hapus)
            else:
                if travCell.left is None:
                    temp = travCell.right
                    travCell = None
                    return temp
                elif travCell.right is None:
                    temp = travCell.left
                    travCell = None
                    return temp
            temp = self.leftMost(travCell.right)
            # Copy Node
            travCell.data = temp.data
            travCell.right = self.deleteNodeC(travCell.right, temp.data)
        return travCell
                    
btree = BinaryTree()

#btree.insert(50)
#btree.insert(30)
#btree.insert(20)
#btree.insert(40)
#btree.insert(70)
#btree.insert(60)
#btree.insert(80)

btree.insert("T")
btree.insert("E")
btree.insert("Y")
btree.insert("A")
btree.insert("M")
btree.insert("U")
btree.insert("D")
btree.insert("I")
btree.insert("S")

search = 'M'
pre, suc = btree.findPred_Suc(btree.root, search)
print('Pre : ', pre)
print('Suc : ', suc)
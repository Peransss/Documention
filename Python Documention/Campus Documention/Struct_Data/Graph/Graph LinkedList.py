class Node:
    def __init__(self, vert):
        self.vert = vert
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def add(self, vert):
        smp = Node(vert)
        ptr = self.head
        if self.head is None:
            self.head = smp
        else:
            while ptr.next:
                ptr = ptr.next
            ptr.next = smp
    
    def remove(self, vert):
        ptr = self.head
        prev = None
        while ptr:
            if ptr.vert == vert:
                if prev is None:
                    self.head = ptr.next
                else:
                    prev.next = ptr.next
                return True
            prev =  ptr
            ptr = ptr.next
        return False
    
    def display(self):
        temp = self.head
        while temp:
            print(f' -> {temp.vert}', end = ' ')
            temp = temp.next
            
class Graph:
    def __init__(self, vert):
        self.vert = vert
        self.adj_list = [LinkedList() for _ in range(self.vert)]
    
    def add_edge(self, start, end):
        self.adj_list[start].add(end)
        
    def remove_edge(self, start, end):
        if self.adj_list[start].remove(end):
            print(f'Edge from {start} to {end} deleted successfully!')
        else:
            print(f'Edge from {start} to {end} is not found!')
            
    def display_graph(self):
        for i in range(self.vert):
            print(f'[{i}]', end = ' ')
            self.adj_list[i].display()
            print()
            
graph = Graph(4)

graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(0, 3)
graph.add_edge(1, 2)
graph.add_edge(2, 3)

graph.display_graph()

print()
graph.remove_edge(0, 2)
graph.remove_edge(0, 3)
graph.display_graph()
class Graph:
    def __init__(self, vert):
        self.vert = vert
        self.adj_mat = []
        for _ in range(vert):
            row = [0] * vert
            self.adj_mat.append(row)
            
    def add_edge(self, start, end):
        if (0 <= start < self.vert) and (0 <= end < self.vert):
            self.adj_mat[start][end] = 1
        else:
            print('Error : Invalid Vertices!')
            
    def remove_edge(self, start, end):
        if (0 <= start < self.vert) and (0 <= end < self.vert):
            self.adj_mat[start][end] = 0
        else:
            print('Error : Invalid Vertices!')
            
    def display(self):
        print('\nAdjacency Matrix')
        print(f'V |', end = ' ')
        for i in range(self.vert):
            print(i, end = ' ')
        print('\n-----------')
        for i in range(self.vert):
            print(f'{i}', end = ' | ')
            for j in range(self.vert):
                print(self.adj_mat[i][j], end = ' ')
            print()

graph = Graph(4)

graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(0, 3)
graph.add_edge(1, 2)
graph.add_edge(2, 3)

graph.display()

graph.remove_edge(0, 2)
graph.display()
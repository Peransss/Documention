x = [[1, 3, 4],
     [7, 13, 5],
     [15, 2, 5],
     [6, 8, 4]]

y = []

for i in range(len(x[0])):
    b = []
    for j in range(len(x)):
        b.append(x[j][i])
    y.append(b) 
    
print(y)
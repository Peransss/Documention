array_2d = [[2, 4, 6],
            [1, 3, 5],
            [7, 8, 9]]

n = [0, 0, 0]

for i in array_2d:
    for j in range(len(i)):
        n[j] += i[j]
        
print(n)
        
                
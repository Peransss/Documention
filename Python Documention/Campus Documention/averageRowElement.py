array_2d = [[10, 20, 30],
            [40, 50, 60],
            [70, 80, 90]]

n = []

for i in array_2d:
    n1 = sum(i) / len(i)
    n.append(n1)
        
print(n)
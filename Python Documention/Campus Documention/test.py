a = [1, 2, 3, 4, 5]
b = [1, 2, 3]
c = b[:]
for i in a:
    if i not in c:
        c.append(i)
        
print(c)
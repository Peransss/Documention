a = [1, 2, 3, 4, 5]
b = [1, 2, 3]
c = []

for i in a:
    for j in range(len(i)):
        if a[j] == b[j]:
            c.append(a[j])

print(c)





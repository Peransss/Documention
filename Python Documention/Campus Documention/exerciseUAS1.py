arr = [3, 2, 1, 56, 10000, 167]
n = len(arr)

min = arr[0]
max = arr[5]

for i in range(n):
    if arr[i] < min:
        min = arr[i]
    elif arr[i] > max:
        max = arr[i]
        
print(f'Min : {min}')
print(f'Max : {max}')  
              
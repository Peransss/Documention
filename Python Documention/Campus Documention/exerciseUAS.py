def num1():
    arr = [1, 3, 5, 9]

    for i in range(len(arr)):
        print(arr[i])
        if i == 2:
            break

print("Number 1")
num1()

def num2():
    arr = ['i', [1, 3, 5, 9]]
    arr1 = arr[1]
    arr1.append(11)
    print(arr)
    
print("\nNumber 2")
num2()

def num3():
    arr = ['i', [1, 3, 5, 3, 7, 1, 9, 3]]
    arr1 = arr[1]
    n = len(arr1)
    temp = [0] * n
    for i in range(n):
        temp[i] = arr1[n - i - 1]
        
    for b in range(n):
        arr1[b] = temp[b]
        
    print(arr1)
                    
print("\nNumber 3")
num3()

def num6():
    arr = ['i', [1, 3, 5, 3, 7, 9, 3]]
    arr1 = arr[1]
    
    n = int(input("Num : "))
    exm = 0
    
    for i in range(len(arr1)):
        if arr1[i] == n:
            exm += 1
    print(f'Many of Num {n} : {exm}')
         
print("\nNumber 6")
num6()

def num9():
    arr = ['i']
    arr1 = [1, 2, 6, -8]
    arr.append(arr1)
    print(arr)
    
print("\nNumber 9")
num9()
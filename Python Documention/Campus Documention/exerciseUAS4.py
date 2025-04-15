def num1():
    for i in range(5):
        for j in range(i + 1):
            print(j + 1, end = " ")
        print()
        
print("Number 1")
num1()

def num2():
    n = int(input("Batas : "))
    j = 0
    for i in range(1, n + 1):
        j += i
    print(j)
    
print("\nNumber 2")
num2()

def num3():
    num = 2
    for i in range(1, 11):
        j = num * i
        print(j)
        
print("\nNumber 3")
num3()

def num4():
    numbers = [12, 75, 150, 180, 145, 525, 50]
    for i in numbers:
        if i % 5 == 0:
            if i > 150:
                False
            else:
                print(i)
                
            if i > 500:
                break
            
print("\nNumber 4")            
num4()

def num5():
    n = int(input("Numbers : "))
    counter = 0
    while n != 0:    
        n = n // 10
        counter += 1
    print(counter)
    
print("\nNumber 5")
num5()     

def num6():
    k = 5
    for i in range(5):
        for j in range(k - i, 0, -1):
            print(j, end = " ")
        print()
        
print("\nNumber 6")
num6()

def num7():
    list1 = [10, 20, 30, 40, 50]
    n = len(list1)
    for i in range(1, n + 1):
        print(list1[-i])
        
print("\nNumber 7")
num7()

def num8():
    import math as m
    n = int(input("Max : "))
    while n > 1:
        i = 2
        j = 1
        a = m.pow(i, j) - 1
        if a % i != 0 :
            print(i)
        i += 1
        j += 1
        
        
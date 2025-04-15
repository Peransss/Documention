def num1():
    angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for i in angka:
        if i % 2 == 0:
            print(i)
            
print("Number 1")
num1()

def num2():
    for i in range(121, 126):
        luas = i * i
        print(f'Luas : {luas}')
        
print("\nNumber 2")
num2()

def num3():
    import math as a
    for i in range(100_000, 200_001):
        if a.sqrt(i) % 2 == 0:
            print(i)
            break                        
print("\nNumber 3")
num3()    

        
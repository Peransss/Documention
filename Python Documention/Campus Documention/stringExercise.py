IsMart = ['Laptop', 
          'Smartphone', 
          'Tablet', 
          'Smartwatch', 
          'Handphone', 
          'Kamera', 
          'Keyboard', 
          'Mouse', 
          'Printer', 
          'Monitor', 
          'Speaker']

#Nomor 1
print("Nomor 1")
d = str(IsMart)
print(d.lower())

#Nomor 2
print("\nNomor 2")
print('Total Produk : ', len(IsMart))

#Nomor 3
print("\nNomor 3")
n = input("Produk : ")
if n in IsMart:
    print(f"Produk {n} Terdapat pada IsMart")
        
#Nomor 4
print("\nNomor 4")
b = input("Produk : ")
for j in IsMart:
    if j[0] == b:
        print(j)
        
#Nomor 5
print("\nNomor 5")
x = ", ".join(IsMart)
print(x)


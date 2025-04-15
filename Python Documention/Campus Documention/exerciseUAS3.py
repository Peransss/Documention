bil = []
i = 0

while True:
    i += 1
    data = {}
    print(f'Data ke {i}')
    data["X"] = int(input("X \t: "))
    data["Y"] = int(input("Y \t: "))
    data["Jumlah"] = data["X"] + data["Y"]
    print(f'Jumlah \t: {data["Jumlah"]}')
    bil.append(data)
        
    a = input("\nApakah input lagi? [Y/N] : ")
    
    print()
    
    if a == "Y":
        continue
    elif a == "N":
        break
    
print("NO", "X", "Y", "Jumlah", sep = "\t| ", end = "\n----------------------------------\n")
for i in range(len(bil)):
    print(i + 1, bil[i]["X"], bil[i]["Y"], bil[i]["Jumlah"], sep = "\t| ", end ="\n")
    
    
    
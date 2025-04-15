Hari = int(input("Hari : "))    
match Hari:
    case 1:
        hari = "Senin"
    case 2:
        hari = "Selasa"
    case 3:
        hari = "Rabu"
    case 4:
        hari = "Kamis"
    case 5:
        hari = "Jumat"
    case 6:
        hari = "Sabtu"
    case 7:
        hari = "Minggu"
        
dataAkhir = []

while True:
    data = {}
    data["Usia"] = input("Dewasa/Kecil : ")
    data["Jumlah Tiket"] = int(input("Jumlah Tiket : "))
    
    if Hari == 6 or Hari == 7:
        if data["Usia"] == "Dewasa":
            data["Harga"] = 100_000
        else:
            data["Harga"] = 75_000
    else:
        if data["Usia"] == "Dewasa":
            data["Harga"] = 80_000
        else:
            data["Harga"] = 50_000
            
    data["Total Harga"] = data["Jumlah Tiket"] * data["Harga"]
    dataAkhir.append(data)
    
    n = input("Apakah ingin menambahkan lagi(Y/N)? : ")
    
    if n == "Y":
        continue
    else:
        break
    
print()    
print("Usia", "Tiket", "Harga", "Total Harga", sep = '\t|', end = "\n-------------------------------------\n")
for i in range(len(dataAkhir)):
    print(dataAkhir[i]["Usia"], dataAkhir[i]["Jumlah Tiket"], dataAkhir[i]["Harga"], dataAkhir[i]["Total Harga"], sep = '\t|', end = "\n")

total = 0
for j in range(len(dataAkhir)):
    total += dataAkhir[j]["Total Harga"]
    
print(f'Total Bayar : {total}')
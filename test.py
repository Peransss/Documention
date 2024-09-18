NIM = int(input("NIM : "))
Nama = input("Nama : ")
Tugas = float(input("Tugas : "))
UTS = float(input("UTS : "))
UAS = float(input("UAS : "))
NA : float

def NilaiAkhir():
    NA = ((30/100*Tugas) + (30/100*UTS) + (40/100*UAS))
    return NA

print("Nama :", Nama, "\nNIM :", NIM, "\nNilaiAkhir :", NilaiAkhir())
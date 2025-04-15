import csv

def baca_data():
    with open("dataMHS.csv", "r") as data:
        baca = data.read()
    baris = baca.splitlines()
    for baris_data in baris:
        kolom = baris_data.split(',')
        nama = kolom[0]
        jurusan = kolom[1]
        ipk = kolom[2]
        print(f'Nama : {nama}, Jurusan : {jurusan}, IPK : {ipk}')
baca_data()
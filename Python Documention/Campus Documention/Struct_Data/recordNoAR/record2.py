dataTugas = {
    'Tugas' : ' ',
    'UTS' : ' ',
    'UAS' : ' ',
    'NA' : ' '
}

Mhs1 = []
i = 0

while True:
    i += 1
    dataMHS = {}
    
    print(f'Mahasiswa {i}')
    dataMHS['Nama'] = input('Nama : ')
    dataMHS['Kelas'] = input('Kelas : ')
    
    dataTugas['Tugas'] = int(input('Tugas : '))
    dataTugas['UTS'] = int(input('UTS : '))
    dataTugas['UAS'] = int(input('UAS : '))
    dataTugas['NA'] = (dataTugas['Tugas'] * 0.3) + (dataTugas['UTS'] * 0.3) + (dataTugas['UAS'] * 0.4)
    
    dataMHS['Nilai Akhir'] = dataTugas
    
    Mhs1.append(dataMHS)
    
    a = input('Apakah input lagi? [Y/N] : ')
    
    print()
    
    if a == 'Y':
        continue
    elif a == 'N':
        break
    
print('NO', 'Nama', 'Kelas', 'Nilai Akhir', sep = '\t| ', end = '\n----------------------------------\n')
for i in range(len(Mhs1)):
    print(i + 1, Mhs1[i]['Nama'], Mhs1[i]['Kelas'], Mhs1[i]['Nilai Akhir']['NA'], sep = '\t| ', end = '\n')
    
    
    
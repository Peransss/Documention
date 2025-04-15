Mhs1 = []

Mhs = {
    'Nama' : ' ',
    'NIM' : ' ',
    'IPK' : ' '
}

for i in range(5):
    print(f'Mahasiwa {i + 1}')
    Mhs['Nama'] = input('Nama : ')
    Mhs['NIM'] = input('Kelas : ')
    Mhs['IPK'] = float(input('IPK : '))
    Mhs2 = {
        'Nama' : Mhs['Nama'],
        'NIM' : Mhs['NIM'],
        'IPK' : Mhs['IPK']
    }
    Mhs1.append(Mhs2)
    
print('NO', 'Nama', 'Kelas', 'NIM', sep = '\t| ', end = "\n----------------------------------\n")
for a in range(5):
    print(a + 1, Mhs1[a]['Nama'], Mhs1[a]['Kelas'], Mhs1[a]['NIM'], sep = '\t| ', end = '\n')
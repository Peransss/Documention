luas = [[225 * 335, 229 * 278, 300 * 250],
        [215 * 394, 144 * 718, 300 * 290],
        [200 * 400, 240 * 333, 142 * 619],
        [314 * 295, 411 * 195, 333 * 222]]

harga_jual = [100, 120, 150]
luas_hasil_trans = []
hasil_akhir = []
total = []

for i in range(len(luas[0])):
    luas_trans = []
    for j in range(len(luas)):
        luas_trans.append(luas[j][i])
    luas_hasil_trans.append(luas_trans)
    
for a in luas_hasil_trans:
    total_hasil = sum(a)
    total.append(total_hasil)
    
for b in range(len(harga_jual)):
    hasil_akhir = total[b] * harga_jual[b]
    print(f'Harga Total Merk {b + 1} : Rp.{hasil_akhir}')

    
    
    
    
        
        
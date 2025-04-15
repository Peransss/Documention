import Tugas_5_Kelas3 as cs

def status_kerja_pegawai_harian(id, nama, status_kerja, jenis_kelamin, status_menikah, jml_anak, gapok, uang_per_hari):    
    return cs.Pegawaiharian(id, nama, status_kerja, jenis_kelamin, status_menikah, jml_anak, gapok, uang_per_hari)

def status_kerja_pegawai_kontrak(id, nama, status_kerja, jenis_kelamin, status_menikah, jml_anak, gapok, uang_prestasi):    
    return cs.PegawaiKontrak(id, nama, status_kerja, jenis_kelamin, status_menikah, jml_anak, gapok, uang_prestasi)

def status_kerja_pegawai_tetap(id, nama, status_kerja, jenis_kelamin, status_menikah, jml_anak, gapok, lama_lembur, biaya_lembur_per_jam):    
    return cs.Pegawai_tetap(id, nama, status_kerja, jenis_kelamin, status_menikah, jml_anak, gapok, lama_lembur, biaya_lembur_per_jam)
   
def info_pendapatan(Pegawai):  
    if isinstance(Pegawai, cs.Pegawai_tetap):
        print(f'Tunjangan : Rp {Pegawai.tunjangan()}')
        print(f'Bonus : Rp {Pegawai.bonus()}')
        print(f'THR : Rp {Pegawai.thr()}')
        
        if Pegawai.tun_istri():
            print(f'Tunjangan Istri : {Pegawai.tun_istri()}')    
            
        if Pegawai.tun_anak():
            print(f'Tunjangan Anak : {Pegawai.tun_anak()}')
                
        print(f'Uang Lembur : {Pegawai.uang_lembur()}')    
        print(f'Total Gaji : {Pegawai.total_gaji()}')
        
    elif isinstance(Pegawai, cs.PegawaiKontrak):
        print(f'Tunjangan : Rp {Pegawai.tunjangan()}')
        print(f'Bonus : Rp {Pegawai.bonus()}')            
        print(f'Total Gaji : {Pegawai.total_gaji()}')    
        
    else:
        print(f'Total Gaji : {Pegawai.total_gaji()}')    

def main():
    print('=' * 33)
    print('\tData Diri Pegawai\t')
    print('=' * 33)

    id = input('ID : ')
    nama = input('Nama : ')
    status_kerja = input('Status Kerja [T/K/H] : ')
    jenis_kelamin = input('Jenis Kelamin [L/P] : ')
    status_menikah = input('Status Menikah [M/B] : ')
    jml_anak = int(input('Jumlah anak : '))
    gapok = int(input('Gaji : '))

    if status_kerja == 'T':
        lama_lembur = int(input('Lama Lembur : '))
        biaya_lembur_per_jam = int(input('Biaya Lembur Per Jam : '))
        Pegawai = status_kerja_pegawai_tetap(id, nama, status_kerja, jenis_kelamin, status_menikah, jml_anak, gapok, lama_lembur, biaya_lembur_per_jam)
    elif status_kerja == 'K':
        uang_prestasi = int(input('Uang Prestasi : '))
        Pegawai = status_kerja_pegawai_kontrak(id, nama, status_kerja, jenis_kelamin, status_menikah, jml_anak, gapok, uang_prestasi)
    elif status_kerja == 'H':
        uang_per_hari = int(input('Uang Per Hari : '))
        Pegawai =  status_kerja_pegawai_harian(id, nama, status_kerja, jenis_kelamin, status_menikah, jml_anak, gapok, uang_per_hari)
 
    print('=' * 33)
    print(f'\tPendapatan Pegawai {status_kerja}\t')
    print('=' * 33)
    
    info_pendapatan(Pegawai)

if __name__ =='__main__':
    main()
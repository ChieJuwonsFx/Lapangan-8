import admfunc as ad 
from datetime import datetime
import os

def menu():
    os.system('cls')
    print("\n" + "+" + "-"*50 + "+")
    print("|{:^50}|".format("MENU"))
    print("+" + "-"*50 + "+")
    print("|{:<50}|".format("1. Data Customer"))
    print("|{:<50}|".format("2. Data Karyawan"))
    print("|{:<50}|".format("3. Data Lapangan"))
    print("|{:<50}|".format("4. Data Jenis Lapangan"))
    print("|{:<50}|".format("5. Data Alat")) 
    print("|{:<50}|".format("6. Data Jam Shift"))     
    print("|{:<50}|".format("7. Data Metode Pembayaran")) 
    print("|{:<50}|".format("8. Data Revervasi")) 
    print("|{:<50}|".format("9. Konfirmasi Pembayaran"))
    print("|{:<50}|".format("10. Data Pengembalian"))
    print("|{:<50}|".format("11. Data Jadwal Shift Karyawan"))      
    print("|{:<50}|".format("12. Keluar"))           
    print("+" + "-"*50 + "+")

def mainadm():
    while True:
        os.system('cls')
        print("+" + "-"*50 + "+")
        print("|{:^50}|".format("Silahkan Login Min!!!"))
        print("+" + "-"*50 + "+")
        username = input('Masukkan username: ')
        password = input('Masukkan password: ')
        karyawan = ad.login_karyawan(username, password)
        if karyawan:
            os.system('cls')
            print('Login berhasil!')
            print("+" + "-"*50 + "+")            
            print("|{:^50}|".format("Login berhasil!"))
            print(f'Selamat datang, {karyawan["nama_karyawan"]}')
            print("+" + "-"*50 + "+")
            while True:
                menu()
                pilihan2 = input('Pilih menu: ')
                if pilihan2 == '1':
                    os.system('cls')
                    print("+" + "-"*50 + "+")
                    print("|{:^50}|".format("Data Customer"))
                    print("+" + "-"*50 + "+")
                    ad.display_customer()

                    print("+" + "-"*50 + "+")
                    print("|{:<50}|".format("1. Kembali"))
                    print("|{:<50}|".format("2. Keluar"))
                    print("+" + "-"*50 + "+")
                    pilihan = input('Pilih menu: ')
                    if pilihan == '1':
                        os.system('cls')
                        menu()
                    else:
                        break
                elif pilihan2 == '2':
                    os.system('cls')
                    print("+" + "-"*50 + "+")
                    print("|{:^50}|".format("Data Karyawan"))
                    print("+" + "-"*50 + "+")
                    ad.display_karyawan()

                    print("+" + "-"*50 + "+")
                    print("|{:<50}|".format("1. Tambah Karyawan"))
                    print("|{:<50}|".format("2. Update Karyawan"))
                    print("|{:<50}|".format("3. Hapus Karyawan"))
                    print("|{:<50}|".format("4. Kembali"))
                    print("|{:<50}|".format("5. Keluar"))
                    print("+" + "-"*50 + "+")
                    pilihan = input('Pilih menu: ')
                    if pilihan == '1':
                        os.system('cls')
                        nama = input("Masukkan nama karyawan: ")
                        no_telp = input("Masukkan nomor telepon karyawan: ")
                        alamat = input("Masukkan alamat karyawan: ")
                        desa = input("Masukkan desa karyawan: ")
                        kecamatan = input("Masukkan kecamatan karyawan: ")
                        kabupaten = input("Masukkan kabupaten karyawan: ")
                        username = input("Masukkan username karyawan: ")
                        password = input("Masukkan password karyawan: ")
                        ad.create_karyawan(nama, alamat, no_telp, desa, kecamatan, kabupaten, username, password)
                    elif pilihan == '2':
                        os.system('cls')
                        ad.display_karyawan()
                        id_karyawan = int(input("Masukkan ID karyawan yang akan diperbarui: "))
                        nama = input("Masukkan nama: ")
                        no_telp = input("Masukkan nomor telepon: ")
                        alamat = input("Masukkan alamat: ")
                        desa = input("Masukkan desa: ")
                        kecamatan = input("Masukkan kecamatan: ")
                        kabupaten = input("Masukkan kabupaten: ")
                        username = input("Masukkan username: ")
                        password = input("Masukkan password: ")
                        is_active = bool(input("Masukkan status karyawan (kosongi jika tidak aktif): "))
                        ad.update_karyawan(id_karyawan, nama, alamat, no_telp, desa, kecamatan, kabupaten, username, password, is_active)
                    elif pilihan == '3':
                        os.system('cls')
                        ad.display_karyawan()
                        id_karyawan = int(input("Masukkan ID karyawan yang ingin dihapus: "))
                        ad.delete_karyawan(id_karyawan)
                    elif pilihan == '4':
                        os.system('cls')
                        menu()
                    else:
                        break
                elif pilihan2 == '3':
                    os.system('cls')
                    print("+" + "-"*50 + "+")
                    print("|{:^50}|".format("Data Lapangan"))
                    print("+" + "-"*50 + "+")
                    ad.display_lapangan()

                    print("+" + "-"*50 + "+")  
                    print("|{:<50}|".format("1. Tambah Lapangan"))
                    print("|{:<50}|".format("2. Update Lapangan"))
                    print("|{:<50}|".format("3. Kembali"))
                    print("|{:<50}|".format("4. Keluar"))
                    print("+" + "-"*50 + "+")
                    pilihan = input('Pilih menu: ')
                    if pilihan == '1':
                        os.system('cls')
                        nomor_lapangan = int(input("Masukkan nomor lapangan: "))
                        kondisi_lapangan = input("Masukkan kondisi lapangan (Baik/Sedang/Rusak): ")
                        ad.display_jenis_lapangan()
                        jenis_lapangan_id = int(input("Masukkan ID jenis lapangan: "))
                        ad.create_lapangan(nomor_lapangan, kondisi_lapangan, jenis_lapangan_id)
                    elif pilihan == '2':
                        os.system('cls')
                        ad.display_lapangan()
                        nomor_lapangan = int(input("Masukkan nomor lapangan yang akan diperbarui: "))
                        kondisi_lapangan = input("Masukkan kondisi lapangan (Baik/Sedang/Rusak): ")
                        ad.display_jenis_lapangan()
                        jenis_lapangan_id = int(input("Masukkan ID jenis: "))
                        ad.update_lapangan(nomor_lapangan, kondisi_lapangan, jenis_lapangan_id)
                    elif pilihan == '3':
                        os.system('cls')
                        menu()
                    elif pilihan == '4':
                        break                    
                elif pilihan2 == '4':
                    os.system('cls')
                    print("+" + "-"*50 + "+")
                    print("|{:^50}|".format("Data Jenis Lapangan"))
                    print("+" + "-"*50 + "+")
                    print("+" + "-"*50 + "+")
                    ad.display_jenis_lapangan()

                    print("+" + "-"*50 + "+")  
                    print("|{:<50}|".format("1. Tambah Jenis Lapangan"))
                    print("|{:<50}|".format("2. Update Jenis Lapangan"))
                    print("|{:<50}|".format("3. Kembali"))
                    print("|{:<50}|".format("4. Keluar"))
                    print("+" + "-"*50 + "+")
                    pilihan = input('Pilih menu: ')
                    if pilihan == '1':
                        os.system('cls')
                        jenis_lapangan = input("Masukkan jenis lapangan: ")
                        deskripsi_lapangan = input("Masukkan deskripsi lapangan: ")
                        harga_sewa_lapangan = input("Masukkan harga sewa lapangan: ")
                        ad.create_jenis_lapangan(jenis_lapangan, deskripsi_lapangan, harga_sewa_lapangan)
                    elif pilihan == '2':
                        os.system('cls')
                        ad.display_jenis_lapangan()
                        id_jenis_lapangan = int(input("Masukkan ID jenis lapangan yang akan diperbarui: "))
                        jenis_lapangan = input("Masukkan jenis: ")
                        deskripsi_lapangan = input("Masukkan deskripsi: ")
                        harga_sewa_lapangan = input("Masukkan harga sewa: ")
                        ad.update_jenis_lapangan(id_jenis_lapangan, jenis_lapangan, deskripsi_lapangan, harga_sewa_lapangan)
                    elif pilihan == '3':
                        os.system('cls')
                        menu()
                    elif pilihan == '4':
                        break
                elif pilihan2 == '5':
                    os.system('cls')
                    print("+" + "-"*50 + "+")
                    print("|{:^50}|".format("Data Alat"))
                    print("+" + "-"*50 + "+")
                    ad.display_alat()

                    print("+" + "-"*50 + "+")  
                    print("|{:<50}|".format("1. Tambah Alat"))
                    print("|{:<50}|".format("2. Update Alat"))
                    print("|{:<50}|".format("3. Kembali"))
                    print("|{:<50}|".format("4. Keluar"))
                    print("+" + "-"*50 + "+")
                    pilihan = input('Pilih menu: ')
                    if pilihan == '1':
                        os.system('cls')
                        jenis_alat = input("Masukkan jenis alat: ")
                        jumlah_alat = input("Masukkan jumlah alat: ")
                        harga_sewa_alat = input("Masukkan harga sewa alat: ")
                        ad.create_alat_olahraga(jenis_alat, jumlah_alat, harga_sewa_alat)
                    elif pilihan == '2':
                        os.system('cls')
                        ad.display_alat()
                        id_alat = int(input("Masukkan ID alat yang akan diperbarui: "))
                        jenis_alat = input("Masukkan jenis alat baru: ")
                        jumlah_alat = input("Masukkan jumlah alat baru: ")
                        harga_sewa_alat = input("Masukkan harga sewa alat baru: ")
                        ad.update_alat_olahraga(id_alat, jenis_alat, jumlah_alat, harga_sewa_alat)
                    elif pilihan == '3':
                        os.system('cls')
                        menu()
                    elif pilihan == '4':
                        break                                              
                elif pilihan2 == '6':
                    os.system('cls')
                    print("+" + "-"*50 + "+")
                    print("|{:^50}|".format("Data Jam Shift"))
                    print("+" + "-"*50 + "+")
                    ad.display_shift()

                    print("+" + "-"*50 + "+")  
                    print("|{:<50}|".format("1. Tambah Jam Shift"))
                    print("|{:<50}|".format("2. Update Jam Shift"))
                    print("|{:<50}|".format("3. Kembali"))
                    print("|{:<50}|".format("4. Keluar"))
                    print("+" + "-"*50 + "+")
                    pilihan = input('Pilih menu: ')
                    if pilihan == '1':
                        os.system('cls')
                        tanggal_berlaku = input("Masukkan tanggal berlaku (YYYY-MM-DD): ")
                        tanggal_berakhir = input("Masukkan tanggal berakhir (YYYY-MM-DD): ")
                        hari_shift = input("Masukkan hari shift: ")
                        jam_awal_shift = input("Masukkan jam awal shift (HH:MM:SS): ")
                        jam_akhir_shift = input("Masukkan jam akhir shift (HH:MM:SS): ")
                        ad.create_jadwal_shift(tanggal_berlaku, tanggal_berakhir, hari_shift, jam_awal_shift, jam_akhir_shift)
                    elif pilihan == '2':
                        os.system('cls')
                        ad.display_shift()
                        id_shift = int(input("Masukkan ID shift yang akan diperbarui: "))
                        tanggal_berlaku = input("Masukkan tanggal berlaku baru (YYYY-MM-DD): ")
                        tanggal_berakhir = input("Masukkan tanggal berakhir baru (YYYY-MM-DD): ")
                        hari_shift = input("Masukkan hari shift baru (dalam Bahasa Inggris): ")
                        jam_awal_shift = input("Masukkan jam awal shift baru (HH:MM:SS): ")
                        jam_akhir_shift = input("Masukkan jam akhir shift baru (HH:MM:SS): ")
                        ad.update_jadwal_shift(id_shift, tanggal_berlaku, tanggal_berakhir, hari_shift, jam_awal_shift, jam_akhir_shift)
                    elif pilihan == '3':
                        os.system('cls')
                        menu()
                    elif pilihan == '4':
                        break 
                elif pilihan2 == '7':
                    os.system('cls')
                    print("+" + "-"*50 + "+")
                    print("|{:^50}|".format("Data Metode Pembayaran"))
                    print("+" + "-"*50 + "+")
                    ad.display_metode()

                    print("+" + "-"*50 + "+")  
                    print("|{:<50}|".format("1. Tambah Metode"))
                    print("|{:<50}|".format("2. Update Metode"))
                    print("|{:<50}|".format("3. Kembali"))
                    print("|{:<50}|".format("4. Keluar"))
                    print("+" + "-"*50 + "+")
                    pilihan = input('Pilih menu: ')
                    if pilihan == '1':
                        os.system('cls')
                        nama_metode = input("Masukkan nama metode pembayaran: ")
                        no_rekening = input("Masukkan nomor rekening pengelola: ")
                        nama_pemilik = input("Masukkan nama pemilik: ")
                        ad.create_metode_pembayaran(nama_metode, no_rekening, nama_pemilik)
                    elif pilihan == '2':
                        os.system('cls')
                        ad.display_metode()
                        id_metode = int(input("Masukkan ID metode pembayaran yang akan diperbarui: "))
                        nama_metode = input("Masukkan nama metode pembayaran baru: ")
                        no_rekening = input("Masukkan nomor rekening pengelola baru: ")
                        nama_pemilik = input("Masukkan nama pemilik baru: ")
                        ad.update_metode_pembayaran(id_metode, nama_metode, no_rekening, nama_pemilik)
                    elif pilihan == '3':
                        os.system('cls')
                        menu()
                    elif pilihan == '4':
                        break                      
                elif pilihan2 == '8':
                    os.system('cls')
                    print("+" + "-"*50 + "+")
                    print("|{:^50}|".format("Data Revervasi"))
                    print("+" + "-"*50 + "+")
                    ad.display_reservasi()

                    print("+" + "-"*50 + "+")
                    print("|{:<50}|".format("1. Hapus Reservasi yang Dilakukan Sebelum Tanggal Tertentu"))
                    print("|{:<50}|".format("2. Kembali"))
                    print("|{:<50}|".format("3. Keluar"))
                    print("+" + "-"*50 + "+")
                    pilihan = input('Pilih menu: ')
                    if pilihan == "1":
                        os.system('cls')
                        ad.display_reservasi()
                        tanggal_batas = input("Masukkan tanggal batas reservasi yang ingin dihapus: ")
                        ad.delete_detail_reservasi_sebelum(tanggal_batas)
                    elif pilihan == '2':
                        os.system('cls')
                        menu()
                    else:
                        break                    
                elif pilihan2 == '9':
                    os.system('cls')
                    print("+" + "-"*50 + "+")
                    print("|{:^50}|".format("Konfirmasi Pembayaran"))
                    print("+" + "-"*50 + "+")
                    ad.display_detail_reservasi()

                    print("+" + "-"*50 + "+")  
                    print("|{:<50}|".format("1. Konfirmasi Pembayaran"))
                    print("|{:<50}|".format("2. Kembali"))
                    print("|{:<50}|".format("3. Keluar"))
                    print("+" + "-"*50 + "+")
                    pilihan = input('Pilih menu: ')
                    if pilihan == '1':
                        os.system('cls')
                        id_detail = int(input("Masukkan ID detail reservasi yang akan diperbarui: "))
                        status_pembayaran = input("Masukkan status pembayaran baru: ")
                        ad.update_status_pembayaran(id_detail, status_pembayaran)
                    elif pilihan == '2':
                        os.system('cls')
                        menu()
                    else:
                        break 
                elif pilihan2 == '10':
                    os.system('cls')
                    print("+" + "-"*50 + "+")
                    print("|{:^50}|".format("Data Pengembalian"))
                    print("+" + "-"*50 + "+")   
                    ad.display_pengembalian()

                    print("+" + "-"*50 + "+")  
                    print("|{:<50}|".format("1. Tambah Pengembalian"))
                    print("|{:<50}|".format("2. Kembali"))
                    print("|{:<50}|".format("3. Keluar"))
                    print("+" + "-"*50 + "+")
                    pilihan = input('Pilih menu: ')
                    if pilihan == '1':
                        os.system('cls')
                        tanggal_pengembalian = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        jumlah_alat_kembali = int(input("Masukkan jumlah alat yang dikembalikan: "))
                        os.system('cls')
                        ad.display_alat()
                        alat_olahraga_id = int(input("Masukkan ID alat olahraga: "))
                        os.system('cls')
                        ad.display_detail_reservasi()
                        reservasi_id = int(input("Masukkan ID reservasi: "))
                        ad.create_pengembalian_alat(tanggal_pengembalian, jumlah_alat_kembali, alat_olahraga_id, reservasi_id)
                    elif pilihan == '2':
                        os.system('cls')
                        menu()
                    else:
                        break 
                elif pilihan2 == '11':
                    os.system('cls')
                    print("+" + "-"*50 + "+")
                    print("|{:^50}|".format("Data Jadwal Shift Karyawan"))
                    print("+" + "-"*50 + "+")
                    ad.display_detail_shift()

                    print("+" + "-"*50 + "+")  
                    print("|{:<50}|".format("1. Tambah Jadwal Shift"))
                    print("|{:<50}|".format("2. Update Jadwal Shift"))
                    print("|{:<50}|".format("3. Kembali"))
                    print("|{:<50}|".format("4. Keluar"))
                    print("+" + "-"*50 + "+")
                    pilihan = input('Pilih menu: ')
                    if pilihan == '1':
                        os.system('cls')
                        ad.display_karyawan()
                        karyawan_id = int(input("Masukkan ID karyawan: "))
                        os.system('cls')
                        ad.display_shift()
                        jadwal_shift_id = int(input("Masukkan ID jadwal shift: "))
                        ad.create_detail_shift(karyawan_id, jadwal_shift_id)
                    elif pilihan == '2':
                        ad.display_detail_shift()
                        karyawan_id = int(input("Masukkan ID jadwal shift yang akan diperbarui: "))
                        jadwal_shift_id = int(input("Masukkan ID karyawan baru: "))
                        ad.update_detail_shift(karyawan_id, jadwal_shift_id)
                    elif pilihan == '3':
                        menu()
                    elif pilihan == '4':
                        break   
                elif pilihan2 == '12':
                    os.system('cls')
                    break
                else:           
                    print("+" + "-"*50 + "+")
                    print("|{:^50}|".format("Pilih yang benar"))
                    print("+" + "-"*50 + "+")                        
        else:
            os.system('cls')
            print("+" + "-"*50 + "+")
            print("|{:^50}|".format("Login gagal. Silakan coba lagi."))
            print("+" + "-"*50 + "+")
            
mainadm()
import cusfunc as cs
from datetime import datetime, timedelta
import os
from tabulate import tabulate


def display_customer_data(name, alamat, kota, kecamatan, kabupaten, telp, email, username, hashed_password):
    data = [[name, alamat, kota, kecamatan, kabupaten, telp, email, username, hashed_password]]
    headers = ["Nama", "Alamat", "Kota", "Kecamatan", "Kabupaten", "No. Telp", "Email", "Username", "Password"]
    print(tabulate(data, headers=headers, tablefmt="grid"))

def display_lapangan(lap):
    headers = ["Nomor Lapangan", "Jenis Lapangan", "Deskripsi Lapangan", "Harga Sewa / jam "]
    data = [[lapangan["nomor_lapangan"], lapangan["jenis_lapangan"], lapangan["deskripsi_lapangan"], lapangan["harga_sewa_lapangan"]] for lapangan in lap]
    print(tabulate(data, headers=headers, tablefmt="grid"))

def display_alat(peralatan):
    peralatan = cs.alat()
    headers = ["ID", "Jenis Peralatan", "Stok", "Harga", "Jumlah"]
    data = [[alor["id_alat"], alor["jenis_alat"], alor["jumlah_alat"], alor["harga_sewa_alat"]] for alor in peralatan]
    print(tabulate(data, headers=headers, tablefmt="grid"))

def display_reservasi(tanggal_reservasi, tanggal_jadwal, jam_awal_waktu, jam_akhir_waktu):
    data = [[tanggal_reservasi, tanggal_jadwal, jam_awal_waktu, jam_akhir_waktu]]
    headers = ["Tanggal Reservasi", "Tanggal Jadwal", "Jama Awal", "Jam Akhir"]
    print(tabulate(data, headers=headers, tablefmt="grid"))

def int_to_time(jam):
    jame = str(jam).zfill(2) 
    str_jam = f"{jame}:00:00"
    return datetime.strptime(str_jam, "%H:%M:%S").time()

def register_process():
    while True:
        name = input('Masukkan nama: ')
        alamat = input('Masukkan alamat: ')
        desa = input('Masukkan desa: ')
        kecamatan = input("Masukkan kecamatan: ")
        kabupaten = input('Masukkan kabupaten: ')
        while True:
            telp = input('Masukkan no. telp: ')
            if len(telp) < 10:
                print('Username harus minimal 8 karakter. Silakan coba lagi.')
            else:
                break   
        email = input('Masukkan email: ')
        while True:
            username = input('Masukkan username (minimal 8 karakter): ')
            if len(username) < 8:
                print('Username harus minimal 8 karakter. Silakan coba lagi.')
            else:
                break

        while True:
            password = input('Masukkan password (minimal 8 karakter): ')
            if len(password) < 8:
                print('Password harus minimal 8 karakter. Silakan coba lagi.')
            else:
                break

        display_customer_data(name, alamat, desa, kecamatan, kabupaten, telp, email, username, password)
        confirm = input('Apakah data di atas sudah benar? (y/n): ')
        if confirm.lower() == 'y':
            cs.register_customer(name, alamat, desa, kecamatan, kabupaten, telp, email, username, password)
            break
        else:
            print('Silakan isi kembali data registrasi.\n')

def login_berhasil(customer):
    os.system('cls')
    print('Login berhasil!')
    print("+" + "-"*50 + "+")
    print("|{:^50}|".format("Login berhasil!"))
    print("+" + "-"*50 + "+")
    print(f'Selamat datang, {customer["nama_customer"]}')

def menu_cust():
    os.system('cls')
    print("\n" + "+" + "-"*50 + "+")
    print("|{:^50}|".format("MENU"))
    print("+" + "-"*50 + "+")
    print("|{:<50}|".format("1. Lihat daftar lapangan"))
    print("|{:<50}|".format("2. Keluar"))
    print("+" + "-"*50 + "+")

def display_detail_reservasi(tanggal_reservasi, tanggal_jadwal, jam_awal_waktu, jam_akhir_waktu):
    data = [
        ["Tanggal Reservasi", tanggal_reservasi],
        ["Tanggal Jadwal", tanggal_jadwal],
        ["Jam Awal", f"{jam_awal_waktu}.00"],
        ["Jam Akhir", f"{jam_akhir_waktu}.00"]
    ]
    print(tabulate(data, tablefmt="grid"))

    
def display_lapangan_terpilih(selected_lapangan):
    data = [[selected_lapangan['nomor_lapangan'], 
             selected_lapangan['jenis_lapangan'], 
             selected_lapangan['deskripsi_lapangan'], 
             selected_lapangan['harga_sewa_lapangan']]]
    headers = ["Nomor Lapangan", "Jenis Lapangan", "Deskripsi", "Harga Sewa"]
    print(tabulate(data, headers=headers, tablefmt="grid"))


def detail_rev_eq(selected_eq_id, peralatan, jam_awal, jam_akhir, selected_lapangan, customer_id, tanggal_reservasi):
    if selected_eq_id in [eq["id_alat"] for eq in peralatan]:
        jumlah_alat = next((eq["jumlah_alat"] for eq in peralatan if eq["id_alat"] == selected_eq_id), 0)
        quantity_alat = int(input("Masukkan jumlah peralatan yang ingin disewa: "))
        if quantity_alat < 0:
            print("Jumlah peralatan harus lebih dari 0.")
        elif quantity_alat > jumlah_alat:
            print("Jumlah peralatan harus lebih kecil dari jumlah stoknya.")
        else:
            selected_eq_name = next((eq["jenis_alat"] for eq in peralatan if eq["id_alat"] == selected_eq_id), None)
            print(f"Anda memesan {quantity_alat} {selected_eq_name}.")
            quantity_lapangan = jam_akhir - jam_awal  
            total_harga_lapangan = selected_lapangan['harga_sewa_lapangan'] * quantity_lapangan
            total_harga_alat = next((eq["harga_sewa_alat"] * quantity_alat for eq in peralatan if eq["id_alat"] == selected_eq_id), 0)
            total_harga = total_harga_lapangan + total_harga_alat
            os.system('cls')
            print(f"Quantity Lapangan: {quantity_lapangan} jam")
            print(f"Total Harga: Rp{total_harga}")

            methods = cs.metode_pembayaran()
            print("\nPilih Metode Pembayaran:")
            for method in methods:
                print(f"{method[0]}. {method[1]}")
            while True:
                try:
                    metode_pembayaran_id = int(input("\nMasukkan ID metode pembayaran: "))
                    selected_method = next((method for method in methods if method[0] == metode_pembayaran_id), None)
                    if selected_method:
                        no_rek = selected_method[2]
                        nama_pemilik = selected_method[3]

                        print(f"\nSilakan transfer ke rekening berikut:")
                        print(f"Nomor Rekening: {no_rek}")
                        print(f"Nama Pemilik: {nama_pemilik}")
                        break
                    else:
                        print("ID metode pembayaran tidak valid. Silakan coba lagi.")
                except ValueError:
                    print("ID metode pembayaran harus berupa angka.")

            deadline = datetime.now() + timedelta(days=1)
            print(f"\nAnda memiliki waktu 24 jam untuk melakukan pembayaran.")
            print(f"Deadline pembayaran: {deadline.strftime('%Y-%m-%d %H:%M:%S')}")

            bukti_pembayaran = input("Masukkan link bukti pembayaran: ")
            print(f"Terima kasih! Bukti pembayaran Anda telah diunggah dengan link: {bukti_pembayaran}")
            status_pembayaran = "Pending"
            id_reservasi = cs.reservasi_id_cari(customer_id)
            cs.bukti_bayar(id_reservasi, bukti_pembayaran)
            cs.simpan_detail_reservasi(total_harga, tanggal_reservasi, bukti_pembayaran, status_pembayaran, quantity_lapangan, id_reservasi, quantity_alat, metode_pembayaran_id, selected_eq_id, selected_lapangan['nomor_lapangan'])
            cs.update_jumlah_alat(selected_eq_id, quantity_alat)
    else:
        print("ID peralatan tidak valid. Silakan coba lagi.")

def maincus():
    while True:
        os.system('cls')
        print("+" + "-"*50 + "+")
        print("|{:^50}|".format("MENU"))
        print("+" + "-"*50 + "+")
        print("| {:<48} |".format("1. Register"))
        print("| {:<48} |".format("2. Login"))
        print("+" + "-"*50 + "+")
        pilihan = input('Pilih menu: ')

        if pilihan == '1':
            register_process()      
        elif pilihan == '2':
            username = input('Masukkan username: ')
            password = input('Masukkan password: ')
            customer = cs.login_customer(username, password)
            if customer:
                login_berhasil(customer)
                while True:
                    menu_cust()
                    pilihan2 = input('Pilih menu: ')
                    if pilihan2 == '1':
                        os.system('cls')
                        print("+" + "-"*50 + "+")
                        print("|{:^50}|".format("Daftar Lapangan Bulutangkis"))
                        print("+" + "-"*50 + "+")

                        lap = cs.lapangan()
                        display_lapangan(lap)

                        while True:
                            try:
                                selected_lapangan_id = int(input("\nMasukkan ID lapangan yang ingin disewa: "))
                                if selected_lapangan_id in [lapangan["nomor_lapangan"] for lapangan in lap]:
                                    break
                                else:
                                    print("ID lapangan tidak valid. Silakan coba lagi.")
                            except ValueError:
                                print("ID lapangan harus berupa angka.")

                        print(f"Anda memilih lapangan dengan ID {selected_lapangan_id}")
                        selected_lapangan = next((lapangan for lapangan in lap if lapangan["nomor_lapangan"] == selected_lapangan_id), None)
                        if selected_lapangan:
                            os.system('cls')
                            display_lapangan_terpilih(selected_lapangan)
                            while True:
                                try:
                                    tanggal_jadwal = input("Masukkan tanggal jadwal (YYYY-MM-DD): ")
                                    jam_awal = int(input("Masukkan jam awal (7-23): "))
                                    jam_akhir = int(input("Masukkan jam akhir (7-23): "))
                                                                           
                                    if jam_awal < 8 or jam_awal > 23 or jam_akhir < 8 or jam_akhir > 23 or jam_awal >= jam_akhir:
                                        print("Jam awal dan jam akhir harus berada dalam rentang 0-23 dan jam akhir harus lebih besar dari jam awal.")
                                    else:
                                        break
                                except ValueError:
                                    print("Jam awal dan jam akhir harus berupa angka.")
 
                            tanggal_reservasi = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            tanggal_jadwal = datetime.strptime(tanggal_jadwal, "%Y-%m-%d").date()

                            tanggal_reservasi_datetime = datetime.strptime(tanggal_reservasi, "%Y-%m-%d %H:%M:%S")
                            nama_hari = tanggal_reservasi_datetime.strftime("%A")
                            waktu_reservasi = datetime.now().time()
                            nama_hari = str(nama_hari)
                            jam_awal_waktu = str(jam_awal) if len(str(jam_awal)) > 1 else '0' + str(jam_awal)
                            jam_akhir_waktu = str(jam_akhir) if len(str(jam_akhir)) > 1 else '0' + str(jam_akhir)

                            os.system('cls')
                            display_detail_reservasi(tanggal_reservasi, tanggal_jadwal, jam_awal_waktu, jam_akhir_waktu)

                            while True:
                                os.system('cls')
                                print("\n" + "+" + "-"*50 + "+")
                                print("|{:^50}|".format("Pilih Tindakan"))
                                print("+" + "-"*50 + "+")
                                print("|{:<50}|".format("1. Sewa Raket"))
                                print("|{:<50}|".format("2. Langsung bayar"))
                                print("|{:<50}|".format("3. Keluar"))
                                print("+" + "-"*50 + "+")
                                pilihan = input('Pilih menu: ')

                                if pilihan == '1':
                                    os.system('cls')
                                    display_reservasi(tanggal_reservasi, tanggal_jadwal, jam_awal_waktu, jam_akhir_waktu)
                                    confirm = input('Apakah data di atas sudah benar? (y/n): ')
                                    if confirm.lower() == 'y':
                                        os.system('cls')
                                        customer_id = cs.customer_id_cari(username)
                                        karyawan_id = cs.karyawan_cari(nama_hari, waktu_reservasi)
                                        cs.simpan_reservasi(tanggal_reservasi, tanggal_jadwal, jam_awal, jam_akhir, customer_id, karyawan_id)                                       
                                    else:
                                        os.system('cls')
                                        break
                                    
                                    print("\nSewa Raket:")
                                    peralatan = cs.alat()
                                    display_alat(peralatan)
                                    while True:
                                        try:
                                            selected_eq_id = int(input("\nMasukkan ID peralatan yang ingin disewa: "))
                                            detail_rev_eq(selected_eq_id, peralatan, jam_awal, jam_akhir, selected_lapangan, customer_id, tanggal_reservasi)
                                            break
                                        except ValueError:
                                            print("ID peralatan dan jumlah harus berupa angka.")
                                elif pilihan == '2':
                                    os.system('cls')
                                    display_reservasi(tanggal_reservasi, tanggal_jadwal, jam_awal_waktu, jam_akhir_waktu)
                                    confirm = input('Apakah data di atas sudah benar? (y/n): ')
                                    if confirm.lower() == 'y':
                                        os.system('cls')
                                        customer_id = cs.customer_id_cari(username)
                                        karyawan_id = cs.karyawan_cari(nama_hari, waktu_reservasi)
                                        cs.simpan_reservasi(tanggal_reservasi, tanggal_jadwal, jam_awal, jam_akhir, customer_id, karyawan_id)                                       
                                    else:
                                        os.system('cls')
                                        break
                                    quantity_lapangan = jam_akhir - jam_awal  
                                    total_harga = selected_lapangan['harga_sewa_lapangan'] * quantity_lapangan  
                                    print(f"Quantity Lapangan: {quantity_lapangan} jam")
                                    print(f"Total Harga: Rp {total_harga}")

                                    methods = cs.metode_pembayaran()
                                    print("\nPilih Metode Pembayaran:")
                                    for method in methods:
                                        print(f"{method[0]}. {method[1]}")
                                    while True:
                                        try:
                                            metode_pembayaran_id = int(input("\nMasukkan ID metode pembayaran: "))
                                            selected_method = next((method for method in methods if method[0] == metode_pembayaran_id), None)
                                            if selected_method:
                                                no_rek = selected_method[2]
                                                nama_pemilik = selected_method[3]
                                                
                                                print(f"\nSilakan transfer ke rekening berikut:")
                                                print(f"Nomor Rekening: {no_rek}")
                                                print(f"Nama Pemilik: {nama_pemilik}")
                                                break
                                            else:
                                                print("ID metode pembayaran tidak valid. Silakan coba lagi.")
                                        except ValueError:
                                            print("ID metode pembayaran harus berupa angka.")
                                    
                                    deadline = datetime.now() + timedelta(days=1)
                                    print(f"\nAnda memiliki waktu 24 jam untuk melakukan pembayaran.")
                                    print(f"Deadline pembayaran: {deadline.strftime('%Y-%m-%d %H:%M:%S')}")
                                    
                                    os.system('cls')
                                    bukti_pembayaran = input("Masukkan link bukti pembayaran: ")
                                    print(f"Terima kasih! Bukti pembayaran Anda telah diunggah dengan link: {bukti_pembayaran}")
                                    status_pembayaran = "Pending"
                                    id_reservasi = cs.reservasi_id_cari(customer_id)
                                    cs.bukti_bayar(id_reservasi, bukti_pembayaran)
                                    cs.simpan_detail_reservasi(total_harga, tanggal_reservasi, bukti_pembayaran, status_pembayaran, quantity_lapangan, id_reservasi, None, metode_pembayaran_id, None, selected_lapangan_id)
                                    break
                                elif pilihan == '3':
                                    os.system('cls')
                                    print("Keluar dari program.")
                                    break
                                else:
                                    os.system('cls')
                                    print("Pilihan tidak valid. Silakan coba lagi.")
                            break
                        else:
                            os.system('cls')
                            print("Lapangan tidak ditemukan. Silakan coba lagi.")
                    elif pilihan2 == '2':
                        os.system('cls')
                        print("+" + "-"*50 + "+")
                        print("|{:^50}|".format("Keluar dari program."))
                        print("+" + "-"*50 + "+")
                        break
            else:
                os.system('cls')
                print("+" + "-"*50 + "+")
                print("|{:^50}|".format("Login gagal. Silakan coba lagi."))
                print("+" + "-"*50 + "+")
maincus()

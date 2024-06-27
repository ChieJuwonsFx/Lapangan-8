import psycopg2
from psycopg2.extras import RealDictCursor
import bcrypt 
from tabulate import tabulate

def get_db_connection():
    conn = psycopg2.connect(
        dbname="basdapro",
        user="postgres",
        password="chiel188",
    )
    return conn


# Login Karyawan
def login_karyawan(username, password):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cur.execute("SELECT * FROM karyawan WHERE username_karyawan = %s", (username,))
        karyawan = cur.fetchone()
        if karyawan:
            if bcrypt.checkpw(password.encode('utf-8'), karyawan['password_karyawan'].encode('utf-8')):
                return karyawan
        return None
    except Exception as e:
        print(f'Error: {e}')
        return None
    finally:
        cur.close()
        conn.close()


# Data Customer
def display_customer():
    conn = get_db_connection()  
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cursor.execute("SELECT nama_customer, email_customer, no_telp_customer, alamat_customer || ', ' || desa_customer || ', ' || kecamatan_customer || ', ' || kabupaten_customer as alamat_lengkap_customer FROM customer ORDER BY id_customer;") 
        customers = cursor.fetchall()
        data = []
        for customer in customers:
            name = customer['nama_customer']
            email = customer['email_customer']
            telp = customer['no_telp_customer']
            alamat_lengkap = customer['alamat_lengkap_customer']
            data.append([name, email, telp, alamat_lengkap])
        
        headers = ["Nama", "Email", "No. Telp", "Alamat Lengkap"]
        print(tabulate(data, headers=headers, tablefmt="grid"))
    except psycopg2.Error as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()


# Data Karyawan
def display_karyawan():
    conn = get_db_connection()  
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cursor.execute("SELECT id_karyawan, nama_karyawan, no_telp_karyawan, alamat_karyawan || ', ' || desa_karyawan || ', ' || kecamatan_karyawan || ', ' || kabupaten_karyawan as alamat_lengkap_karyawan, username_karyawan, is_active FROM karyawan ORDER BY id_karyawan;") 
        admin = cursor.fetchall()
        data = []
        for karyawan in admin:
            id = karyawan ["id_karyawan"]
            name = karyawan['nama_karyawan']
            telp = karyawan['no_telp_karyawan']
            alamat_lengkap = karyawan['alamat_lengkap_karyawan']
            username = karyawan['username_karyawan']
            is_active = karyawan ['is_active']
            data.append([id, name, telp, alamat_lengkap, username, is_active])
        
        headers = ["ID", "Nama", "No. Telp", "Alamat Lengkap", "Username", "Active"]
        print(tabulate(data, headers=headers, tablefmt="grid"))
    except psycopg2.Error as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

def create_karyawan(nama, alamat, no_telp, desa, kecamatan, kabupaten, username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        is_active = True
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        cursor.execute("INSERT INTO karyawan (nama_karyawan, alamat_karyawan, no_telp_karyawan, desa_karyawan, kecamatan_karyawan, kabupaten_karyawan, username_karyawan, password_karyawan, is_active) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);",
        (nama, alamat, no_telp, desa, kecamatan, kabupaten, username, hashed_password, is_active))
        conn.commit()
        print("Data karyawan berhasil ditambahkan!")
    except psycopg2.Error as e:
        conn.rollback()
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

def update_karyawan(id_karyawan, nama, alamat, no_telp, desa, kecamatan, kabupaten, username, password, is_active):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        cursor.execute("UPDATE karyawan SET nama_karyawan = %s, alamat_karyawan = %s, no_telp_karyawan = %s, desa_karyawan = %s, kecamatan_karyawan = %s, kabupaten_karyawan = %s, username_karyawan = %s, password_karyawan = %s, is_active = %s WHERE id_karyawan = %s;",
        (nama, alamat, no_telp, desa, kecamatan, kabupaten, username, hashed_password, is_active, id_karyawan))
        conn.commit()
        print("Data karyawan berhasil diperbarui!")
    except psycopg2.Error as e:
        conn.rollback()
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()


def delete_karyawan(id_karyawan):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE karyawan SET is_active = FALSE WHERE id_karyawan = %s;", (id_karyawan,))
        conn.commit()
        print("Data karyawan berhasil dinonaktifkan!")
    except psycopg2.Error as e:
        conn.rollback()
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()


# Data Lapangan
def display_lapangan():
    conn = get_db_connection()  
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cursor.execute("SELECT l.nomor_lapangan, l.kondisi_lapangan, jl.jenis_lapangan FROM lapangan l JOIN jenis_lapangan jl ON l.jenis_lapangan_id_jenis_lapangan = jl.id_jenis_lapangan ORDER BY nomor_lapangan;") 
        lap = cursor.fetchall()
        data = []
        for lapangan in lap:
            nomor = lapangan ["nomor_lapangan"]
            kondisi = lapangan['kondisi_lapangan']
            jenis = lapangan['jenis_lapangan']
            data.append([nomor, kondisi, jenis])
        
        headers = ["Nomor", "Kondisi", "Jenis Lapangan"]
        print(tabulate(data, headers=headers, tablefmt="grid"))
    except psycopg2.Error as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

def create_lapangan(nomor_lapangan, kondisi_lapangan, jenis_lapangan_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO lapangan (nomor_lapangan, kondisi_lapangan, jenis_lapangan_id_jenis_lapangan) VALUES (%s, %s, %s);",
        (nomor_lapangan, kondisi_lapangan, jenis_lapangan_id))
        conn.commit()
        print("Data lapangan berhasil ditambahkan!")
    except psycopg2.Error as e:
        conn.rollback()
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

def update_lapangan(nomor_lapangan, kondisi_lapangan, jenis_lapangan_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE lapangan SET kondisi_lapangan = %s, jenis_lapangan_id_jenis_lapangan = %s WHERE nomor_lapangan = %s;",
        (kondisi_lapangan, jenis_lapangan_id, nomor_lapangan))
        conn.commit()
        print("Data lapangan berhasil diperbarui!")
    except psycopg2.Error as e:
        conn.rollback()
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()


# Data Jenis Lapangan
def display_jenis_lapangan():
    conn = get_db_connection()  
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cursor.execute("SELECT id_jenis_lapangan, jenis_lapangan, deskripsi_lapangan, harga_sewa_lapangan FROM jenis_lapangan ORDER BY id_jenis_lapangan;") 
        lap = cursor.fetchall()
        data = []
        for jenis in lap:
            id = jenis ["id_jenis_lapangan"]
            namaJenis = jenis['jenis_lapangan']
            deskripsi = jenis['deskripsi_lapangan']
            harga = jenis['harga_sewa_lapangan']
            data.append([id, namaJenis, deskripsi, harga])
        
        headers = ["ID", "Jenis", "Deskripsi", "Harga"]
        print(tabulate(data, headers=headers, tablefmt="grid"))
    except psycopg2.Error as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

def create_jenis_lapangan(jenis_lapangan, deskripsi_lapangan, harga_sewa_lapangan):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO jenis_lapangan (jenis_lapangan, deskripsi_lapangan, harga_sewa_lapangan) VALUES (%s, %s, %s);",
            (jenis_lapangan, deskripsi_lapangan, harga_sewa_lapangan))
        conn.commit()
        print("Data jenis lapangan berhasil ditambahkan!")
    except psycopg2.Error as e:
        conn.rollback()
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

def update_jenis_lapangan(id_jenis_lapangan, jenis_lapangan, deskripsi_lapangan, harga_sewa_lapangan):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE jenis_lapangan SET jenis_lapangan = %s, deskripsi_lapangan = %s, harga_sewa_lapangan = %s WHERE id_jenis_lapangan = %s;",
        (jenis_lapangan, deskripsi_lapangan, harga_sewa_lapangan, id_jenis_lapangan))
        conn.commit()
        print("Data jenis lapangan berhasil diperbarui!")
    except psycopg2.Error as e:
        conn.rollback()
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()


# Data Alat
def display_alat():
    conn = get_db_connection()  
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cursor.execute("SELECT id_alat, jenis_alat, jumlah_alat, harga_sewa_alat FROM alat_olahraga ORDER BY id_alat;") 
        alator = cursor.fetchall()
        data = []
        for alat in alator:
            id = alat ["id_alat"]
            namaAlat = alat['jenis_alat']
            jumlah = alat['jumlah_alat']
            harga = alat['harga_sewa_alat']
            data.append([id, namaAlat, jumlah, harga])
        
        headers = ["ID", "Nama", "Jumlah", "Harga"]
        print(tabulate(data, headers=headers, tablefmt="grid"))
    except psycopg2.Error as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

def create_alat_olahraga(jenis_alat, jumlah_alat, harga_sewa_alat):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO alat_olahraga (jenis_alat, jumlah_alat, harga_sewa_alat) VALUES (%s, %s, %s);",
        (jenis_alat, jumlah_alat, harga_sewa_alat))
        conn.commit()
        print("Data alat olahraga berhasil ditambahkan!")
    except psycopg2.Error as e:
        conn.rollback()
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

def update_alat_olahraga(id_alat, jenis_alat, jumlah_alat, harga_sewa_alat):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE alat_olahraga SET jenis_alat = %s, jumlah_alat = %s, harga_sewa_alat = %s WHERE id_alat = %s;",
        (jenis_alat, jumlah_alat, harga_sewa_alat, id_alat))
        conn.commit()
        print("Data alat olahraga berhasil diperbarui!")
    except psycopg2.Error as e:
        conn.rollback()
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()


# Data Shift
def display_shift():
    conn = get_db_connection()  
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cursor.execute("SELECT id_shift, tanggal_berlaku, tanggal_berakhir, hari_shift, jam_awal_shift, jam_akhir_shift FROM jadwal_shift ORDER BY id_shift;") 
        shifts = cursor.fetchall()
        data = []
        for shift in shifts:
            id = shift['id_shift']
            tanggal_berlaku = shift ['tanggal_berlaku']
            tanggal_berakhir = shift ['tanggal_berakhir']
            hari = shift['hari_shift']
            jam_awal = shift['jam_awal_shift']
            jam_akhir = shift['jam_akhir_shift']
            data.append([id, tanggal_berlaku, tanggal_berakhir, hari, jam_awal, jam_akhir ])
        
        headers = ["ID", "Tanggal Berlaku", "Tanggal Berakhir", "Hari", "Jam Awal", "Jam Akhir"]
        print(tabulate(data, headers=headers, tablefmt="grid"))
    except psycopg2.Error as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

def create_jadwal_shift(tanggal_berlaku, tanggal_berakhir, hari_shift, jam_awal_shift, jam_akhir_shift):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO jadwal_shift (tanggal_berlaku, tanggal_berakhir, hari_shift, jam_awal_shift, jam_akhir_shift) VALUES (%s, %s, %s, %s, %s);",
        (tanggal_berlaku, tanggal_berakhir, hari_shift, jam_awal_shift, jam_akhir_shift))
        conn.commit()
        print("Data jadwal shift berhasil ditambahkan!")
    except psycopg2.Error as e:
        conn.rollback()
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

def update_jadwal_shift(id_shift, tanggal_berlaku, tanggal_berakhir, hari_shift, jam_awal_shift, jam_akhir_shift):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE jadwal_shift SET tanggal_berlaku = %s, tanggal_berakhir = %s, hari_shift = %s, jam_awal_shift = %s, jam_akhir_shift = %s WHERE id_shift = %s;",
        (tanggal_berlaku, tanggal_berakhir, hari_shift, jam_awal_shift, jam_akhir_shift, id_shift))
        conn.commit()
        print("Data jadwal shift berhasil diperbarui!")
    except psycopg2.Error as e:
        conn.rollback()
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

def delete_jadwal_shift(id_detail_shift):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM detail_shift WHERE id_detail_shift = %s;", (id_detail_shift,))

        conn.commit()
        if cursor.rowcount > 0:
            print(f"Detail shift dengan ID {id_detail_shift} berhasil dihapus.")
        else:
            print(f"Tidak ada ID {id_detail_shift} dalam detail shift.")
        
    except psycopg2.Error as e:
        conn.rollback()
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()


# Data Metode Pembayaran
def display_metode():
    conn = get_db_connection()  
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cursor.execute("SELECT id_metode_pembayaran, nama_metode_pembayaran, no_rekening_pengelola, nama_pemilik FROM metode_pembayaran ORDER BY id_metode_pembayaran;") 
        cara = cursor.fetchall()
        data = []
        for metode in cara:
            id = metode['id_metode_pembayaran']
            nama = metode ['nama_metode_pembayaran']
            no_rek = metode ['no_rekening_pengelola']
            pemilik = metode['nama_pemilik']
            data.append([id, nama, no_rek, pemilik])
        
        headers = ["ID", "Nama Metode", "No Rek", "Pemilik"]
        print(tabulate(data, headers=headers, tablefmt="grid"))
    except psycopg2.Error as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

def create_metode_pembayaran(nama_metode_pembayaran, no_rekening_pengelola, nama_pemilik):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO metode_pembayaran (nama_metode_pembayaran, no_rekening_pengelola, nama_pemilik) VALUES (%s, %s, %s);", 
        (nama_metode_pembayaran, no_rekening_pengelola, nama_pemilik))
        conn.commit()
        print("Data metode pembayaran berhasil ditambahkan!")
    except psycopg2.Error as e:
        conn.rollback()
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

def update_metode_pembayaran(id_metode_pembayaran, nama_metode_pembayaran, no_rekening_pengelola, nama_pemilik):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE metode_pembayaran SET nama_metode_pembayaran = %s, no_rekening_pengelola = %s, nama_pemilik = %s WHERE id_metode_pembayaran = %s;", 
        (nama_metode_pembayaran, no_rekening_pengelola, nama_pemilik, id_metode_pembayaran))
        conn.commit()
        print("Data metode pembayaran berhasil diperbarui!")
    except psycopg2.Error as e:
        conn.rollback()
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()


# Data Reservasi
def display_reservasi():
    conn = get_db_connection()  
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cursor.execute("SELECT r.id_reservasi, r.tanggal_reservasi, r.tanggal_jadwal, r.jam_awal, r.jam_akhir, c.nama_customer, k.nama_karyawan FROM reservasi r JOIN customer c ON r.customer_id_customer = c.id_customer JOIN karyawan k ON r.karyawan_id_karyawan = k.id_karyawan ORDER BY id_reservasi;") 
        pesan = cursor.fetchall()
        data = []
        for reservasi in pesan:
            id = reservasi['id_reservasi']
            tanggal_reservasi = reservasi ['tanggal_reservasi']
            tanggal_jadwal = reservasi ['tanggal_jadwal']
            jam_awal = reservasi['jam_awal']
            jam_akhir = reservasi['jam_akhir']
            customer = reservasi['nama_customer']
            karyawan = reservasi['nama_karyawan']
            data.append([id, tanggal_reservasi, tanggal_jadwal, jam_awal, jam_akhir, customer, karyawan])
        
        headers = ["ID", "Tanggal Reservasi", "Tanggal Jadwal", "Jam Awal", "Jam Akhir", "Nama Customer", "Nama Karyawan"]
        print(tabulate(data, headers=headers, tablefmt="grid"))
    except psycopg2.Error as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()


# Konfirmasi Pembayaran
def display_detail_reservasi():
    conn = get_db_connection()  
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cursor.execute("""
            SELECT
                r.id_reservasi,
                COALESCE(dr.total_pembayaran, 0) AS total_pembayaran,
                dr.tanggal_pembayaran,
                dr.status_pembayaran,
                dr.quantity_reservasi,
                dr.quantity_alat,
                m.nama_metode_pembayaran,
                a.jenis_alat,
                COALESCE(l.nomor_lapangan, 0) AS nomor_lapangan,
                p.id_pengembalian
            FROM
                detail_reservasi dr
            JOIN
                reservasi r ON dr.reservasi_id_reservasi = r.id_reservasi
            JOIN
                metode_pembayaran m ON dr.metode_pembayaran_id_metode_pembayaran = m.id_metode_pembayaran
            LEFT JOIN
                pengembalian_alat_olahraga p ON dr.pengembalian_alat_olahraga_id_pengembalian = p.id_pengembalian
            LEFT JOIN
                lapangan l ON dr.lapangan_nomor_lapangan = l.nomor_lapangan
            LEFT JOIN
                alat_olahraga a ON dr.alat_olahraga_id_alat = a.id_alat
            ORDER BY
                r.id_reservasi;
        """) 
        pesan = cursor.fetchall()
        data = []
        for reservasi in pesan:
            id = reservasi['id_reservasi']
            total = reservasi['total_pembayaran']
            tanggal_pembayaran = reservasi['tanggal_pembayaran']
            status = reservasi['status_pembayaran']
            quantity_reservasi = reservasi['quantity_reservasi']
            quantity_alat = reservasi['quantity_alat']
            metode = reservasi['nama_metode_pembayaran']
            alat = reservasi['jenis_alat']
            lapangan = reservasi['nomor_lapangan']
            pengembalian = reservasi['id_pengembalian']
            data.append([id, total, tanggal_pembayaran, status, quantity_reservasi, quantity_alat, metode, alat, lapangan, pengembalian])
        
        headers = ["ID", "Total Bayar", "Tanggal Bayar", "Status", "Jumlah Lapangan", "Jumlah Alat", "Metode Bayar", "Jenis Alat", "Nomor Lapangan", "ID Kembali"]
        print(tabulate(data, headers=headers, tablefmt="grid"))
    except psycopg2.Error as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

def update_status_pembayaran(id_detail, status_pembayaran):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE detail_reservasi SET status_pembayaran = %s WHERE id_detail_reservasi = %s;""",
        (status_pembayaran, id_detail))
        conn.commit()
        print("Status pembayaran detail reservasi berhasil diperbarui!")
    except psycopg2.Error as e:
        conn.rollback()
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()


# Data Pengembalian
def display_pengembalian():
    conn = get_db_connection()  
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cursor.execute("SELECT p.id_pengembalian, p.tanggal_pengembalian, p.jumlah_alat_kembali, ao.jenis_alat, c.nama_customer FROM pengembalian_alat_olahraga p JOIN detail_reservasi dr ON p.id_pengembalian = dr.pengembalian_alat_olahraga_id_pengembalian JOIN alat_olahraga ao ON dr.alat_olahraga_id_alat = ao.id_alat JOIN reservasi r ON dr.reservasi_id_reservasi = r.id_reservasi JOIN customer c ON r.customer_id_customer = c.id_customer ORDER BY id_pengembalian;") 
        kembali = cursor.fetchall()
        data = []
        for pengembalian in kembali:
            id = pengembalian['id_pengembalian']
            tanggal = pengembalian ['tanggal_pengembalian']
            alat = pengembalian ['jumlah_alat_kembali']
            jenis = pengembalian['jenis_alat']
            customer = pengembalian['nama_customer']
            data.append([id, tanggal, alat, jenis, customer])
        
        headers = ["ID", "Tanggal Pengembalian", "Jumlah Alat Kembali", "Jenis Alat", "Nama Customer"]
        print(tabulate(data, headers=headers, tablefmt="grid"))
    except psycopg2.Error as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

def select_alat_olahraga_by_id(alat_id):
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    try:
        cursor.execute("SELECT * FROM alat_olahraga WHERE id_alat = %s;", (alat_id,))
        alat = cursor.fetchone()
        return alat
    except psycopg2.Error as e:
        print("Error:", e)
        return None
    finally:
        cursor.close()
        conn.close()

def update_alat_olahraga_quantity(alat_id, new_quantity):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE alat_olahraga SET jumlah_alat = %s WHERE id_alat = %s;", (new_quantity, alat_id))
        conn.commit()
        print("Jumlah alat berhasil diperbarui!")
    except psycopg2.Error as e:
        conn.rollback()
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

def update_detail_reservasi_pengembalian_alat_id(reservasi_id, id_pengembalian):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE detail_reservasi SET pengembalian_alat_olahraga_id_pengembalian = %s WHERE reservasi_id_reservasi = %s;", (id_pengembalian, reservasi_id))
        conn.commit()
        print("ID pengembalian alat berhasil diperbarui di detail reservasi!")
    except psycopg2.Error as e:
        conn.rollback()
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

def create_pengembalian_alat(tanggal_pengembalian, jumlah_alat_kembali, alat_olahraga_id, reservasi_id):
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    try:
        cursor.execute("SELECT COUNT(*) FROM detail_reservasi WHERE reservasi_id_reservasi = %s AND pengembalian_alat_olahraga_id_pengembalian IS NOT NULL;", (reservasi_id,))
        count = cursor.fetchone()[0]
        if count > 0:
            print("Pengembalian sudah ada dalam detail reservasi. Pengembalian dibatalkan.")
            return
        
        cursor.execute(
            "INSERT INTO pengembalian_alat_olahraga (tanggal_pengembalian, jumlah_alat_kembali) VALUES (%s, %s) RETURNING id_pengembalian;",
            (tanggal_pengembalian, jumlah_alat_kembali)
        )
        id_pengembalian = cursor.fetchone()[0]

        conn.commit()
        print(f"Data pengembalian alat berhasil ditambahkan dengan ID {id_pengembalian}!")

        alat = select_alat_olahraga_by_id(alat_olahraga_id)
        if alat:
            new_quantity = int(alat['jumlah_alat']) + jumlah_alat_kembali
            update_alat_olahraga_quantity(alat_olahraga_id, new_quantity)
            print("Jumlah alat berhasil diperbarui!")
        else:
            print("ID alat olahraga tidak valid.")
            return

        update_detail_reservasi_pengembalian_alat_id(reservasi_id, id_pengembalian)
        print("Data pengembalian alat berhasil diperbarui di detail reservasi!")

    except psycopg2.Error as e:
        conn.rollback()
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()


# Data Detail Shift
def display_detail_shift():
    conn = get_db_connection()  
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cursor.execute("SELECT ds.karyawan_id_karyawan, k.nama_karyawan, ds.jadwal_shift_id_shift, j.tanggal_berlaku, j.tanggal_berakhir, j.hari_shift, j.jam_awal_shift, j.jam_akhir_shift FROM detail_shift ds JOIN karyawan k ON ds.karyawan_id_karyawan = k.id_karyawan JOIN jadwal_shift j ON ds.jadwal_shift_id_shift = j.id_shift ORDER BY id_karyawan;") 
        shifts = cursor.fetchall()
        data = []
        for shift in shifts:
            karyawan_id = shift['karyawan_id_karyawan']
            nama_karyawan = shift['nama_karyawan']
            shift_id = shift['jadwal_shift_id_shift']
            tanggal_berlaku = shift['tanggal_berlaku']
            tanggal_berakhir = shift['tanggal_berakhir']
            hari_shift = shift['hari_shift']
            jam_awal = shift['jam_awal_shift']
            jam_akhir = shift['jam_akhir_shift']
            data.append([karyawan_id, nama_karyawan, hari_shift, jam_awal, jam_akhir, shift_id, tanggal_berlaku, tanggal_berakhir])
        
        headers = ["ID Karyawan", "Nama Karyawan", "Hari Shift", "Jam Awal", "Jam Akhir", "ID Shift", "Tanggal Berlaku", "Tanggal Berakhir"]
        print(tabulate(data, headers=headers, tablefmt="grid"))
    except psycopg2.Error as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

def create_detail_shift(karyawan_id, jadwal_shift_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO detail_shift (karyawan_id_karyawan, jadwal_shift_id_shift) VALUES (%s, %s);",
        (karyawan_id, jadwal_shift_id))
        conn.commit()
        print("Data detail shift berhasil ditambahkan!")
    except psycopg2.Error as e:
        conn.rollback()
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

def update_detail_shift(karyawan_id, jadwal_shift_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE detail_shift SET WHERE karyawan_id_karyawan = %s jadwal_shift_id_shift = %s;",
        (karyawan_id, jadwal_shift_id))
        conn.commit()
        print("Data detail shift berhasil diperbarui!")
    except psycopg2.Error as e:
        conn.rollback()
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

def delete_detail_reservasi_sebelum(tanggal_batas):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM detail_reservasi WHERE reservasi_id_reservasi IN (SELECT id_reservasi FROM reservasi WHERE tanggal_reservasi < %s)", (tanggal_batas,)) 
        cursor.execute("DELETE FROM pengembalian_alat_olahraga WHERE id_pengembalian IN (SELECT pengembalian_alat_olahraga_id_pengembalian FROM detail_reservasi JOIN reservasi ON detail_reservasi.reservasi_id_reservasi = reservasi.id_reservasi WHERE reservasi.tanggal_reservasi < %s)", (tanggal_batas,))
        cursor.execute("DELETE FROM reservasi WHERE tanggal_reservasi < %s;", (tanggal_batas,))
        conn.commit()
        print(f"Data detail reservasi sebelum tanggal {tanggal_batas} berhasil dihapus!")
    except psycopg2.Error as e:
        conn.rollback()
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

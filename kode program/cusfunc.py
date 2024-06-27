import psycopg2
from psycopg2.extras import RealDictCursor
import bcrypt 
from datetime import datetime, time
from tabulate import tabulate 

def get_db_connection():
    conn = psycopg2.connect(
        dbname="basdapro",
        user="postgres",
        password="chiel188",
    )
    return conn


def register_customer(name, alamat, desa, kecamatan, kabupaten, telp, email, username, password):
    conn = get_db_connection()
    cur = conn.cursor()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    try:
        cur.execute("INSERT INTO customer (nama_customer, alamat_customer, desa_customer, kecamatan_customer, kabupaten_customer, no_telp_customer, email_customer, username_customer, password_customer) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (name, alamat, desa, kecamatan, kabupaten, telp, email, username, hashed_password)
        )
        conn.commit()
        print('Registrasi berhasil!')
    except Exception as e:
        print(f'Error: {e}')
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def login_customer(username, password):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cur.execute("SELECT * FROM customer WHERE username_customer = %s", (username,))
        customer = cur.fetchone()
        if customer:
            if bcrypt.checkpw(password.encode('utf-8'), customer['password_customer'].encode('utf-8')):
                return customer
        return None
    except Exception as e:
        print(f'Error: {e}')
        return None
    finally:
        cur.close()
        conn.close()

def customer_id_cari(username):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT id_customer FROM customer WHERE username_customer = %s", (username,))
        customer_id = cur.fetchone()[0]
        return customer_id
    except Exception as e:
        print(f"Error getting customer ID: {e}")
    finally:
        cur.close()
        conn.close()

def karyawan_cari(nama_hari, waktu_reservasi):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        jam_reservasi = waktu_reservasi.strftime('%H:%M:%S')

        cur.execute("SELECT k.id_karyawan FROM karyawan k JOIN detail_shift ds ON k.id_karyawan = ds.karyawan_id_karyawan JOIN jadwal_shift js ON ds.jadwal_shift_id_shift = js.id_shift WHERE k.is_active = TRUE AND js.hari_shift = %s AND js.jam_awal_shift <= %s AND js.jam_akhir_shift >= %s", (nama_hari, jam_reservasi, jam_reservasi))
        id_karyawan = cur.fetchone()
        
        if id_karyawan:
            return id_karyawan[0]
        else:
            print("Tidak ada karyawan yang tersedia untuk melayani pada waktu yang diminta.")
            return None
    except Exception as e:
        print(f"Error getting karyawan ID: {e}")
        return None
    finally:
        cur.close()
        conn.close()

def karyawan_cari(nama_hari, waktu_reservasi):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        jam_reservasi = waktu_reservasi.strftime('%H:%M:%S')

        cur.execute("SELECT k.id_karyawan FROM karyawan k JOIN detail_shift ds ON k.id_karyawan = ds.karyawan_id_karyawan JOIN jadwal_shift js ON ds.jadwal_shift_id_shift = js.id_shift WHERE js.hari_shift = %s AND js.jam_awal_shift <= %s AND js.jam_akhir_shift >= %s", (nama_hari, jam_reservasi, jam_reservasi))
        id_karyawan = cur.fetchone()
        
        if id_karyawan:
            return id_karyawan[0]
        else:
            print("Tidak ada karyawan yang tersedia untuk melayani pada waktu yang diminta.")
            return None
    except Exception as e:
        print(f"Error getting karyawan ID: {e}")
        return None
    finally:
        cur.close()
        conn.close()

def lapangan():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT l.nomor_lapangan, j.jenis_lapangan, j.deskripsi_lapangan, j.harga_sewa_lapangan FROM lapangan l JOIN jenis_lapangan j ON l.jenis_lapangan_id_jenis_lapangan = j.id_jenis_lapangan")
    rows = cur.fetchall()
    courts = []
    for row in rows:
        court = {
            "nomor_lapangan": row[0],
            "jenis_lapangan": row[1],
            "deskripsi_lapangan": row[2],
            "harga_sewa_lapangan": row[3]
        }
        courts.append(court)
    cur.close()
    conn.close()
    return courts

def alat():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id_alat, jenis_alat, jumlah_alat, harga_sewa_alat FROM alat_olahraga")
    rows = cur.fetchall()
    peralatan = []
    for row in rows:
        alat = {
            "id_alat": row[0],
            "jenis_alat": row[1],
            "jumlah_alat": row[2],
            "harga_sewa_alat": row[3]
        }
        peralatan.append(alat)
    cur.close()
    conn.close()
    return peralatan

def metode_pembayaran():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id_metode_pembayaran, nama_metode_pembayaran, no_rekening_pengelola, nama_pemilik FROM metode_pembayaran")
    methods = cur.fetchall()
    cur.close()
    conn.close()
    return methods

def bukti_bayar(reservasi_id, bukti_bayar):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "UPDATE detail_reservasi SET bukti_pembayaran = %s WHERE reservasi_id_reservasi = %s",
            (bukti_bayar, reservasi_id)
        )
        conn.commit()
        print("Bukti pembayaran berhasil disimpan ke database.")
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def simpan_reservasi(tanggal_reservasi, tanggal_jadwal, jam_awal, jam_akhir, customer_id, id_karyawan):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        jam_awal_waktu = time(jam_awal, 0)
        jam_akhir_waktu = time(jam_akhir, 0)

        cur.execute(
            "INSERT INTO reservasi (tanggal_reservasi, tanggal_jadwal, jam_awal, jam_akhir, customer_id_customer, karyawan_id_karyawan) VALUES (%s, %s, %s, %s, %s, %s) ",
            (tanggal_reservasi, tanggal_jadwal, jam_awal_waktu, jam_akhir_waktu, customer_id, id_karyawan)
        )
        conn.commit()
    except Exception as e:
        print(f"Error saving reservation: {e}")
        conn.rollback()
        raise
    finally:
        cur.close()
        conn.close()

def simpan_detail_reservasi(total_pembayaran, tanggal_pembayaran, bukti_pembayaran, status_pembayaran, quantity_reservasi, reservasi_id, quantity_alat, metode_pembayaran_id, alat_olahraga_id, nomor_lapangan):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO detail_reservasi (total_pembayaran, tanggal_pembayaran, bukti_pembayaran, status_pembayaran, quantity_reservasi, reservasi_id_reservasi, quantity_alat, metode_pembayaran_id_metode_pembayaran, alat_olahraga_id_alat, lapangan_nomor_lapangan) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (total_pembayaran, tanggal_pembayaran, bukti_pembayaran, status_pembayaran, quantity_reservasi, reservasi_id, quantity_alat, metode_pembayaran_id, alat_olahraga_id, nomor_lapangan)
        )
        conn.commit()
    except Exception as e:
        print(f"Error saving detail reservation: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def reservasi_id_cari(customer_id):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT id_reservasi FROM reservasi WHERE customer_id_customer = %s  ORDER BY id_reservasi DESC LIMIT 1", (customer_id,))
        reservasi_id = cur.fetchone()[0]
        return reservasi_id
    except Exception as e:
        print(f"Error getting customer ID: {e}")
    finally:
        cur.close()
        conn.close()

def update_jumlah_alat(alat_id, jumlah_sewa):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT jumlah_alat FROM alat_olahraga WHERE id_alat = %s", (alat_id,))
        current_quantity = cur.fetchone()[0]
        new_quantity = current_quantity - jumlah_sewa
        cur.execute("UPDATE alat_olahraga SET jumlah_alat = %s WHERE id_alat = %s", (new_quantity, alat_id))
        conn.commit()

    except psycopg2.Error as e:
        print("Terjadi kesalahan saat mengupdate jumlah alat:", e)

    finally:
        if conn:
            cur.close()
            conn.close()

def display_jenis_lapangan():
    conn = get_db_connection()  
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cursor.execute("SELECT id_jenis_lapangan, jenis_lapangan, deskripsi_lapangan, harga_sewa_lapangan FROM jenis_lapangan;") 
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
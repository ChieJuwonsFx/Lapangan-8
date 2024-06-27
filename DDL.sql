CREATE TABLE alat_olahraga (
    id_alat         SERIAL PRIMARY KEY,
    jenis_alat      VARCHAR(64) NOT NULL,
    jumlah_alat     INTEGER NOT NULL,
    harga_sewa_alat INTEGER NOT NULL
);

CREATE TABLE customer (
    id_customer        SERIAL PRIMARY KEY,
    nama_customer      VARCHAR(64) NOT NULL,
    email_customer     VARCHAR(256) NOT NULL,
    no_telp_customer   VARCHAR(16) NOT NULL,
    alamat_customer    VARCHAR(256) NOT NULL,
    desa_customer      VARCHAR(64) NOT NULL,
    kecamatan_customer VARCHAR(64) NOT NULL,
    kabupaten_customer VARCHAR(64) NOT NULL,
    username_customer  VARCHAR(64) NOT NULL,
    password_customer  VARCHAR(128) NOT NULL
);

CREATE INDEX username_customer_idx ON customer (username_customer);
CREATE INDEX email_customer_idx ON customer (email_customer);
CREATE INDEX no_telp_customer_idx ON customer (no_telp_customer);

CREATE TABLE jenis_lapangan (
    id_jenis_lapangan   SERIAL PRIMARY KEY,
    jenis_lapangan      VARCHAR(64) NOT NULL,
    deskripsi_lapangan  VARCHAR(255) NOT NULL,
    harga_sewa_lapangan INTEGER NOT NULL
);

CREATE TABLE lapangan (
    nomor_lapangan                   SERIAL PRIMARY KEY,
    kondisi_lapangan                 VARCHAR(64) NOT NULL, 
    jenis_lapangan_id_jenis_lapangan INTEGER NOT NULL,
    CONSTRAINT lapangan_jenis_lapangan_fk FOREIGN KEY (jenis_lapangan_id_jenis_lapangan)
        REFERENCES jenis_lapangan (id_jenis_lapangan)
);

CREATE TABLE metode_pembayaran (
    id_metode_pembayaran   SERIAL PRIMARY KEY,
    nama_metode_pembayaran VARCHAR(64) NOT NULL,
    no_rekening_pengelola  VARCHAR(64) NOT NULL,
    nama_pemilik           VARCHAR(64) NOT NULL
);

CREATE INDEX no_rekening_idx ON metode_pembayaran (no_rekening_pengelola);

CREATE TABLE pengembalian_alat_olahraga (
    id_pengembalian      SERIAL PRIMARY KEY,
    tanggal_pengembalian DATE NOT NULL,
    jumlah_alat_kembali  INTEGER NOT NULL
);

CREATE TABLE karyawan (
    id_karyawan        SERIAL PRIMARY KEY,
    nama_karyawan      VARCHAR(64) NOT NULL,
    alamat_karyawan    VARCHAR(255) NOT NULL,
    no_telp_karyawan   VARCHAR(16) NOT NULL,
    desa_karyawan      VARCHAR(64) NOT NULL,
    kecamatan_karyawan VARCHAR(64) NOT NULL,
    kabupaten_karyawan VARCHAR(64) NOT NULL,
    username_karyawan  VARCHAR(64) NOT NULL,
    password_karyawan  VARCHAR(128) NOT NULL
);

CREATE INDEX no_telp_karyawan_idx ON karyawan (no_telp_karyawan);
CREATE INDEX username_karyawan_idx ON karyawan (username_karyawan);

CREATE TABLE jadwal_shift (
    id_shift         SERIAL PRIMARY KEY,
    tanggal_berlaku  DATE NOT NULL,
    tanggal_berakhir DATE NOT NULL,
    hari_shift       VARCHAR(10) NOT NULL,
    jam_awal_shift   TIME NOT NULL,
    jam_akhir_shift  TIME NOT NULL
);

CREATE TABLE reservasi (
    id_reservasi         SERIAL PRIMARY KEY,
    tanggal_reservasi    DATE NOT NULL,
    tanggal_jadwal       DATE NOT NULL,
    jam_awal             TIME NOT NULL,
    jam_akhir            TIME NOT NULL,
    customer_id_customer INTEGER NOT NULL,
    karyawan_id_karyawan INTEGER NOT NULL,
    CONSTRAINT reservasi_customer_fk FOREIGN KEY (customer_id_customer)
        REFERENCES customer (id_customer),
    CONSTRAINT reservasi_karyawan_fk FOREIGN KEY (karyawan_id_karyawan)
        REFERENCES karyawan (id_karyawan)
);

CREATE TABLE detail_reservasi (
    id_detail_reservasi                        SERIAL PRIMARY KEY,
    total_pembayaran                           INTEGER NOT NULL,
    tanggal_pembayaran                         DATE NOT NULL,
    bukti_pembayaran                           VARCHAR(64) NOT NULL,
    status_pembayaran                          VARCHAR(16) NOT NULL,
    quantity_reservasi                         INTEGER NOT NULL,
    reservasi_id_reservasi                     INTEGER NOT NULL,
    quantity_alat                              INTEGER,  
    metode_pembayaran_id_metode_pembayaran     INTEGER NOT NULL,
    alat_olahraga_id_alat                      INTEGER,
    lapangan_nomor_lapangan                    INTEGER NOT NULL, 
    pengembalian_alat_olahraga_id_pengembalian INTEGER,
    CONSTRAINT detail_reservasi_alat_olahraga_fk FOREIGN KEY (alat_olahraga_id_alat)
        REFERENCES alat_olahraga (id_alat),
    CONSTRAINT detail_reservasi_lapangan_fk FOREIGN KEY (lapangan_nomor_lapangan)
        REFERENCES lapangan (nomor_lapangan),
    CONSTRAINT detail_reservasi_metode_pembayaran_fk FOREIGN KEY (metode_pembayaran_id_metode_pembayaran)
        REFERENCES metode_pembayaran (id_metode_pembayaran),
    CONSTRAINT detail_reservasi_pengembalian_alat_olahraga_fk FOREIGN KEY (pengembalian_alat_olahraga_id_pengembalian)
        REFERENCES pengembalian_alat_olahraga (id_pengembalian),
    CONSTRAINT detail_reservasi_reservasi_fk FOREIGN KEY (reservasi_id_reservasi)
        REFERENCES reservasi (id_reservasi)
);

CREATE TABLE detail_shift (
    id_detail_shift        SERIAL PRIMARY KEY,
    karyawan_id_karyawan  INTEGER NOT NULL,
    jadwal_shift_id_shift INTEGER NOT NULL,
    CONSTRAINT detail_shift_jadwal_shift_fk FOREIGN KEY (jadwal_shift_id_shift)
        REFERENCES jadwal_shift (id_shift),
    CONSTRAINT detail_shift_karyawan_fk FOREIGN KEY (karyawan_id_karyawan)
        REFERENCES karyawan (id_karyawan)
);


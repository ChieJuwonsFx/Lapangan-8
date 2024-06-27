INSERT INTO jenis_lapangan ( jenis_lapangan, deskripsi_lapangan, harga_sewa_lapangan) VALUES
('Lapangan Plester', 'Lapangan dengan permukaan plesteran memberikan stabilitas yang baik dan tahan lama untuk pengalaman bermain yang konsisten.', 25000),
('Lapangan Karpet', 'Lapangan dengan permukaan karpet memberikan kenyamanan ekstra dan meredam suara untuk lingkungan bermain yang tenang.', 35000);

INSERT INTO lapangan (kondisi_lapangan, jenis_lapangan_id_jenis_lapangan) VALUES
('Baik', 1),
('Baik', 1),
('Baik', 2),
('Baik', 2),
('Baik', 1),
('Baik', 1),
('Baik', 1),
('Baik', 1);

INSERT INTO alat_olahraga (jenis_alat, jumlah_alat, harga_sewa_alat) VALUES
('Raket', 20, 15000);

INSERT INTO metode_pembayaran (nama_metode_pembayaran, no_rekening_pengelola, nama_pemilik) VALUES
('Transfer BCA', '8912012556', 'Richie Olajuwon Santoso'),
('Dana', '081238038207', 'Richie Olajuwon Santoso');

INSERT INTO pengembalian_alat_olahraga (tanggal_pengembalian, jumlah_alat_kembali) VALUES
(TO_TIMESTAMP('2024-05-10 10:15:33', 'YYYY-MM-DD HH24:MI:SS'), 2);

INSERT INTO customer (nama_customer, email_customer, no_telp_customer, alamat_customer, desa_customer, kecamatan_customer, kabupaten_customer, username_customer, password_customer) VALUES
('Lexandra Hansen', 'axelion@gmail.com', '081238038207', 'RT 009 RW 003', 'Jambearum', 'Puger', 'Jember', 'lexa8888', '$2y$10$ThECSCpx2V5ihgBxR.4tT.1QLGa0u6DBTaMT8VbLudNSQ.cTja6US'),
('Carina Egita Tan', 'carina@gmail.com', '081238023407', 'Jln Kenari', 'Sumbersari', 'Sumbersari', 'Jember', 'carina12', '$2y$10$IdEJBGUB5YquHtE3SKthNewS0cV4HNVa1s6V1qhhP/3IE9HjRU/tu');

INSERT INTO jadwal_shift (tanggal_berlaku, tanggal_berakhir, hari_shift, jam_awal_shift, jam_akhir_shift) VALUES
(TO_DATE('2024-05-01', 'YYYY-MM-DD'), TO_DATE('2024-06-30', 'YYYY-MM-DD'), 'Monday', '08:00:00', '16:00:00'),
(TO_DATE('2024-05-01', 'YYYY-MM-DD'), TO_DATE('2024-06-30', 'YYYY-MM-DD'), 'Tuesday', '08:00:00', '16:00:00'),
(TO_DATE('2024-05-01', 'YYYY-MM-DD'), TO_DATE('2024-06-30', 'YYYY-MM-DD'), 'Wednesday', '08:00:00', '16:00:00'),
(TO_DATE('2024-05-01', 'YYYY-MM-DD'), TO_DATE('2024-06-30', 'YYYY-MM-DD'), 'Thursday', '08:00:00', '16:00:00'),
(TO_DATE('2024-05-01', 'YYYY-MM-DD'), TO_DATE('2024-06-30', 'YYYY-MM-DD'), 'Friday', '08:00:00', '16:00:00'),
(TO_DATE('2024-05-01', 'YYYY-MM-DD'), TO_DATE('2024-06-30', 'YYYY-MM-DD'), 'Saturday', '07:00:00', '16:00:00'),
(TO_DATE('2024-05-01', 'YYYY-MM-DD'), TO_DATE('2024-06-30', 'YYYY-MM-DD'), 'Sunday', '07:00:00', '16:00:00'),
(TO_DATE('2024-05-01', 'YYYY-MM-DD'), TO_DATE('2024-06-30', 'YYYY-MM-DD'), 'Monday', '16:00:00', '23:00:00'),
(TO_DATE('2024-05-01', 'YYYY-MM-DD'), TO_DATE('2024-06-30', 'YYYY-MM-DD'), 'Tuesday', '16:00:00', '23:00:00'),
(TO_DATE('2024-05-01', 'YYYY-MM-DD'), TO_DATE('2024-06-30', 'YYYY-MM-DD'), 'Wednesday', '16:00:00', '23:00:00'),
(TO_DATE('2024-05-01', 'YYYY-MM-DD'), TO_DATE('2024-06-30', 'YYYY-MM-DD'), 'Thursday', '16:00:00', '23:00:00'),
(TO_DATE('2024-05-01', 'YYYY-MM-DD'), TO_DATE('2024-06-30', 'YYYY-MM-DD'), 'Friday', '16:00:00', '23:00:00'),
(TO_DATE('2024-05-01', 'YYYY-MM-DD'), TO_DATE('2024-06-30', 'YYYY-MM-DD'), 'Saturday', '16:00:00', '23:00:00'),
(TO_DATE('2024-05-01', 'YYYY-MM-DD'), TO_DATE('2024-06-30', 'YYYY-MM-DD'), 'Sunday', '16:00:00', '23:00:00');

INSERT INTO karyawan (nama_karyawan, alamat_karyawan, no_telp_karyawan, desa_karyawan, kecamatan_karyawan, kabupaten_karyawan, username_karyawan, password_karyawan) VALUES
('Richie Olajuwon Santoso', 'RT 009 RW 003', '081234567893', 'Jambearum', 'Puger', 'Jember', 'chiejuwons', '$2y$10$a/Kq4YHKeAESRwSa0K2AJeV0z9ttTp5ATvgoePm7fJbtEHUWcGirm'),
('Ken Riezqy Fahme Hudie', 'Jl. Dahlia No. 5', '081234567894', 'Sumbersari', 'Sumbersari', 'Jember', 'hudienih', '$2y$10$eV4dvcmQqwkuUILxnyOzP.xHzZAubWSPGckE.cS090z.DwAH2d0DS'),
('Almas Teva Zahran Dinastian', 'Jl. Tulip No. 6', '081234567895', 'Tutul', 'Balung', 'Jember', 'kalisate', '$2y$10$pbXYmDXlEBLV1D1yzgdd6.cFzfHuENs1eFM/BsWgiJf/urlwZQfBa'),
('Ahmad Fais Arifin', 'Jl. Santai', '081234567905', 'Wuluhan', 'Ambulu', 'Jember', 'icangson', '$2y$10$jDTn6sqre0n/LaZW3/7dO.XP93pMNGRnN1Z78RZxClddj7pbjERum');

INSERT INTO reservasi (tanggal_reservasi, tanggal_jadwal, jam_awal, jam_akhir, customer_id_customer, karyawan_id_karyawan) VALUES
(TO_TIMESTAMP('2024-05-10 09:00:00', 'YYYY-MM-DD HH24:MI:SS'), TO_DATE('2024-05-10', 'YYYY-MM-DD'), '08:00:00', '10:00:00', 1, 1);

INSERT INTO detail_reservasi (total_pembayaran, tanggal_pembayaran, bukti_pembayaran, status_pembayaran, quantity_reservasi, reservasi_id_reservasi, quantity_alat, metode_pembayaran_id_metode_pembayaran, alat_olahraga_id_alat, lapangan_nomor_lapangan, pengembalian_alat_olahraga_id_pengembalian) VALUES
(100000, TO_DATE('2024-05-10', 'YYYY-MM-DD'), 'bukti1.png', 'Lunas', 2, 1, 2, 1, 1, 3, 1);

INSERT INTO detail_shift (karyawan_id_karyawan, jadwal_shift_id_shift) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(1, 5),
(2, 6),
(3, 7),
(4, 8),
(1, 9),
(2, 10),
(3, 11),
(4, 12),
(1, 13),
(2, 14);

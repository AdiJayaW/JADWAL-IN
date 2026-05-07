# JADWAL-IN 

JADWAL-IN adalah sebuah program sederhana berbasis Python yang dirancang untuk mengelola dan mengorganisir data jadwal kuliah secara terstruktur. Program ini dibuat untuk membantu mahasiswa membaca dan memahami urutan jadwal perkuliahan harian dengan lebih baik, sehingga dapat meminimalisir keterlambatan atau melewatkan perkuliahan.

Proyek ini dibuat sebagai implementasi konsep algoritma dalam pemrograman untuk Laporan Proyek UTS

## Fitur Utama

* **Sistem Login Pengguna**: Autentikasi sederhana menggunakan NIM (9 digit) dan Password (5 digit) yang terhubung dengan *database* berformat JSON.
* **Pengurutan Jadwal (Bubble Sort)**: Jadwal harian secara otomatis diurutkan berdasarkan parameter waktu (jam), memastikan jadwal yang lebih pagi selalu menempati urutan teratas.
* **Pencarian Mata Kuliah (Sequential Search)**: Fitur penelusuran linear yang memungkinkan pencarian jadwal berdasarkan nama mata kuliah. Mendukung pencarian teks *case-insensitive* dan *partial match* (potongan kata).

## Teknologi yang Digunakan

* **Bahasa Pemrograman**: Python
* **Penyimpanan Data**: JSON (`users.json` dan `data_jadwal.json`)

## Cara Menjalankan Program

1.  *Clone* repositori ini ke dalam perangkat lokal kamu:
    `git clone https://github.com/username-kamu/jadwal-in.git`
2.  Pastikan *file* `main.py`, `data_jadwal.json`, dan `users.json` berada di dalam direktori atau *folder* yang sama.
3.  Jalankan program melalui terminal atau *command prompt*:
    `python main.py`
4.  Lakukan *login* menggunakan data yang tersedia di `users.json` (Contoh NIM: 252000001, Password: 12345).

## Tim Pengembang (Kelompok 5)

Proyek ini dikembangkan untuk memenuhi tugas mata kuliah Analisis Algoritma dan Struktur Data pada tahun 2026 oleh:

* **Adi Jaya Wibawa** (252011114) 
* **M. Nafi Ranu S.** (252011090) 
* **Farhan Ahmad S.** (252011201) 

**Program Studi Teknik Informatika** 
**Fakultas Teknologi dan Desain** 
**Institut Teknologi dan Bisnis Asia Malang**

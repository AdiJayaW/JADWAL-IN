import time #mengimpor library time
import json #mengimpor library json untuk datanya

# MODUL MANAJEMEN DATA
def load_data(file_json): #fungsi
    try:
        with open(file_json, 'r') as file:                      # Membuka file JSON dalam mode baca ('r')
            return json.load(file)                              # Mengubah isi file JSON menjadi dictionary/list Python
    except FileNotFoundError:                                   # Jika file tidak ditemukan...
        print(f"⚠️ Error: File {file_json} tidak ditemukan!")
        return []                                               # Mengembalikan list kosong agar program tidak crash

# MODUL SORTING & SEARCHING
# ALGORITMA SORTING (Bubble Sort berdasarkan Jam)
def urutkan_jadwal_berdasarkan_jam(data):
    n = len(data)                                               # Mendapatkan jumlah item dalam list
    for i in range(n):                                          # Perulangan luar untuk setiap elemen
        for j in range(0, n-i-1):                               # Perulangan dalam untuk membandingkan elemen bersebelahan
            if data[j]['jam'] > data[j+1]['jam']:               # Jika jam di kiri lebih besar dari jam di kanan
                data[j], data[j+1] = data[j+1], data[j]         # Tukar posisi elemen
    return data

# ALGORITMA SEARCHING (Sequential Search berdasarkan Mata Kuliah)
def cari_mata_kuliah(data, keyword):
    hasil_pencarian = []                                        # List kosong untuk menampung hasil
    for jadwal in data:                                         # Memeriksa setiap data satu per satu
        if keyword.lower() in jadwal['mata_kuliah'].lower():    # Jika kata kunci ditemukan (abaikan huruf besar/kecil)
            hasil_pencarian.append(jadwal)                      # Tambahkan data ke hasil pencarian
    return hasil_pencarian

# FUNGSI TAMPILAN JADWAL
def tampilkan_jadwal(data): #disini fungsi tampilan jadwal
    if not data: #jika tidak ada jadwal maka akan print di bawahnya
        print("Jadwal tidak ditemukan.")
    else: #ini akan menampilkan judul kolomnya saja
        print("-" * 78)
        print(f"{'HARI':<10} | {'JAM':<7} | {'MATA KULIAH':<40} | {'RUANG'}")
        print("-" * 78)
        for jdw in data: #disini jika kamu ada data maka akan dikeluarkan secara satu persatu lalu ditampilkan di hari jadwal dan ada mata kuliahnya
            print(f"{jdw['hari']:<10} | {jdw['jam']:<7} | {jdw['mata_kuliah']:<40} | {jdw['ruang']}")
        print("-" * 78)


# BAGIAN AUTH (Login)

def login(database_user):
    chance = 1                                                                  # Inisialisasi percobaan pertama
    max_chance = 3                                                              # Batas maksimal percobaan
    while chance <= max_chance:                                                 # Loop selama kesempatan chance masih kurang dari max chance
        try:
            print(f"\n--- Percobaan Login ke-{chance} dari {max_chance} ---")
            print("""
"Selamat Pagi", Selamat datang di JADWAL-IN!!!!
Silahkan masukkan NIM dan Passwordnya
""")
            account_input = input("Masukkan NIM Kamu (9 digit) : ")             # Mengambil input NIM dari user

            if len(account_input) != 9:                                         # Cek validasi NIM harus 9 digit
                print("❌ Format Salah, NIM harus 9 digit!") # hasil dari print karna NIM tidak sama dengan 9 digit
                time.sleep(1) #program akan dijeda selama 1 detik
                chance += 1 #chance akan bertambah 1, jika salah disini
                continue

            # Convert setelah pengecekan panjang untuk menghindari error jika bukan angka
            account_angka = int(account_input)

            password = input("Masukkan Password Kamu (5 digit) : ")
            if len(password) != 5: #disini jika panjang password lebih dari 5 digit, maka akan print salah
                print("❌ Format Salah, Password harus 5 digit!") # ini adalah output ketika hasil printnya tidak sama dengan 5 digit
                time.sleep(1) #program akan dijeda 1 detik
                chance += 1 #menambahkan chance karna kesalahan user
                continue

            # Pengecekan data di users.json
            for user in database_user:                                                   # Mencocokkan input user dengan data di list database_user
                if user['nim'] == account_angka and user['nim_password'] == password:
                    print(f"\n✅ Login Berhasil! Selamat datang, {user['nama']}.")
                    time.sleep(1)
                    return user                                                          # Jika cocok, kembalikan data user tersebut

            print("❌ NIM atau Password yang Anda masukkan salah, silahkan coba lagi.")
            chance += 1
            time.sleep(1)

        except ValueError:                                                               # Jika user memasukkan selain angka pada NIM
            print("❌ Input tidak valid. Kamu harus memasukkan angka untuk NIM.")
            chance += 1
            time.sleep(1)

        if chance > max_chance:
            print("\n⚠️ Anda telah melakukan percobaan maksimal, coba ulangi beberapa saat lagi.")
            break

    return None                                                                          # Jika gagal 3 kali, kembalikan Kosong

# 4. MAIN MENU JADWAL-IN (UPDATED)
def main(current_user): #Fungsi main di program ini
    file_jadwal = '/content/drive/Shareddrives/ANALisis ALGOJO KELOMPOK/CODE/data_jadwal.json' # disini file jadwal diimpor
    semua_jadwal = load_data(file_jadwal) #menggunakan fungsi load data untuk membaca data json dari file_jadwal
    # FILTER JADWAL KHUSUS UNTUK USER YANG LOGIN
    jadwal_user = [j for j in semua_jadwal if j.get('nim') == current_user['nim']] #disini adalah data diambil satu persatu, dan dilabeli dengan 'j' Sementaranya, dan ditanya apakah NIM tertulis didalam jadwal, sama dengan NIM milik mahasiswa yang login saat ini?
    if not jadwal_user: #disini ditanya lagi apakah user tidak memiliki jadwal
        print(f"\n⚠️ Belum ada jadwal yang terdaftar untuk NIM {current_user['nim']}.") #disini jika menghasilkan TRUE maka akan mengprint bagian in
    else : #jika salah maka akan masuk ke while true (True tak hingga,)
        while True:
            print(f"\n=== MENU UTAMA JADWAL-IN | User: {current_user['nama']} ===")
            print("1. Tampilkan Jadwal Harian (Terurut by Jam)")
            print("2. Cari Mata Kuliah")
            print("3. Keluar")
            pilihan = input("Pilih menu (1/2/3): ") #disini user diberi 3 inputan untuk user memilih selain ini pilihan tidak valid dan harus mengulang terus menerus sampai benar

            if pilihan == '1': # Disini user jika memilih 1 maka akan menjalankan perintah bawah ini
                hari_dicari = input("Masukkan hari (contoh: Senin): ").capitalize() #disini user memasukkan harinya, contoh hari senin

                # Filter jadwal user berdasarkan hari (dari data yang sudah difilter by NIM tadi)
                jadwal_hari_ini = [j for j in jadwal_user if j['hari'] == hari_dicari]

                jadwal_terurut = urutkan_jadwal_berdasarkan_jam(jadwal_hari_ini) #disini fungsi urutan_jadwal xx, diberi variabel jadwal_terurut untuk membungkus fungsi tadi,
                print(f"\nJadwal {current_user['nama']} untuk hari {hari_dicari}:")
                tampilkan_jadwal(jadwal_terurut) #Disini hasilnya ditampilkan dengan fungsi tampilkan jadwal

            elif pilihan == '2': #disini jika user memilih 2
                matkul_dicari = input("Masukkan nama mata kuliah: ") #kita disuruh inputkan nama mata kuliah untuk searching

                # Pencarian hanya dilakukan pada jadwal milik user tersebut
                hasil = cari_mata_kuliah(jadwal_user, matkul_dicari) #disini fungsi cari_mata_kuliah dibungkus ke  hasil

                print(f"\nHasil pencarian untuk '{matkul_dicari}':")
                tampilkan_jadwal(hasil) #disini menampilkan tampilan_jadwal dengan parameter hasil

            elif pilihan == '3':
                print("Terima kasih telah menggunakan Jadwal-In! Semoga kuliahnya lancar.")
                break
            else:
                print("⚠️ Pilihan tidak valid, silakan coba lagi.")
# Main Program
if __name__ == "__main__":
    file_users = '/content/drive/Shareddrives/ANALisis ALGOJO KELOMPOK/CODE/users.json'
    database_users = load_data(file_users) #disini fungsi load_data(file_users) dibungkus ke database_users

    if not database_users: #disini ditahan ketika user tidak ditemukan di database_users maka akan print bawahnya
        print("Program dihentikan karena data user tidak ditemukan.")
    else: #disini akan masuk ke fungsi login database users untuk pencocokan ke database
        current_user = login(database_users)

        # Jika login berhasil, passing data user ke dalam fungsi main
        if current_user is not None: #disini ditanyain jika user tidak kosong maka akan masuk ke main menu
            main(current_user) # <--- Passing current_user ke sini
        else:
            print("Sesi dihentikan. Silakan jalankan ulang program untuk mencoba login kembali.")
import hashlib

def buat_hash_md5(data: str) -> str:
    """
    Membuat hash MD5 dari sebuah string data.
 
    Parameter:
        data (str): String yang akan di-hash.
 
    Return:
        str: Hasil hash MD5 dalam format hexadecimal.
    """
    hash_objek = hashlib.md5(data.encode())
    return hash_objek.hexdigest()
 
 
def input_data_profil(label: str) -> tuple:
    """
    Meminta input data profil user dari terminal.
 
    Parameter:
        label (str): Label untuk memberi tahu data mana yang sedang diinput
                     (misalnya 'Awal' atau 'Baru').
 
    Return:
        tuple: Berisi (nama, email, nomor_hp) hasil input user.
    """
    print(f"\n{'='*45}")
    print(f"  INPUT DATA PROFIL {label.upper()}")
    print(f"{'='*45}")
 
    nama     = input("  Nama Lengkap : ").strip()
    email    = input("  Email        : ").strip()
    nomor_hp = input("  Nomor HP     : ").strip()
 
    return nama, email, nomor_hp
 
 
def gabungkan_data(nama: str, email: str, nomor_hp: str) -> str:
    """
    Menggabungkan data profil menjadi satu string tunggal
    dengan pemisah tanda pipa '|'.
 
    Return:
        str: String gabungan, contoh: "Budi|budi@email.com|08123456789"
    """
    return f"{nama}|{email}|{nomor_hp}"
 
 
def tampilkan_ringkasan(label: str, nama: str, email: str, nomor_hp: str, hash_md5: str):
    """
    Menampilkan ringkasan data dan nilai hash MD5-nya ke terminal.
    """
    print(f"\n  --- Ringkasan Data {label} ---")
    print(f"  Nama     : {nama}")
    print(f"  Email    : {email}")
    print(f"  Nomor HP : {nomor_hp}")
    print(f"  Hash MD5 : {hash_md5}")
 
 
def main():
    """Fungsi utama yang menjalankan program."""
    print("\n" + "="*45)
    print("  PROGRAM CEK PERUBAHAN DATA PROFIL USER")
    print("  Menggunakan Algoritma Hash MD5")
    print("="*45)

    nama_awal, email_awal, hp_awal = input_data_profil("Awal")
    data_awal = gabungkan_data(nama_awal, email_awal, hp_awal)
    hash_awal = buat_hash_md5(data_awal)
 
    tampilkan_ringkasan("Awal", nama_awal, email_awal, hp_awal, hash_awal)

    print("\n" + "-"*45)
    print("  Masukkan data profil yang (mungkin) baru.")
    print("  Jika tidak ada perubahan, isi sama seperti sebelumnya.")
 
    nama_baru, email_baru, hp_baru = input_data_profil("Baru")
    data_baru = gabungkan_data(nama_baru, email_baru, hp_baru)
    hash_baru = buat_hash_md5(data_baru)
 
    tampilkan_ringkasan("Baru", nama_baru, email_baru, hp_baru, hash_baru)

    print(f"\n{'='*45}")
    print("  HASIL PERBANDINGAN HASH MD5")
    print(f"{'='*45}")
    print(f"  Hash Awal : {hash_awal}")
    print(f"  Hash Baru : {hash_baru}")
    print(f"{'-'*45}")
 
    if hash_awal == hash_baru:
        print("  ✅ STATUS  : Data Tidak Berubah")
        print("  (Kedua hash identik — data profil sama persis)")
    else:
        print("  ⚠️  STATUS  : Data Berubah")
        print("  (Hash berbeda — ada perubahan pada data profil)")
 
    print("="*45 + "\n")

if __name__ == "__main__":
    main()

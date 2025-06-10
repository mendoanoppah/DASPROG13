from modul import utils

def tampilkan_pemilih():
    pemilih_list = utils.load_data("data/pemilih.json")
    print("\n--- DAFTAR PEMILIH ---")
    for p in pemilih_list:
        print(f"{p['id']} - {p['nama']} ({p['jurusan']}) - Sudah Memilih: {p['sudah_memilih']}")
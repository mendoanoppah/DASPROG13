from modul import utils

def tampilkan_calon():
    calon_list = utils.load_data("data/calon.json")
    print("\n--- DAFTAR CALON KETUA ---")
    for c in calon_list:
        print(f"{c['id']} - {c['nama']} | Visi: {c['visi']} | Jumlah Suara: {c['jumlah_suara']}")
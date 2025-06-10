from modul import utils

def mulai_voting():
    pemilih_list = utils.load_data("data/pemilih.json")
    calon_list = utils.load_data("data/calon.json")

    id_pemilih = input("Masukkan ID Pemilih: ")
    pemilih = next((p for p in pemilih_list if p["id"] == id_pemilih), None)

    if not pemilih:
        print("ID pemilih tidak ditemukan.")
        return
    if pemilih["sudah_memilih"]:
        print("Anda sudah pernah memilih.")
        return

    print("\n--- CALON KETUA ---")
    for c in calon_list:
        print(f"{c['id']} - {c['nama']}")
    id_calon = input("Masukkan ID Calon yang dipilih: ")
    calon = next((c for c in calon_list if c["id"] == id_calon), None)

    if not calon:
        print("ID calon tidak ditemukan.")
        return

    # Proses voting
    calon["jumlah_suara"] += 1
    pemilih["sudah_memilih"] = True

    utils.save_data("data/pemilih.json", pemilih_list)
    utils.save_data("data/calon.json", calon_list)
    print("Voting berhasil!")
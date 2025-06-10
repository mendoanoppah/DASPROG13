from modul import utils

def tampilkan_statistik():
    pemilih_list = utils.load_data("data/pemilih.json")
    calon_list = utils.load_data("data/calon.json")

    total_pemilih = len(pemilih_list)
    sudah_memilih = sum(p["sudah_memilih"] for p in pemilih_list)
    partisipasi = (sudah_memilih / total_pemilih * 100) if total_pemilih else 0
    calon_teratas = max(calon_list, key=lambda x: x["jumlah_suara"], default=None)

    print("\n--- STATISTIK PEMILU ---")
    print(f"Total Pemilih      : {total_pemilih}")
    print(f"Sudah Memilih      : {sudah_memilih}")
    print(f"Persentase Voting  : {partisipasi:.2f}%")
    if calon_teratas:
        print(f"Calon Terbanyak    : {calon_teratas['nama']} ({calon_teratas['jumlah_suara']} suara)")
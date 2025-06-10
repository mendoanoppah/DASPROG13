from modul import pemilih, calon, voting, statistik

def main():
    while True:
        print("\n=== SISTEM E-VOTING ===")
        print("1. Lihat Daftar Pemilih")
        print("2. Lihat Daftar Calon")
        print("3. Voting")
        print("4. Tampilkan Hasil Sementara")
        print("5. Statistik Pemilu")
        print("0. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            pemilih.tampilkan_pemilih()
        elif pilihan == "2":
            calon.tampilkan_calon()
        elif pilihan == "3":
            voting.mulai_voting()
        elif pilihan == "4":
            calon.tampilkan_calon()
        elif pilihan == "5":
            statistik.tampilkan_statistik()
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak valid.")
            
if __name__ == "__main__":
    main()
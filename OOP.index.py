# Class Hewan sebagai template dasar
class Hewan:
    def __init__(self, nama, umur, jenis):
        #variabel & encapsulation
        self.nama = nama            # public attribute
        self._umur = umur           # protected attribute
        self.__jenis = jenis        # private attribute

    # Method untuk menampilkan informasi hewan
    def tampilkan_info(self):
        print(f"Nama: {self.nama}, Umur: {self._umur} tahun, Jenis: {self.__jenis}")

    # Setter dan getter untuk atribut __jenis (private)
    def set_jenis(self, jenis):
        self.__jenis = jenis  # setter untuk mengubah jenis hewan

    def get_jenis(self):
        return self.__jenis   # getter untuk mengambil nilai jenis hewan


# Class Burung sebagai subclass dari Hewan (menggunakan inheritance)
class Burung(Hewan):
    def __init__(self, nama, umur, warna_bulu):
        super().__init__(nama, umur, "Burung")  # Mewarisi konstruktor dari class Hewan
        self.warna_bulu = warna_bulu            # Atribut tambahan khusus Burung

    # Method untuk menampilkan informasi khusus burung
    def tampilkan_info(self):
        super().tampilkan_info()  # Memanggil method dari class induk
        print(f"Warna Bulu: {self.warna_bulu}")


# Contoh penggunaan class
# Membuat objek dari class Hewan
kucing = Hewan("Kucing", 3, "Mamalia")
kucing.tampilkan_info()  # Menampilkan informasi kucing

# Menggunakan setter dan getter
kucing.set_jenis("Karnivora")  # Mengubah jenis kucing menggunakan setter
print("Jenis setelah diubah:", kucing.get_jenis())  # Mendapatkan jenis hewan setelah diubah

# Membuat objek dari class Burung (inheritance dari Hewan)
elang = Burung("Elang", 5, "Coklat")
elang.tampilkan_info()  # Menampilkan informasi elang (termasuk warna bulu)

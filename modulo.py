"""01. Operasi Modulo
Modulo (mod) memberi SISA pembagian. Pada kriptografi klasik, modulo dipakai
agar pergeseran huruf yang melewati 'Z' otomatis "berputar balik" ke 'A',
alih-alih menghasilkan karakter di luar alfabet.
"""

def mod(a, m):
    """Mengembalikan sisa pembagian a oleh m, selalu bernilai 0..m-1
    (berbeda dari operator % Python biasa saat a negatif pun sebenarnya
    Python sudah menangani ini dengan benar, fungsi ini hanya untuk kejelasan)."""
    return a % m


def demo():
    print("=== DEMO OPERASI MODULO (basis 26 huruf) ===")
    contoh = [(23, 3), (25, 1), (2, -5), (29, 26), (-1, 26)]
    for a, m in contoh:
        print(f"{a} mod {m} = {mod(a, m)}")

    print("\nContoh penerapan pada pergeseran huruf:")
    print("Huruf 'X' (23) digeser 5 -> 23 + 5 =", 23 + 5, "-> tanpa modulo TIDAK valid (>25)")
    print("Dengan modulo: (23 + 5) mod 26 =", mod(23 + 5, 26), "-> huruf ke-", mod(23 + 5, 26), "yaitu 'C'")


def interaktif():
    print("\n=== MODE INTERAKTIF ===")
    print("Pilih mode:")
    print("  1. Modulo angka biasa (a mod m)")
    print("  2. Modulo pada pergeseran huruf (seperti Caesar Cipher)")
    pilihan = input("Pilihan (1/2) : ").strip()

    if pilihan == "1":
        try:
            a = int(input("Masukkan angka a : "))
            m = int(input("Masukkan angka m (modulus) : "))
            print(f"{a} mod {m} = {mod(a, m)}")
        except ValueError:
            print("Input harus berupa angka bulat.")

    elif pilihan == "2":
        try:
            huruf = input("Masukkan satu huruf (A-Z) : ").strip().upper()
            shift = int(input("Masukkan nilai pergeseran (key) : "))
            if not ("A" <= huruf <= "Z"):
                raise ValueError
            angka_asal = ord(huruf) - ord("A")
            angka_geser = angka_asal + shift
            angka_hasil = mod(angka_geser, 26)
            huruf_hasil = chr(angka_hasil + ord("A"))
            print(f"\nHuruf '{huruf}' = angka {angka_asal}")
            print(f"{angka_asal} + {shift} = {angka_geser}  (bisa di luar 0-25)")
            print(f"({angka_asal} + {shift}) mod 26 = {angka_hasil}  -> huruf '{huruf_hasil}'")
        except ValueError:
            print("Input tidak valid. Huruf harus A-Z dan key berupa angka bulat.")
    else:
        print("Pilihan tidak dikenali.")


if __name__ == "__main__":
    demo()
    interaktif()

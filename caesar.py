"""03. Caesar Cipher dengan Modulo
Enkripsi : C = (P + k) mod 26
Dekripsi : P = (C - k) mod 26
Menggunakan fungsi dari konversi.py untuk pemetaan huruf <-> angka.
"""
from konversi import huruf_ke_angka, angka_ke_huruf


def caesar(teks, key, mode="enkripsi"):
    if mode == "dekripsi":
        key = -key
    hasil = []
    for ch in teks:
        if ch.isalpha() and ch.isascii():
            angka = huruf_ke_angka(ch)
            angka_baru = (angka + key) % 26          # <- operasi modulo berperan di sini
            huruf_baru = angka_ke_huruf(angka_baru)
            hasil.append(huruf_baru.lower() if ch.islower() else huruf_baru)
        else:
            hasil.append(ch)                          # non-huruf dibiarkan apa adanya
    return "".join(hasil)


def demo():
    print("=== DEMO CAESAR CIPHER ===")
    plaintext = "KRIPTO"
    key = 3
    ciphertext = caesar(plaintext, key, "enkripsi")
    print(f"plaintext  = {plaintext}")
    print(f"key        = {key}")
    print(f"ciphertext = {ciphertext}")
    print(f"dekripsi   = {caesar(ciphertext, key, 'dekripsi')}")


def interaktif():
    print("\n=== MODE INTERAKTIF ===")
    plaintext = input("Masukkan plaintext : ")
    key = int(input("Masukkan key (shift) : "))
    ciphertext = caesar(plaintext, key, "enkripsi")
    print(f"ciphertext : {ciphertext}")
    print(f"dekripsi   : {caesar(ciphertext, key, 'dekripsi')}")


if __name__ == "__main__":
    demo()
    interaktif()

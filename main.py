"""main.py - Menjalankan seluruh demo (01-04) + 3 pengujian untuk Caesar
dan 3 pengujian untuk XOR, sesuai deliverables tugas.
"""
import modulo, konversi, caesar, xor_cipher
from caesar import caesar as caesar_fn
from xor_cipher import xor_bytes

GARIS = "=" * 60


def pengujian_caesar():
    print(GARIS)
    print("PENGUJIAN CAESAR CIPHER (3 kasus)")
    print(GARIS)
    kasus = [
        ("KRIPTO", 3),
        ("HELLO WORLD", 5),
        ("Keamanan Data!", 7),
    ]
    for i, (plaintext, key) in enumerate(kasus, 1):
        ciphertext = caesar_fn(plaintext, key, "enkripsi")
        dekripsi = caesar_fn(ciphertext, key, "dekripsi")
        status = "BERHASIL" if dekripsi == plaintext else "GAGAL"
        print(f"\nKasus {i}:")
        print(f"  plaintext  : {plaintext}")
        print(f"  key        : {key}")
        print(f"  ciphertext : {ciphertext}")
        print(f"  dekripsi   : {dekripsi}  -> {status}")


def pengujian_xor():
    print("\n" + GARIS)
    print("PENGUJIAN XOR CIPHER (3 kasus)")
    print(GARIS)
    kasus = [
        ("KRIPTO", b"KUNCI"),
        ("HELLO WORLD", b"KEY"),
        ("Data Rahasia", b"SANDI123"),
    ]
    for i, (plaintext, key) in enumerate(kasus, 1):
        data = plaintext.encode("utf-8")
        ciphertext = xor_bytes(data, key)
        dekripsi = xor_bytes(ciphertext, key).decode("utf-8")
        status = "BERHASIL" if dekripsi == plaintext else "GAGAL"
        print(f"\nKasus {i}:")
        print(f"  plaintext        : {plaintext}")
        print(f"  key              : {key.decode()}")
        print(f"  ciphertext (hex) : {ciphertext.hex()}")
        print(f"  dekripsi         : {dekripsi}  -> {status}")


if __name__ == "__main__":
    modulo.demo()
    print()
    konversi.demo()
    print()
    caesar.demo()
    print()
    xor_cipher.demo()
    print()
    pengujian_caesar()
    pengujian_xor()

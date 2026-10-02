"""04. XOR Sederhana pada Data Biner
XOR (exclusive OR) bersifat SIMETRIS: A XOR B XOR B = A.
Karena itu, fungsi yang sama bisa dipakai untuk enkripsi MAUPUN dekripsi,
cukup meng-XOR-kan data dengan kunci yang sama dua kali.
"""

def xor_bytes(data: bytes, key: bytes) -> bytes:
    """XOR setiap byte data dengan byte key yang diulang (repeating key)."""
    return bytes(d ^ key[i % len(key)] for i, d in enumerate(data))


def demo():
    print("=== DEMO XOR CIPHER ===")
    plaintext = "KRIPTO"
    key = b"KUNCI"

    data = plaintext.encode("utf-8")
    print(f"plaintext (teks)  : {plaintext}")
    print(f"plaintext (biner) : {' '.join(format(b, '08b') for b in data)}")
    print(f"key (biner)       : {' '.join(format(b, '08b') for b in key)}")

    ciphertext = xor_bytes(data, key)
    print(f"\nciphertext (hex)  : {ciphertext.hex()}")
    print(f"ciphertext (biner): {' '.join(format(b, '08b') for b in ciphertext)}")

    hasil_dekripsi = xor_bytes(ciphertext, key)          # XOR kedua kali = kembali ke asal
    print(f"\nhasil dekripsi    : {hasil_dekripsi.decode('utf-8')}")


def interaktif():
    print("\n=== MODE INTERAKTIF ===")
    plaintext = input("Masukkan plaintext : ")
    key = input("Masukkan key : ").encode("utf-8")
    data = plaintext.encode("utf-8")
    ciphertext = xor_bytes(data, key)
    print(f"ciphertext (hex) : {ciphertext.hex()}")
    print(f"dekripsi         : {xor_bytes(ciphertext, key).decode('utf-8')}")


if __name__ == "__main__":
    demo()
    interaktif()

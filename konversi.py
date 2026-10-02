"""02. Konversi Huruf <-> Angka
Alfabet dipetakan ke angka: A=0, B=1, C=2, ..., Z=25
"""

def huruf_ke_angka(huruf):
    """Mengubah satu huruf (A-Z, a-z) menjadi angka 0-25."""
    huruf = huruf.upper()
    if not ('A' <= huruf <= 'Z'):
        raise ValueError(f"'{huruf}' bukan huruf A-Z")
    return ord(huruf) - ord('A')


def angka_ke_huruf(angka):
    """Mengubah angka 0-25 menjadi huruf A-Z."""
    if not (0 <= angka <= 25):
        raise ValueError(f"{angka} di luar rentang 0-25")
    return chr(angka + ord('A'))


def demo():
    print("=== DEMO KONVERSI HURUF <-> ANGKA ===")
    for h in ['A', 'K', 'R', 'I', 'P', 'T', 'O', 'Z']:
        print(f"{h} -> {huruf_ke_angka(h)}")
    print()
    for a in [0, 10, 17, 8, 15, 19, 14, 25]:
        print(f"{a} -> {angka_ke_huruf(a)}")


def interaktif():
    print("\n=== MODE INTERAKTIF ===")
    pilihan = input("Konversi (1) huruf->angka atau (2) angka->huruf? ").strip()
    if pilihan == "1":
        h = input("Masukkan huruf : ")
        print(f"{h.upper()} -> {huruf_ke_angka(h)}")
    elif pilihan == "2":
        a = int(input("Masukkan angka (0-25) : "))
        print(f"{a} -> {angka_ke_huruf(a)}")
    else:
        print("Pilihan tidak dikenali.")


if __name__ == "__main__":
    demo()
    interaktif()

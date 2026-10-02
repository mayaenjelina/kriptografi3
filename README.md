# Praktikum Kriptografi - Pertemuan 3
Praktikkan konsep dengan Python: modulo, konversi huruf-angka, Caesar Cipher, dan XOR sederhana.

## Struktur Folder
```
praktikum3_kriptografi/
├── modulo.py           # 01. Operasi modulo
├── konversi.py         # 02. Konversi huruf <-> angka (A=0 ... Z=25)
├── caesar.py           # 03. Caesar Cipher dengan modulo
├── xor_cipher.py        # 04. XOR sederhana pada data biner
├── main.py             # Menjalankan semua demo + 3 pengujian Caesar & XOR
├── jawaban_analisis.md # Jawaban pertanyaan analisis
├── hasil_pengujian.txt # Output hasil menjalankan main.py
└── README.md
```

## Cara Menjalankan

**Mode otomatis (demo + 3 pengujian, tanpa perlu input apa pun):**
```
python main.py
```
Cocok untuk screenshot bukti pengujian karena langsung menampilkan semua
hasil tanpa menunggu kamu mengetik apa pun.

**Mode interaktif (boleh input plaintext/key sendiri):**
```
python caesar.py
python xor_cipher.py
python modulo.py
python konversi.py
```
Setiap file di atas akan menampilkan demo bawaan dulu, lalu meminta kamu
mengetik input sendiri (plaintext, key, dsb) di bagian "MODE INTERAKTIF".

## Deliverables
- [x] Source code (4 modul + main.py)
- [x] Screenshot hasil -> ambil screenshot sendiri saat menjalankan `python main.py`
- [x] 3 pengujian -> ada di main.py (pengujian_caesar & pengujian_xor)
- [x] Jawaban analisis -> jawaban_analisis.md
- [x] Kesimpulan singkat -> lihat di bagian bawah hasil_pengujian.txt

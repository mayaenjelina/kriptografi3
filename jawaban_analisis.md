# Jawaban Analisis

## 1. Mengapa operasi modulo diperlukan pada Caesar Cipher?

Alfabet A-Z hanya memiliki 26 huruf (angka 0 sampai 25). Ketika sebuah huruf
digeser dengan nilai kunci (key), hasil penjumlahannya bisa melebihi 25 atau
menjadi negatif (saat dekripsi). Contoh: huruf 'X' (23) digeser 5 menjadi
23 + 5 = 28, padahal angka valid untuk huruf hanya 0-25.

Operasi **modulo 26** membuat hasil tersebut "berputar balik" (wrap-around)
ke awal alfabet, seperti jarum jam yang kembali ke angka 1 setelah 12.
28 mod 26 = 2, yang berarti huruf hasilnya adalah 'C' (angka ke-2).
Tanpa modulo, program akan error atau menghasilkan karakter di luar A-Z saat
pergeseran melewati batas 'Z' (untuk enkripsi) atau batas 'A' (untuk dekripsi).

## 2. Mengapa XOR dapat dipakai untuk enkripsi dan dekripsi sekaligus?

XOR (exclusive OR) punya sifat matematis yang unik: jika suatu data di-XOR
dengan kunci yang sama sebanyak **dua kali**, hasilnya akan kembali ke data
asal. Secara notasi:

```
ciphertext = plaintext XOR key
plaintext  = ciphertext XOR key   (XOR kedua kali membatalkan XOR pertama)
```

Ini terjadi karena untuk setiap bit, X XOR K XOR K = X (meng-XOR dua kali
dengan nilai yang sama saling meniadakan, karena 0 XOR 0 = 0 dan 1 XOR 1 = 0).
Karena itu, **fungsi `xor_bytes()` yang sama** bisa dipanggil baik untuk
mengenkripsi maupun mendekripsi, cukup dengan kunci yang identik — tidak
perlu fungsi dekripsi terpisah seperti pada Caesar Cipher.

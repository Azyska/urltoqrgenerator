# URL to QR Code Generator 🚀

Proyek mandiri berbasis Python untuk mengubah tautan (URL) menjadi gambar QR Code secara langsung tanpa perantara pihak ketiga. 

Dibuat sebagai sarana eksplorasi pemrograman Python sekaligus menghadirkan utilitas lokal yang cepat, aman, dan bersih.

---

## 💡 Latar Belakang

Kebanyakan generator QR Code daring gratis sering kali menggunakan tautan *redirect* (pengalihan). Saat kode dipindai, pengguna diarahkan terlebih dahulu ke situs penyedia sebelum akhirnya menuju ke URL asli. Beberapa di antaranya bahkan menyisipkan pelacak, iklan, atau membatasi masa aktif QR Code.

Proyek ini dibangun secara independen agar:
- **Langsung ke Tujuan:** Data URL ditanamkan langsung ke dalam QR Code tanpa tautan perantara atau *redirect*.
- **Tanpa Batasan / Iklan:** Berjalan 100% secara lokal di komputer tanpa ketergantungan pada server pihak ketiga.
- **Bahan Belajar Python:** Memahami manipulasi string, struktur direktori/file di Linux, serta pemanfaatan modul Python eksternal (`qrcode` & `Pillow`).

---

## ✨ Fitur

- Otomatis menambahkan skema protokol `https://` jika pengguna lupa memasukkannya.
- Tingkat koreksi kesalahan tinggi (*High Error Correction* / `ERROR_CORRECT_H`), membuat QR Code tetap mudah dibaca meski gambar sedikit buram atau terpotong.
- Penyimpanan file otomatis dan rapi di dalam folder `output/`.

---

## 📁 Struktur Direktori

```text
qr-code-generator/
│
├── output/              # Folder tempat gambar QR Code (.png) disimpan
├── main.py              # Skrip utama pembuatan QR Code
├── requirements.txt     # Daftar dependensi modul
├── .gitignore           # File pengabaian Git
└── README.md            # Dokumentasi proyek
<div align="center">

# ⚡ Direct URL to QR Code Generator

A lightweight, zero-tracking, standalone Python tool to generate direct-link QR codes.

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-blue?style=flat-square)](#)

</div>

---

## 📌 Problem & Motivation

Banyak layanan pembuat QR code daring gratis memanfaatkan **redirect proxy links**. Ketika kode dipindai:
1. Pengguna dilempar ke domain perantara pihak ketiga terlebih dahulu.
2. Sering kali terdapat injeksi pelacak aktivitas, iklan, atau pembatasan masa aktif (*expiry date*).
3. Jika domain penyedia down atau gulung tikar, QR code yang sudah dicetak menjadi tidak dapat digunakan.

Proyek ini dibangun sebagai alat independen untuk memangkas dependensi tersebut. Data URL diinjeksikan secara langsung (**raw URL payload**) ke dalam matriks kode batang tanpa perantara, memastikan tautan bersifat permanen, aman, dan 100% berjalan di mesin lokal.

Proyek ini sekaligus menjadi media eksplorasi terstruktur mengenai sintaksis Python, manajemen *virtual environment*, manipulasi file I/O, serta pemanfaatan library pemrosesan citra.

---

## 🚀 Key Features

- **Direct Payload:** Tidak ada server perantara atau skema pengalihan URL.
- **Smart Protocol Normalizer:** Otomatis menambahkan prefix protokol `https://` jika input pengguna belum memilikinya.
- **High Error Correction (H Level):** Menggunakan koreksi kesalahan tingkat tinggi (~30% data dapat dipulihkan), menjaga keterbacaan kode meski cetakan sedikit kotor atau rusak.
- **Organized Storage:** Penyimpanan terisolasi secara otomatis di direktori `output/`.

---

## 🏗️ Directory Architecture

```text
urltoqrgenerator/
├── output/              # Direktori penyimpanan hasil render (.png)
├── .gitignore           # Filter Git untuk artefak cache & output
├── main.py              # Logika eksekusi utama CLI
├── README.md            # Dokumentasi proyek
└── requirements.txt     # Dependensi modul produksi
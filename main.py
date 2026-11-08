import os
import qrcode

def buat_qr(url_atau_teks, nama_file):
    # Memastikan folder output sudah ada
    os.makedirs("output", exist_ok=True)
    
    # Pengaturan konfigurasi QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Tingkat koreksi kesalahan tinggi
        box_size=10,
        border=4,
    )
    
    # Masukkan data
    qr.add_data(url_atau_teks)
    qr.make(fit=True)
    
    # Render gambar QR Code
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Simpan ke dalam folder output
    path_simpan = os.path.join("output", f"{nama_file}.png")
    img.save(path_simpan)
    
    print(f"\n[SUKSES] QR Code berhasil dibuat!")
    print(f"Lokasi file: {path_simpan}")

if __name__ == "__main__":
    print("=" * 40)
    print("      URL QR CODE GENERATOR      ")
    print("=" * 40)
    
    tautan = input("Masukkan URL/Link (contoh: https://google.com): ").strip()
    
    # Pastikan diawali skema web agar langsung bisa dibuka saat di-scan kamera HP
    if not tautan.startswith(("http://", "https://")):
        tautan = "https://" + tautan
        print(f"-> URL disesuaikan otomatis menjadi: {tautan}")
        
    nama = input("Masukkan nama file QR CODE (tanpa .png): ").strip()
    if not nama:
        nama = "qrcode_hasil"
        
    buat_qr(tautan, nama)
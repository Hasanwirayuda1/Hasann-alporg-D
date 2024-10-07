# Cara Bikin Nasi Goreng Ala Algoritma

## Deskripsi

Ini adalah algoritma yang ngejelasin gimana cara bikin nasi goreng yang simpel tapi enak. Prosesnya mulai dari siapin bahan, goreng bumbu, masukin nasi, tambahin topping, dan akhirnya siap disajikan. Algoritma ini bakal ngajarin kamu langkah-langkahnya biar bikin nasi goreng jadi gampang.

## Langkah-langkah Algoritma

1. **Siapin bahan**: Pastikan bahan-bahan kayak nasi sama bumbu udah ada. Kalau mau lebih enak, siapin juga topping kayak telur, ayam, atau sayur.
2. **Goreng bumbu**: Panasin minyak, terus tumis bumbu sampe harum.
3. **Masukin nasi**: Kalau bumbunya udah mateng, masukin nasi dan aduk-aduk biar nyatu sama bumbunya.
4. **Tambahin topping**: Kalau suka, tambahin telur, ayam, atau sayur ke nasi gorengnya biar makin mantap.
5. **Sajikan**: Kalau udah mateng, nasi goreng siap dimakan! Selamat makan!

##Contoh Kode

def buat_nasi_goreng(bahan):
    if 'nasi' not in bahan or 'bumbu' not in bahan:
        return "Gagal bikin nasi goreng: Nasi atau bumbu nggak ada!"
    
    print("Goreng bumbu dulu... Harum banget cok!")
    print("Masukin nasi ke wajan, aduk-aduk biar rata.")
    
    if 'telur' in bahan:
        print("Masukin telur biar makin mantap.")
    if 'ayam' in bahan:
        print("Tambahin ayam buat lebih gurih.")
    if 'sayuran' in bahan:
        print("Tambahin sayuran biar sehat.")
    
    return "Nasi goreng siap! Gass makan!"

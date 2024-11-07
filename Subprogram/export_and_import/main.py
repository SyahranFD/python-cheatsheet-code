import hello

persegi_panjang_pertama = hello.mencari_luas_persegi_panjang(5,10)
print(persegi_panjang_pertama)
print(hello.nama)

# contoh jika spesifik import
from hello import mencari_luas_persegi_panjang, nama

persegi_panjang_pertama = mencari_luas_persegi_panjang(5,10)
print(persegi_panjang_pertama)

print(nama)
ketersediaan = "Daging sapi"

if ketersediaan == "Daging ayam":
    print("Ibu membeli dan memasak ayam")
elif ketersediaan == "Daging sapi":
    print("Ibu membeli dan memasak sapi")
else:
    print("Ibu membeli dan memasak tempe")


# one line if statement
score = 100

if score == 100: print("Nilai Anda sempurna!")


# contoh lain
nilai = 65

if nilai >= 80:
    print("Selamat! And mendapat niali A")
    print("Pertahankan!")
elif nilai >= 70:
    print("Hore! Anda mendapat nilai B")
    print("Tingkatkan!")
elif nilai >= 60:
    print("Hmm. Anda mendapat nilai C")
    print("Ayo semangat!")
else:
   print("Waduh, Anda mendapat nilai D")
   print("Yuk belajar lebih giat lagi!")


# contoh 2 kondisi
nilai = 81
perilaku = 'tidak baik'

if nilai>=80 and perilaku == 'baik':
   print("Selamat! Anda mendapat nilai A dan telah berkelakuan baik")
   print("Pertahankan!")
elif nilai>=80 and perilaku != 'baik':
   print("Kamu mendapatkan nilai A, tetapi perilaku Anda kurang baik")
   print("Perbaiki lagi ya!")
else:
   print("Yuk belajar lebih giat lagi!")
kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort()

print(kendaraan) # ['helikopter', 'mobil', 'motor', 'pesawat']


# reverse sort
kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort(reverse=True)

print(kendaraan) # ['pesawat', 'motor', 'mobil', 'helikopter']


# huruf kapital lebih dulu
kendaraan = ['motor', 'mobil', 'helikopter', 'Pesawat']
kendaraan.sort()

print(kendaraan) # ['Pesawat', 'helikopter', 'mobil', 'motor']


# dibuat lowercase terlebih dahulu agar bisa diurutkan dengan benar
kendaraan = ['motor', 'mobil', 'helikopter', 'Pesawat']
kendaraan.sort(key=str.lower)

print(kendaraan) # ['helikopter', 'mobil', 'motor', 'Pesawat']

# berdasarkan panjang karakter
kendaraan = ['motor', 'mobil', 'helikopter', 'Pesawat']
kendaraan.sort(key=len)

print(kendaraan) # ['motor', 'mobil', 'Pesawat', 'helikopter']


# berdasarkan tahun
def myFunc(e):
    return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

cars.sort(key=myFunc)

print(cars) # [{'car': 'Mitsubishi', 'year': 2000}, {'car': 'Ford', 'year': 2005}, {'car': 'VW', 'year': 2011}, {'car': 'BMW', 'year': 2019}]   
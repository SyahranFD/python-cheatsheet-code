teks = 'Code'
tambah_number = teks.zfill(5)
print(tambah_number) # Output: 0Code, 
'''
karena panjang karakter seharusnya 5, 
tetapi panjang karakter teks hanya 4, 
jadi ditambahkan 0 di depan teks agar panjang karakternya menjadi 5
'''

print('Dicoding'.rjust(20)) # Output: '            Dicoding'

print('Dicoding'.rjust(20, '!')) # Output: '!!!!!!!!!!!!Dicoding'

print('Dicoding'.ljust(20)) # Output: 'Dicoding            '

print('Dicoding'.center(20, '-')) # Output: '-----Dicoding------'
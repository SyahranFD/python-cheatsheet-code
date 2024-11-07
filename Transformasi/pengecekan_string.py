kata = 'DICODING'
print(kata.isupper()) # True

kata = 'dicoding'
print(kata.islower()) # True

kata = 'dicoding'
print(kata.isalpha()) # True, karena semua huruf alphabet

kata = 'dicoding123'
print(kata.isalnum()) # True, karena semua karakter adalah huruf atau angka

print('123'.isdecimal()) # True, karena semua karakter adalah angka

print('         '.isspace()) # True, karena semua karakter adalah whitespace

print('Dicoding Indonesia'.istitle()) # True, karena setiap kata dimulai dengan huruf besar
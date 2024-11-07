x = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }

print(type(x)) # <class 'dict'>

print(x ['age']) # 20

# Menambahkan data baru ke dalam dictionary
x = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }
x ['Job'] = "Web Developer"
x ['Life'] = "Happy Life"

print(x) # {'name': 'Perseus Evans', 'age': 20, 'isMarried': False, 'Job': 'Web Developer', 'Life': 'Happy Life'}
print(x ['Life']) # Happy Life


# Menghapus data dari dictionary
x = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }
del x['age']

print(x) # {'name': 'Perseus Evans', 'isMarried': False}


# Mengubah nilai elemen dictionary
x = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }
x['name'] = 'Dicoding'

print(x) # {'name': 'Evans Perseus', 'age': 20, 'isMarried': False}
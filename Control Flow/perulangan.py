# perulangan for list
var_list = [1,2,3,4,5,6,7,8,9,10]
for i in var_list:
    print(i)

# perulangan for berdasarkan panjang suatu nilai
for i in range(1, 10, 2):
    print(i)

# perulangan while
counter = 1
while counter <= 5:
    print(counter)
    counter +=1

# perulangan for bersarang (nested loop)
for i in range(1, 3):
    for j in range(1, 3):
        print(i, j)

# perulangan break
for i in range(2):
    print("Perulangan luar : ", i)
    for j in range(10):
        print("Perulangan dalam : ", j)
        if j == 1:
            break

# perulangan break string
for huruf in "Dico ding":
    if huruf == " ":
        break
    print("Huruf saat ini: {}".format(huruf))

# perulangan continue
for huruf in "Dico ding":
    if huruf == " ":
        continue
    print(f"Huruf saat ini: {huruf}")

# else setelah for
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 6:
        print("Angka ditemukan! Program berhenti!")
        break
else:
    print("Angka tidak ditemukan!")

# else setelah while
count = 0

while count < 3:
    print("Dicoding Indonesia")
    count += 1
else:
    print("Blok else dieksekusi karena kondisi pada while salah (3<3 == False).")

# pass
x = 10

if x > 5:
    pass
else: 
    print("Nilai x tidak memenuhi kondisi")

# list comprehension
angka = [1, 2, 3, 4]
pangkat = [n**2 for n in angka]
print(pangkat)
# Positional-or-Keyword (default)
def greeting(nama, pesan):
    return "Halo, " + nama + "! " + pesan

print(greeting("Dicoding", "Selamat pagi!"))
print(greeting(pesan="Selamat sore!", nama="Dicoding"))


# Positional-Only
def penjumlahan(a, b, /):
    return a + b

print(penjumlahan(8, 50))


# Keyword-Only
def greeting(*, nama, pesan):
    return "Halo, " + nama + "! " + pesan

print(greeting(pesan="Selamat sore!",nama="Dicoding"))


# Var-Positional (Variadic Positional Parameter) 
def hitung_total(*args): # tuple
    print(type(args))
    total = sum(args)
    return total

print(hitung_total(1, 2, 3))


# Var-Keyword (Variadic Keyword Parameter)
def cetak_info(**kwargs): # dictionary
    info = ""
    for key, value in kwargs.items():
        info += key + ': ' + value + ", "
    return info

print(cetak_info(nama="Dicoding", usia="17", pekerjaan="Python Programmer"))
# Perhatikan penggunaan spasi dari kedua kode berikut.

Yes:
def munge(input: str):  # Menambahkan informasi parameter bertipe string
    pass
def munge() -> str:   # Menambahkan informasi return value bertipe string
    pass

No:
def munge(input:str):  # Menambahkan informasi parameter bertipe string
    pass
def munge()->str:   # Menambahkan informasi return value bertipe string
    pass


Yes:
def LuasPersegiPanjang(panjang=2, lebar=None):
    luas = panjang*lebar
    return luas

No:
def LuasPersegiPanjang(panjang = 2, lebar = None):
    luas = panjang*lebar
    return luas


Yes:
def LuasPersegiPanjang(panjang:int = 2, lebar=None):
    pass

No:
def LuasPersegiPanjang(panjang: int=2, lebar = None):
    pass
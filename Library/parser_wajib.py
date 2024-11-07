import argparse
from datetime import datetime, date

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--nama', required=True, help="Masukkan Nama Anda")
parser.add_argument('-t', '--tanggallahir', required=True, help="Masukkan Tanggal Lahir Anda (DD-MM-YYYY)")
args = parser.parse_args()

# Konversi string tanggal lahir menjadi objek tanggal
tanggal_lahir = datetime.strptime(args.tanggallahir, "%d-%m-%Y").date()

# Hitung umur
umur = date.today().year - tanggal_lahir.year - ((date.today().month, date.today().day) < (tanggal_lahir.month, tanggal_lahir.day))

panggilan = "bapak "

if umur <= 30:
    panggilan = "kakak "

print("Terima kasih telah menggunakan panggildicoding.py, "+ panggilan + args.nama)


# ketik python Library/parser_wajib.py -n
# ketik python Library/parser_wajib.py --nama
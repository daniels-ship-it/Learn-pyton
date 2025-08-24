import random

huruf_kecil = "abcdefghijklmnopkrstuvwxyz"
huruf_besar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
angka = "0123456789"
huruf_unik = "@#_&-+!?%"

semua = huruf_kecil + huruf_besar + angka + huruf_unik

kata_acak = ''.join(random.sample(semua,12))

print(f"inilah : {kata_acak} ")
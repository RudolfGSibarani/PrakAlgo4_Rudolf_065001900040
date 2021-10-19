# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 23:07:03 2021

@author: Rudolf
"""

masuk = list(map(int, input("Masukkan list angka (integer): ").strip().split()))
panjang = len(masuk)

genap = 0

for angka in masuk:
    if angka % 2 == 0:
        genap += 1

if genap > 0:
    print("List angka memiliki angka yang genap")
else:
    print("List angka tidak memiliki angka yang genap")
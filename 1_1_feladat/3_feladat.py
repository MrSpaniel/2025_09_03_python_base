"""Készíts egy programot! A gép "gondol" egy számra 1 és 5 között, vagyis egy változóban tárolj egy ilyen számot! Azután a program bekér egy számot a felhasználótól, majd kiírja, hogy ez a szám egyenlő-e a gép által "gondolt" számmal, vagy annál kisebb, illetve nagyobb."""

import random

gondolt_szam = random.randint(1, 5)
tipp = int(input('Gondoltam egy számra 1 és 5 között. Tippelj: '))

if tipp == gondolt_szam:
    print('Eltaláltad!')
elif tipp < gondolt_szam:
    print('A tipped kisebb, mint a gondolt szám.')
else:
    print('A tipped nagyobb, mint a gondolt szám.')
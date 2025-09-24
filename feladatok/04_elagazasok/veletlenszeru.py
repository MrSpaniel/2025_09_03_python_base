"""Készíts egy rövid programot, amely 1 és 3 között generál véletlenszámot, majd összehasonlítja ezt a felhasználó által megadott, szintén ebbe a tartományba eső számmal! Az összehasonlítás eredményéről tájékoztassa a felhasználót!
"""


import random

gondolt_szam = random.randint(1, 3)
tipp = int(input('Gondoltam egy számra 1 és 3 között. Tippelj: '))

if tipp == gondolt_szam:
    print('Eltaláltad!')
elif tipp < gondolt_szam:
    print('A tipped kisebb, mint a gondolt szám.')
else:
    print('A tipped nagyobb, mint a gondolt szám.')
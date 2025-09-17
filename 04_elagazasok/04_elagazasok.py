"""Pozitiv negativ szamok kimutatasa"""


# szam = int(input('Adj meg egy számot!'))

# if szam < 0:
#     print('Ez a szám negatív!')

# elif szam > 0:
#     print('Ez a szám pozitív!')

# else:
#     print('Ez a szám Nulla!')

"""Paros paratlan szamok kimutatasa"""

szam = int(input('Kérlek adj meg egy számot:'))

if szam % 2 == 0 and szam != 0 :
    print('Ez a szám páros')
elif szam == 0 :
    print('Nulla')
else :
    print('Ez a szám páratlan')
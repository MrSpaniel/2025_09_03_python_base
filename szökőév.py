"""Kérj be egy évet, és írd ki, hogy szökőév-e.
 (Szökőév, ha osztható 4-gyel, de nem 100-zal, kivéve ha 400-zal is osztható.)
"""

evszam = int(input('Adj meg egy évszámot!'))

if evszam % 4 == 0 and (evszam % 100 != 0 or evszam % 400 == 0):
    print(f'{evszam} szökőév!')
else:
    print(f'{evszam} nem szökőév!')
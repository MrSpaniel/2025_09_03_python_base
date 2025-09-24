"""Kérj be egy pontszámot 0–100 között, és írd ki az érdemjegyet:
0–49: Elégtelen


50–64: Elégséges


65–79: Közepes


80–89: Jó


90–100: Jeles
"""

pontszam = float(input('Írd be a pontszámodat!'))
if pontszam >= 90:
    print('Jeles')
elif pontszam >= 80:
    print('Jó')
elif pontszam >= 65:
    print('Közepes')
elif pontszam >= 50:
    print('Eléséges')
elif pontszam >=0:
    print('Elégtelen')
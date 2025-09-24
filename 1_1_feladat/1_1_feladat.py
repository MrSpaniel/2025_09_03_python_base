"""valasz = input('Jó napod van? (igen/nem): ').strip().lower()

if valasz == 'igen':
    print('Örülök, hogy jó napod van!')
elif valasz == 'nem':
    print('Sajnálom, hogy nem jó a napod.')
else:
    print('Csak "igen" vagy "nem" választ adhatsz meg.')"""

valasz = input('Jó napod van? (igen/nem): ')

if valasz == 'igen':
    print('Örülök, hogy jó napod van!')
elif valasz == 'nem':
    print('Sajnálom, hogy rossz a napod.')
else:
    print('Sajnálom, nem értem a válaszodat!')

    """Fejleszd tovább az első feladat programját úgy, hogy amennyiben a felhasználó nem a két lehetséges válasz (igen/nem) közül ad meg egyet, a gép kiírja: "Sajnos nem értem a válaszodat!"
"""
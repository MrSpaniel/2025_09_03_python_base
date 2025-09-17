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
    print('Csak "igen" vagy "nem" választ adhatsz meg.')
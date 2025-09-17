# """Kérj be három egész számot, és írd ki, melyik a legnagyobb."""

# egyszam = float(input('Adj meg egy számot!'))
# ketszam = float(input('Adj meg egy számot!'))
# haromszam = float(input('Adj meg egy számot!'))

# if egyszam >= ketszam and egyszam >= haromszam:
#     print(f'A legnagyobb szám: {egyszam}')
# elif ketszam >= egyszam and ketszam >= haromszam:
#     print(f'A legnagyobb szám: {ketszam}')
# elif haromszam >= egyszam and haromszam >= ketszam:
#     print(f'A legnagyobb szám: {haromszam}')


egyszam = float(input('Adj meg egy számot!'))
ketszam = float(input('Adj meg egy számot!'))
haromszam = float(input('Adj meg egy számot!'))

legnagyobb = max(egyszam, ketszam, haromszam)
print(f'A legnagyobb szám: {legnagyobb}')
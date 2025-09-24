"""A csoport:
Készítsünk programot, amely labdák csomagolásához végez számításokat.
A labdákat szalaggal kell átkötni úgy, hogy kétszer körbe érje őket, és a masni készítéséhez számolunk még 60 cm-t.
A labda körül a szalag egy kör (kerület képlete 2*r*PI)
A program kérje be a labda átmérőjét, a labdák számát, és a rendelkezésre álló szalag hosszát!
Számítsa ki, és írja a képernyőre, hogy a bekért számú labda csomagolásához hány centiméter szalagra van szükség, valamint állapítsa meg,
hogy elegendő szalagunk van-e a művelet elvégzéséhez, és ezt is közölje a felhasználóval!"""

szalaghossz = float(input("Adja meg az önnél lévő szalag hosszát cm-ben:"))
atmero = float(input("Adja meg a labda átmérőjét cm-ben:"))
PI = 3.14
Kerulet = 2*(2* atmero * PI) + 60
if Kerulet <= szalaghossz print("Az önnél lévő szalag elegendő a labdához!")
else print("Az önnél lévő szalag nem elegendő!")

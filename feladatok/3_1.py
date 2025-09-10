"""Thonny fejlesztői környezetben készíts egy rövid programot, amely
kommentként tartalmazza a program funkciójának leírását,
konstansként tárolja PI értékét,
egy másik változóban tárolja egy kör sugarának nagyságát (cm-ben megadva),
kiszámolja és a képernyőre kiírja a kör kerületét és területét!"""

PI = 3.14
print("Írd le a kör sugarát:")
radius = int(input())
Kerulet = 2 * radius * PI
Terulet = radius * radius * PI
print(f"Kerület: {Kerulet} cm")
print(f"Terület: {Terulet} cm²")
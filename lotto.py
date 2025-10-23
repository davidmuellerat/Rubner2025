import random

def lottoziehung():
    zahlen = []
    while len(zahlen) < 6:
        zahl = random.randint(1, 45)
        if zahl not in zahlen:
            zahlen.append(zahl)
    return sorted(zahlen)

def statistik():
    stats = {i: 0 for i in range(1, 46)}
    for _ in range(1000000):
        gezogene = lottoziehung()
        for z in gezogene:
            stats[z] += 1
    return stats

print("Gezogene Lottozahlen:", lottoziehung())
print("\nStatistik nach 1000 Ziehungen:")
ergebnis = statistik()
for zahl in sorted(ergebnis.keys()):
    print(f"Zahl {zahl:2d}: {ergebnis[zahl]} mal")

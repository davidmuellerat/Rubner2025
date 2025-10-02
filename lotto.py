import random


def lottoziehung():
    zahlen = list(range(1, 46))
    random.shuffle(zahlen)
    return zahlen[:6]


def statistik(anzahl_ziehungen=1000):
    stats = {i: 0 for i in range(1, 46)}

    for _ in range(anzahl_ziehungen):
        gezogene = lottoziehung()
        for zahl in gezogene:
            stats[zahl] += 1

    return stats


print("Eine Ziehung:", lottoziehung())

ergebnis = statistik(1000)
print("\nStatistik nach 1000 Ziehungen:")
for zahl, haeufigkeit in sorted(ergebnis.items()):
    print(f"{zahl:2d}: {haeufigkeit}")
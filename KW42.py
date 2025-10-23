liste = ["a","b","b","c"]

simuliertes_set = [x for i, x in enumerate(liste) if x not in liste[:i]]

print(simuliertes_set)

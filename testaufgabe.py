# schreib eine methode die aus einer liste die
# kombinationen von 2 zahlen raussucht, die auf eine bestimmte summe enden,
# liste von den kombinationen als retour

def find_combination(numbers, sum):
    paare = []
    for a in numbers:
        if sum - a in numbers:
            paar_single = []
            paar_single.append((a, sum - a))
            paare.append(paar_single)
    return paare


numbers = [1, 2, 3, 4, 5, 6]
lum = 10
pairs = find_combination(numbers, lum)
print(pairs)
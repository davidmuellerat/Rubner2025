# List C
#gerade Zahlen verdoppeln
numbers = [1, 2, 3, 4, 5, 6]
even_doubled = [x * 2 for x in numbers if x % 2 == 0]
print(even_doubled)

# 2. Set C
#buchstaben aus wort extrahieren
word = "bananenbrot"
unique_letters = {letter for letter in word}
print(unique_letters)

# Dict C mit if else
words = ["Apfel", "Ei", "Banane", "Obst"]
length_info = {w: "lang" if len(w) > 3 else "kurz" for w in words}
print(length_info)

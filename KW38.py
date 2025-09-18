def main():
    # 1) if / elif / else
    note = 85
    if note >= 90:
        print("Sehr gut")
    elif note >= 75:
        print("Gut")
    else:
        print("Verbesserung nötig")

    print("-" * 40)

    # 2) for-Schleife
    for zahl in range(1, 6):
        print("Zahl:", zahl)

    print("-" * 40)

    # 3) while-Schleife mit break + continue
    i = 0
    while i < 10:
        i += 1
        if i == 3:
            continue
        if i == 7:
            break
        print("i =", i)

    print("-" * 40)

    # 4) pass-Beispiel
    for buchstabe in "Python":
        if buchstabe == "h":
            pass  #macht nix
        else:
            print("Buchstabe:", buchstabe)

    print("-" * 40)

    # 5) try-except-else-finally
    try:
        zahl = int(input("Gib eine Zahl ein: "))
        ergebnis = 10 / zahl
    except ValueError:
        print("Fehler: Bitte eine gültige Zahl eingeben.")
    except ZeroDivisionError:
        print("Fehler: Division durch Null.")
    else:
        print("Ergebnis =", ergebnis)
    finally:
        print("Programm beendet")


if __name__ == "__main__":
    main()

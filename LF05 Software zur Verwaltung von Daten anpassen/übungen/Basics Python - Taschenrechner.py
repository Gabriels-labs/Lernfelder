def taschenrechner():
    # Eingabe
    zahl1 = float(input("Gib die erste Zahl ein: "))
    operator = input("Wähle eine Operation (+, -, *, /): ")
    zahl2 = float(input("Gib die zweite Zahl ein: "))

    # Berechnung
    if operator == "+":
        ergebnis = zahl1 + zahl2
    elif operator == "-":
        ergebnis = zahl1 - zahl2
    elif operator == "*":
        ergebnis = zahl1 * zahl2
    elif operator == "/":
        if zahl2 == 0:
            print("Fehler: Division durch 0 ist unzulässig!")
            return
        ergebnis = zahl1 / zahl2
    else:
        print("Ungültiger Operator!")
        return

    # Ausgabe
    print("Ergebnis:", ergebnis)

    # Programm starten
taschenrechner()

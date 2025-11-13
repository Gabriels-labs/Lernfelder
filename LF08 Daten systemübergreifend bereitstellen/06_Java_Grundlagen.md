# Java – Geschichte & Grundlagen

## 1. Kurzgeschichte von Java
Java wurde Anfang der 1990er Jahre bei Sun Microsystems entwickelt und 1995 veröffentlicht.  
Die Kernidee lautet: **„Write once, run anywhere“**, was durch die Java Virtual Machine (JVM) ermöglicht wird.  
Heute wird Java von Oracle und der OpenJDK-Community weiterentwickelt.

---

## 2. Grundstruktur eines Java-Programms
Ein Java-Programm besteht aus Klassen. Die `main`-Methode bildet den Einstiegspunkt.  
Geschweifte Klammern strukturieren den Code, Kommentare erklären Abläufe und werden nicht ausgeführt.

Beispiel:

    public class Main {
        public static void main(String[] args) {
            System.out.println("Hallo Welt!");
        }
    }

---

## 3. Datentypen und Variablen

### Grundtypen
- **int** – Ganzzahlen  
- **double** – Dezimalzahlen (mit `.` als Trennzeichen)  
- **String** – Text  
- **boolean** – true / false  

Deklaration & Initialisierung:

    int zahl = 10;
    String name = "Anna";
    boolean aktiv = true;

---

## 4. Operatoren & Logik

### Arithmetische Operatoren
"+"  Addition  
"-"  Subtraktion  
"*"  Multiplikation  
"/"  Division  
"%"  Modulo (Restwert)

    int rest = 7 % 3;   // ergibt 1

### Zuweisungsoperatoren
=, +=, -=, *=, /=

    int x = 5;
    x += 3;   // x = 8

### Inkrement / Dekrement
++ erhöht um 1  
-- verringert um 1

### Vergleichsoperatoren
==, !=, >, <, >=, <=

### Logische Operatoren
&&  UND  
||  ODER  
!   NICHT

Beispiele:

    true && false    // false
    !true            // false
    3 == 3           // true

---

## 5. Verzweigungen (if/else)

Einfaches Beispiel:

    int alter = 17;

    if (alter >= 18) {
        System.out.println("Volljährig");
    } else {
        System.out.println("Minderjährig");
    }

Mehrere Bedingungen:

    if (punkte >= 90) {
        System.out.println("Sehr gut");
    } else if (punkte >= 75) {
        System.out.println("Gut");
    } else {
        System.out.println("Verbesserungsbedarf");
    }

---

## 6. Schleifen

### for-Schleife

    for (int i = 0; i < 5; i++) {
        System.out.println(i);
    }

### while-Schleife

    int n = 3;
    while (n > 0) {
        System.out.println(n);
        n--;
    }

### do-while

    int z = 0;
    do {
        System.out.println("Mindestens einmal!");
        z++;
    } while (z < 1);

### for-each (typisch für Arrays)

    String[] namen = {"Tom", "Lisa", "Mark"};

    for (String n : namen) {
        System.out.println(n);
    }

---

## 7. Arrays

### Deklaration

    int[] zahlen = new int[3];   // {0, 0, 0}

### Direkte Initialisierung

    int[] werte = {5, 10, 15};

### Zugriff

    werte[0]         // erstes Element
    werte.length     // Anzahl der Elemente

---

## Fazit
Dieses Kapitel vermittelt die Basis der Java-Programmierung: Aufbau eines Programms, Datentypen, Operatoren, Bedingungen, Schleifen und Arrays. Diese Grundlagen bilden das Fundament für objektorientierte Konzepte wie Klassen, Objekte und Methoden, die anschließend folgen.

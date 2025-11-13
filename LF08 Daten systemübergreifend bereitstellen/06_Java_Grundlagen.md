# Java – Geschichte & Grundlagen

## 1. Kurzgeschichte von Java
Java wurde Anfang der 1990er von Sun Microsystems entwickelt und 1995 offiziell vorgestellt.
Zentrale Idee: **„Write once, run anywhere“** – dank der Java Virtual Machine (JVM).
Heute wird Java durch Oracle und OpenJDK weiterentwickelt.


## 2. Grundstruktur eines Java-Programms
Jedes Java-Programm besteht aus Klassen.  
Die `main`-Methode ist der Einstiegspunkt.  
Geschweifte Klammern strukturieren den Code.  
Kommentare dienen der Erklärung und werden nicht ausgeführt.

// Beispielprogramm:
public class Main {
    public static void main(String[] args) {
        System.out.println("Hallo Welt!");
    }
}


## 3. Datentypen und Variablen

### Grundtypen
- int       → ganze Zahlen  
- double    → Kommazahlen (Punkt als Trennzeichen)  
- String    → Text  
- boolean   → true / false  

// Beispiele:
int zahl = 10;
String name = "Anna";
boolean aktiv = true;


## 4. Operatoren & Logik

### Arithmetische Operatoren
+   Addition  
-   Subtraktion  
*   Multiplikation  
/   Division  
%   Modulo (Rest)

// Beispiel:
int rest = 7 % 3;     // ergibt 1

### Zuweisungsoperatoren
=    einfache Zuweisung  
+=   Addition & Zuweisung  
-=   Subtraktion & Zuweisung  
*=   Multiplikation & Zuweisung  
/=   Division & Zuweisung

// Beispiel:
int x = 5;
x += 3;   // x = 8

### Inkrement / Dekrement
++   erhöht um 1  
--   verringert um 1

### Vergleichsoperatoren
==   gleich  
!=   ungleich  
>    größer  
<    kleiner  
>=   größer gleich  
<=   kleiner gleich  

### Logische Operatoren
&&   UND  
||   ODER  
!    NICHT

// Beispiele:
true && false    // false
!true            // false
3 == 3           // true


## 5. Verzweigungen (if/else)

// Beispiel:
int alter = 17;

if (alter >= 18) {
    System.out.println("Volljährig");
} else {
    System.out.println("Minderjährig");
}

// Mehrere Bedingungen:
if (punkte >= 90) {
    System.out.println("Sehr gut");
} else if (punkte >= 75) {
    System.out.println("Gut");
} else {
    System.out.println("Verbesserungsbedarf");
}


## 6. Schleifen

### for-Schleife (klassische Zählschleife)
for (int i = 0; i < 5; i++) {
    System.out.println(i);
}

### while-Schleife (kopfgesteuert)
int n = 3;
while (n > 0) {
    System.out.println(n);
    n--;
}

### do-while (mindestens ein Durchlauf)
int z = 0;
do {
    System.out.println("Mindestens einmal!");
    z++;
} while (z < 1);

### for-each (für Arrays oder Listen)
String[] namen = {"Tom", "Lisa", "Mark"};

for (String n : namen) {
    System.out.println(n);
}


## 7. Arrays

### Deklaration
int[] zahlen = new int[3];    // {0, 0, 0}

### Direkte Initialisierung
int[] werte = {5, 10, 15};

### Zugriff
werte[0]         // erstes Element  
werte.length     // Anzahl der Elemente


## Fazit
Dieses Kapitel vermittelt die Grundlagen der Java-Programmierung:
Programmausführung, Datentypen, Operatoren, Bedingungen, Schleifen und Arrays.
Damit entsteht ein stabiles Fundament für die objektorientierte Programmierung
(Klassen, Objekte, Methoden), die in späteren Kapiteln folgt.

# Java – Geschichte & Grundlagen

## 1. Kurzgeschichte von Java
Java entstand Anfang der 1990er Jahre bei Sun Microsystems. 1995 wurde es erstmals öffentlich vorgestellt. Die zentrale Idee lautet: „Write once, run anywhere“ – also Programme auf verschiedensten Systemen ausführen, ohne sie anzupassen. Dies gelingt durch die Java Virtual Machine (JVM). Heute wird Java von Oracle und der OpenJDK-Community weiterentwickelt.

---

## 2. Grundstruktur eines Java-Programms
Ein Java-Programm besteht aus Klassen. Die main-Methode ist der Startpunkt einer Anwendung. Geschweifte Klammern strukturieren den Code. Kommentare (`//` oder `/* ... */`) werden nicht ausgeführt und dienen nur der Erklärung.

Ein typisches Grundgerüst:
public class Main {
    public static void main(String[] args) {
        System.out.println("Hallo Welt!");
    }
}

---

## 3. Datentypen und Variablen

### Grundtypen
- int – ganze Zahlen  
- double – Kommazahlen (mit Punkt als Trennzeichen)  
- String – Text  
- boolean – true/false  

Variablen können getrennt deklariert und initialisiert oder direkt zusammen angelegt werden.

Beispiele:
int zahl = 10;
String name = "Anna";
boolean aktiv = true;

---

## 4. Operatoren & Logik

### Arithmetische Operatoren
+  -  *  /  %

Beispiel:
int rest = 7 % 3;   // ergibt 1

### Zuweisungsoperatoren
=   +=   -=   *=   /=

Beispiel:
int x = 5;
x += 3;  // x wird zu 8

### Inkrement & Dekrement
++  --  

### Vergleichs- & Logikoperatoren
==   !=   &&   ||   !

Beispiele:
true && false     // false
!true             // false
3 == 3            // true

---

## 5. Verzweigungen (if/else)

Verzweigungen steuern den Programmablauf abhängig von Bedingungen.

Beispiel:
int alter = 17;

if (alter >= 18) {
    System.out.println("Volljährig");
} else {
    System.out.println("Minderjährig");
}

Mit mehreren Bedingungen:
if (score >= 90) {
    System.out.println("Sehr gut");
} else if (score >= 75) {
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

Arrays speichern mehrere Werte desselben Typs in fester Größe.

Deklaration:
int[] zahlen = new int[3];   // {0, 0, 0}

Direkte Initialisierung:
int[] werte = {5, 10, 15};

Zugriff:
werte[0]        // erstes Element
werte.length    // Anzahl der Elemente

---

## Fazit
Dieses Kapitel vermittelt die zentralen Grundlagen der Java-Programmierung: Aufbau eines Programms, grundlegende Datentypen, Operatoren, Verzweigungen, Schleifen und Arrays. Damit entsteht ein stabiles Fundament für die objektorientierte Programmierung, Klassen, Methoden, Objekte und alle weiteren Java-Konzepte.

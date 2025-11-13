# Java – Objektorientierte Programmierung (OOP)

OOP modelliert Software anhand realer Objekte. Klassen beschreiben Aufbau und Verhalten, Objekte sind konkrete Instanzen dieser Klassen. Ziel ist klare Struktur, Wiederverwendbarkeit und leichte Erweiterbarkeit von Code.

---

## 1. Klassen & Objekte

Eine Klasse ist eine Blaupause.  
Objekte sind konkrete Exemplare dieser Blaupause.

Beispiel:

    public class Auto {
        String farbe;
        int baujahr;
    }

Objekt erzeugen:

    Auto a = new Auto();
    a.farbe = "Schwarz";

Bestandteile einer Klasse:
- Attribute → Zustand  
- Methoden → Verhalten  
- Konstruktoren → Erzeugung der Objekte  

---

## 2. Attribute

Attribute definieren Eigenschaften eines Objekts.

    public class Auto {
        String marke;
        int leistung;
    }

Werte können direkt zugewiesen werden:

    Auto b = new Auto();
    b.leistung = 150;

---

## 3. Methoden

Methoden beschreiben das Verhalten eines Objekts.

Aufbau:

    Rueckgabetyp name(Parameter) {
        // Anweisungen
    }

Beispiel:

    public int verdoppeln(int x) {
        return x * 2;
    }

Wichtig:
- Methoden können Werte zurückgeben (alles außer void)  
- Parameter sind Platzhalter für Eingaben  
- Methoden bieten Struktur, Wiederverwendbarkeit und Kapselung  

Scope:
Variablen in Methoden gelten nur innerhalb der Methode.

---

## 4. Getter & Setter (Encapsulation)

Encapsulation bedeutet: Attribute schützen, Zugriff kontrollieren.

Attribute privat machen:

    private String name;

Öffentliche Getter/Setter bereitstellen:

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

Nutzen:
- Schutz vor falschen Werten  
- Validierung möglich  
- Implementierung später änderbar  

---

## 5. Konstruktoren

Ein Konstruktor wird beim Erzeugen des Objekts ausgeführt.  
Name = Klassenname, kein Rückgabewert.

Beispiel:

    public class Auto {
        String marke;
        int ps;

        public Auto(String marke, int ps) {
            this.marke = marke;
            this.ps = ps;
        }
    }

Objekt erzeugen:

    Auto audi = new Auto("Audi", 190);

### Default-Konstruktor
Java erzeugt ihn automatisch, wenn man keinen eigenen definiert.

    public class Person { }

### Konstruktorüberladung
Mehrere Konstruktoren mit unterschiedlichen Parametern:

    public Auto() {
        this("Unbekannt", 0);
    }

    public Auto(String marke, int ps) {
        this.marke = marke;
        this.ps = ps;
    }

---

## 6. Vererbung (Inheritance)

Vererbung beschreibt eine **"ist-ein"** Beziehung.

    class Tier { }
    class Vogel extends Tier { }
    class Papagei extends Vogel { }

Regeln:
- Subklassen erben Attribute & Methoden der Superklasse  
- Subklassen können eigene Methoden hinzufügen  
- Superklassen sind allgemeiner, Subklassen spezialisierter  

Beispiel:

    class Animal {
        void sayHello() {
            System.out.println("Hello from Animal");
        }
    }

    class Parrot extends Animal {
        @Override
        void sayHello() {
            System.out.println("Hello from Parrot");
        }
    }

Aufruf:

    Parrot p = new Parrot();
    p.sayHello();

---

## 7. Methoden überschreiben (Override)

Subklassen können eine Methode der Superklasse ersetzen.

Regeln:
- gleicher Name  
- gleiche Parameter  
- gleiche oder „größere“ Sichtbarkeit  
- Annotation `@Override` empfohlen  

Nutzung:

    super.methodenName()   // Zugriff auf Superklasse
    this.methodenName()    // Zugriff auf eigene Methode

---

## 8. Methoden überladen (Overload)

Gleicher Methodenname, verschiedene Parameterlisten:

    int summe(int x, int y) { return x + y; }
    int summe(int x, int y, int z) { return x + y + z; }
    double summe(double a, double b) { return a + b; }

Overload passiert **in der gleichen Klasse**, nicht zwischen Sub-/Superklasse.

---

## 9. Zugriffsmodifizierer (public, private, protected)

| Modifier   | Überall sichtbar | In Subklassen | Im Package |
|------------|------------------|---------------|------------|
| public     | ja               | ja            | ja         |
| protected  | nein (außer Vererbung) | ja  | ja |
| default    | nein             | nein          | ja |
| private    | nein             | nein          | nein |

Merke:
- `private` wird NICHT vererbt  
- `protected` wird vererbt  
- `public` ist überall sichtbar  

---

## 10. static

`static` bedeutet: gehört zur Klasse, nicht zum Objekt.

    class MathUtils {
        static int add(int a, int b) {
            return a + b;
        }
    }

Aufruf:

    int r = MathUtils.add(3, 5);

Nutzen:
- Hilfsmethoden  
- Konstanten  
- kein Objekt nötig  

---

## 11. Abstrakte Klassen & abstrakte Methoden

Abstrakte Klassen können nicht instanziiert werden.  
Sie dienen als Oberklassen.

    abstract class Tier {
        abstract void geraeusch();
    }

Subklasse MUSS die abstrakte Methode implementieren:

    class Hund extends Tier {
        void geraeusch() {
            System.out.println("Wuff");
        }
    }

---

## 12. Type Casting (Typumwandlung)

### Implizit (automatisch)
Von kleinerem zu größerem Datentyp:

    int x = 5;
    double y = x;   // ok

### Explizit (erzwingen)
Von größerem zu kleinerem Typ:

    double a = 5.7;
    int b = (int) a;   // b = 5

### String ↔ Zahl

    int n = Integer.parseInt("123");
    String s = String.valueOf(123);

Objektdatentypen (Integer, Double etc.) bieten Methoden für Parsing und Konvertierung.

---

## Fazit
Dieser Abschnitt führt in die Kernkonzepte der objektorientierten Programmierung ein:
Klassen, Objekte, Methoden, Konstruktoren, Vererbung, Kapselung und abstrakte Klassen.  
Diese Grundlagen ermöglichen strukturierten, flexiblen und wartbaren Java-Code und bilden das Fundament für jede moderne Softwareentwicklung.

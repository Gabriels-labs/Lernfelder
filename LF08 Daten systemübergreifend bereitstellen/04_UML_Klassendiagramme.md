# UML-Klassendiagramme als Werkzeug in der Softwareentwicklung

## 1. Zweck von Klassendiagrammen

Klassendiagramme zeigen die **statische Struktur** eines Systems:

- Welche Klassen gibt es?
- Welche Attribute und Methoden haben sie?
- Wie hängen die Klassen zusammen?

Sie unterstützen:
- ein gemeinsames Verständnis im Team,
- bessere Wartbarkeit,
- und eine saubere objektorientierte Struktur.

---

## 2. Aufbau einer Klasse

Eine Klasse wird als Rechteck mit drei Bereichen dargestellt:

1. **Name** der Klasse  
2. **Attribute** (Eigenschaften/Zustand)  
3. **Methoden** (Fähigkeiten/Verhalten)

Sichtbarkeit vor Attributen/Methoden:
- `+` public  
- `-` private  
- `#` protected  
- `~` package

Beispiele für Datentypen: `String`, `int`, `boolean`, `Date`, `double`.

---

## 3. Beziehungen zwischen Klassen

Wichtige Beziehungstypen:

- **Vererbung** (Is-a-Beziehung):  
  - Unterklasse erbt von Oberklasse  
  - Darstellung: Linie mit Dreieckspfeil zur Oberklasse

- **Assoziation**:  
  - Allgemeine Beziehung (z. B. „Person hat Adresse“)

- **Aggregation** (loses Teil-Ganzes):  
  - Ganze kann ohne Teile existieren  
  - Darstellung: leere Raute an der Ganzes-Seite

- **Komposition** (starkes Teil-Ganzes):  
  - Teile hängen existenziell am Ganzen  
  - Darstellung: ausgefüllte Raute

**Kardinalitäten** (z. B. `1`, `0..1`, `*`, `1..*`) zeigen, wie viele Objekte an einer Beziehung beteiligt sind.

---

## 4. Abstrakte Klassen

- Dienen als Oberklassen, werden aber nicht direkt instanziiert
- Können gemeinsame Attribute und Methoden bündeln
- Häufig mit «abstract» oder kursivem Namen gekennzeichnet

---

## Fazit

Dieses Kapitel fasst die wesentlichen Bausteine von UML-Klassendiagrammen zusammen: den Aufbau von Klassen mit Attributen und Methoden, Sichtbarkeiten sowie grundlegende Beziehungstypen wie Vererbung, Assoziation, Aggregation und Komposition. Damit liefert es ein strukturiertes Bild, wie objektorientierte Systeme modelliert und in ihrer statischen Struktur beschrieben werden.

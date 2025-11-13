# UML & Anwendungsfalldiagramme

## 1. Wozu UML?

UML (Unified Modeling Language) ist eine Standardsprache, um Systeme grafisch darzustellen.  
Sie hilft dabei,

- Anforderungen zu klären,
- mit Fachbereichen zu kommunizieren,
- und Software zu planen und zu dokumentieren.

Es gibt grob zwei Gruppen:
- **Strukturdiagramme** (z. B. Klassendiagramm)
- **Verhaltensdiagramme** (z. B. Use Case, Aktivitätsdiagramm)

---

## 2. Anwendungsfalldiagramme – Überblick

Anwendungsfalldiagramme (Use-Case-Diagramme) zeigen:

- **Wer** (Akteure)  
- **was** (Use Cases)  
- mit **welchem System** macht.

Sie konzentrieren sich auf **funktionale Anforderungen** und sind ein guter Einstieg in objektorientierte Analyse.

---

## 3. Elemente eines Use-Case-Diagramms

- **Systemgrenze**: Kasten mit dem Systemnamen
- **Akteur**: Strichmännchen außerhalb des Systems
- **Use Case**: Oval mit Funktions- oder Zielbeschreibung
- **Beziehungen**: Linien zwischen Akteuren und Use Cases

Akteure können Menschen (z. B. „Benutzer“) oder andere Systeme (z. B. „Zahlungssystem“) sein.

---

## 4. Beziehungen zwischen Use Cases

- **Normale Beziehung**: einfache Linie  
- **«include»**:  
  - Ein Use Case zieht einen anderen immer mit hinein  
  - Wiederverwendung eines gemeinsamen Teilablaufs  
- **«extend»**:  
  - Erweiterung, die nur unter bestimmten Bedingungen ausgeführt wird  
  - Der Basis-Use-Case funktioniert auch ohne die Erweiterung

---

## 5. Beispiel: Geldautomat

Akteur: Bankkunde  
Use Cases (vereinfacht):

- Karte einlesen  
- PIN prüfen  
- Kontostand anzeigen  
- Geld abheben (inklusive PIN-Eingabe)

So entsteht ein schnelles, verständliches Bild der Funktionalität – geeignet für Gespräche mit Kunde oder Fachabteilung.

---

## Fazit

Das Kapitel stellt Anwendungsfalldiagramme als Werkzeug vor, um die funktionale Sicht auf ein System zu modellieren: Akteure, Anwendungsfälle und deren Beziehungen werden klar abgegrenzt und grafisch festgehalten. Dadurch entsteht ein verständliches Bild der Systemgrenzen und der angebotenen Funktionen, das als Grundlage für weitere Analyse- und Designschritte dient.

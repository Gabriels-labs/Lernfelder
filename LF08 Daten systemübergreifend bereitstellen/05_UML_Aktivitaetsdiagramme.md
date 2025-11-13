# UML-Aktivitätsdiagramme und Darstellungselemente

## 1. Was beschreibt ein Aktivitätsdiagramm?

Ein Aktivitätsdiagramm zeigt, **wie ein Ablauf Schritt für Schritt** durchlaufen wird:

- Welche Aktionen werden in welcher Reihenfolge ausgeführt?
- Wo wird entschieden?
- Wo laufen Dinge parallel?

Es eignet sich für:
- Geschäftsprozesse (z. B. Bestellablauf)
- Ablauf von Algorithmen
- Workflows mit Entscheidungen und Verzweigungen

---

## 2. Wichtige Elemente

- **Startknoten**: gefüllter Kreis – Start des Ablaufs  
- **Endknoten**: gefüllter Kreis mit Außenring – Ablauf komplett beendet  
- **Aktion**: abgerundetes Rechteck, z. B. „Passwort eingeben“  
- **Kontrollfluss**: Pfeil, zeigt die Reihenfolge der Aktionen  

**Entscheidung (if):**
- Raute mit einem Eingang und mehreren Ausgängen
- Ausgänge mit Bedingungen in `[ ]`
- Nur ein Pfad wird weiterverfolgt

**Zusammenführung:**
- Raute, mehrere Eingänge, ein Ausgang
- Zusammenführung mehrerer Alternativen

**Gabelung / Vereinigung (Parallelität):**
- Dicke Balken
- Gabelung: ein Eingang, mehrere parallele Ausgänge
- Vereinigung: mehrere parallele Eingänge, ein Ausgang

**Swimlanes:**
- Unterteilung in Spalten (z. B. „Benutzer“, „System“)
- Zeigen, wer welche Aktion ausführt

---

## 3. Beispiel: Login-Prozess (vereinfacht)

1. Start  
2. Aktion: „Benutzername und Passwort eingeben“  
3. Entscheidung: `[Daten gültig?]`  
   - Ja → Aktion: „Zugang gewähren“ → Endknoten  
   - Nein → Aktion: „Fehlermeldung anzeigen“ → zurück zur Eingabe

---

## Fazit

Das Kapitel beschreibt Aktivitätsdiagramme als Mittel zur Modellierung von Abläufen mit Aktionen, Entscheidungen und parallelen Pfaden. Anhand der wichtigsten Symbole und eines typischen Login-Beispiels wird gezeigt, wie Prozesse klar und nachvollziehbar visualisiert werden können, sodass fachliche Abläufe und technische Umsetzung besser aufeinander abgestimmt werden.

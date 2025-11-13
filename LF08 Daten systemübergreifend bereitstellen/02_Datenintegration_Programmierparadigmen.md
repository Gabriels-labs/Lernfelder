# Datenintegration & Programmierparadigmen

## 1. Daten systemübergreifend bereitstellen

Unternehmen nutzen viele verschiedene Systeme (CRM, ERP, Fachanwendungen).  
Typische Probleme dabei:

- Unterschiedliche **Strukturen** (Tabelle vs. XML/JSON)
- Unterschiedliche **Bedeutung** (z. B. „Name“ = vollständiger Name vs. Nachname)
- Unterschiedliche **Formate** (Datum, Zahlen)
- Unterschiedliche **Technologien** (SQL, NoSQL, Files)
- Unterschiedliche **Qualität** (alt, unvollständig, ungenau)

Ziel der Datenintegration:  
**trotz dieser Unterschiede eine gemeinsame, nutzbare Sicht auf die Daten schaffen.**

---

## 2. Formen der Datenintegration

### Physische Integration

- Daten aus Quellsystemen werden in eine zentrale Datenbank übernommen
- Typisch: regelmäßige ETL-Prozesse (Extract – Transform – Load)
- Vorteil: gute Performance, einheitliche Sicht
- Nachteil: nicht immer „tagesaktuell“

### Virtuelle Integration

- Daten bleiben in den Ursprungssystemen
- Zugriff erfolgt über virtuelle Sichten / spezielle Integrationsschichten
- Vorteil: aktuelle Daten in (fast) Echtzeit
- Nachteil: abhängig von Verfügbarkeit und Geschwindigkeit der Quellsysteme

---

## 3. Data Warehouse vs. Data Lake

**Data Warehouse (DWH)**  
- Strukturierte, bereinigte Daten  
- Stark für Berichte, Kennzahlen, Management-Entscheidungen  
- Schema wird **vor** dem Laden definiert (schema-on-write)

**Data Lake**  
- Speichert Daten im Rohformat (Logs, Dateien, JSON, Bilder usw.)  
- Stark für Big-Data-Analysen und Machine Learning  
- Schema wird erst **beim Lesen** angewendet (schema-on-read)

Kurz:  
DWH = „aufgeräumter Analyse-Raum“  
Data Lake = „Rohdaten-Lager“ für flexible Auswertungen.

---

## 4. Programmierparadigmen – Denkmodelle beim Programmieren

Ein Programmierparadigma beschreibt, **wie** man Probleme in Code übersetzt.

### Imperativ (strukturiert & prozedural)

- Programm = Folge von Anweisungen
- Zustand wird über Variablen verändert
- Kontrollstrukturen: if, Schleifen

Strukturiert:  
- „sauberer“ Kontrollfluss (Sequenz, Verzweigung, Schleife)

Prozedural:  
- Code wird in Funktionen/Prozeduren aufgeteilt  
- Besser wartbar und wiederverwendbar

Typische Sprachen: C, klassische Java-/Python-Stile.

### Deklarativ (funktional & logisch)

- Fokus auf „Was soll erreicht werden?“ statt „Wie?“
- Funktionales Programmieren:
  - Reine Funktionen ohne Seiteneffekte
  - Gut testbar, gut für Datenverarbeitung
- Logisches Programmieren:
  - Fakten + Regeln
  - System leitet Lösungen selbst ab (z. B. Prolog)

---

## Fazit

Dieses Kapitel fasst zwei Ebenen zusammen: Auf der **Datenebene** werden verschiedene Formen der Integration (physisch, virtuell, Data Warehouse, Data Lake) beschrieben, mit denen Informationen aus heterogenen Systemen zusammengeführt werden. Auf der **Codeebene** werden wichtige Programmierparadigmen gegenübergestellt, die unterschiedliche Sichtweisen auf die Strukturierung von Programmen und die Lösung von Problemen bieten.

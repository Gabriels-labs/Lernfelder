# 07 – Datenbanken – Grundlagen

## Grundbegriffe
- **DBMS**, **Datenmodell**, **ANSI/SPARC-Architektur** (logisch/extern/intern – Überblick).  
- **Relationales Modell:** Tabellen (Relationen), **Primär-/Fremdschlüssel**, Integrität, Redundanz vermeiden.  
- **ERM → Relational:** Entitäten/Beziehungen modellieren, in Tabellen überführen.

## SQL – Kategorien & Standard
- **DDL** (z. B. `CREATE TABLE`, `ALTER`, `DROP`),  
- **DML** (`SELECT`, `INSERT`, `UPDATE`, `DELETE`),  
- **DCL** (`GRANT`, `REVOKE`),  
- **TCL** (`COMMIT`, `ROLLBACK`).  
- SQL ist standardisiert (ANSI/ISO); Dialekte existieren.

## Abfragen & Joins (Überblick)
- Projektion/Selektion; **JOINs**: INNER/LEFT/RIGHT/FULL – Verknüpfung über Schlüssel.  
- Einfache Beispiele reichen (Mehrtabellenabfragen per JOIN statt redundanter Daten).

## Python ↔ SQLite
- Kleine Projekte: lokale **SQLite** per Python-Modul (keine Extra-Installation).

## Prüfungsfokus (IHK)
- **PK/FK**, ERM→Relational, Grund-SQL (DDL/DML), JOIN-Prinzip verstehen; Zweck von SQLite im Lernkontext.

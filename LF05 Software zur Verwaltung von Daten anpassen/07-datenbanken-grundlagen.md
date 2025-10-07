# 07 – Datenbanken – Grundlagen

## Begriffe & Architektur
- **Datenbank (DB):** geordnete, dauerhaft gespeicherte Daten für Anwendungen.
- **DBMS (Datenbankmanagementsystem):** Software, die Daten **speichert**, **schützt** und **organisiert**. Kernaufgaben:
  - **Persistenz & Speicherverwaltung**, **Transaktionen** (ACID), **Nebenläufigkeit** (Sperren, MVCC),
  - **Sicherheit** (Benutzer/Rollen/Rechte), **Recovery** (WAL/Logs, Backups),
  - **Abfragesprache** (meist **SQL**), **Sichten**, **Indizes**, **Optimierung**.
- **RDBMS (relational):** Tabellen mit Beziehungen (Schlüsseln); Beispiele: **PostgreSQL**, **MySQL/MariaDB**, **SQLite**, **MS SQL Server**, **Oracle**.
  - **Client/Server** (z. B. PostgreSQL) vs. **Embedded** (z. B. SQLite – Datei im Projekt).
- **Werkzeuge (typisch):** CLI (**psql**, **mysql**, **sqlite3**), GUIs (**pgAdmin**, **MySQL Workbench**, **SSMS**, **DBeaver**, **DataGrip**).

## Datenmodellierung (vom Fachlichen zum Relationalen)
- **ERM (Entity-Relationship-Modell):** Entitäten (Objekte), Attribute (Eigenschaften), Beziehungen mit **Kardinalität** (1:1, 1:n, n:m) und **Optionalität** (0/1).
- **Mapping → Tabellen:**
  - Entität → **Tabelle**; Attribut → **Spalte** (Datentyp).
  - **1:n**: FK in der n-Tabelle.
  - **n:m**: **Zwischentabelle** mit zwei FKs.
- **Schlüsselbegriffe:** **Primärschlüssel (PK)** eindeutig; **Fremdschlüssel (FK)** verweist auf PK; **Kandidatenschlüssel** (alternative Eindeutigkeit).

## Relationales Modell & Normalisierung
- Ziel: **Redundanz** und **Anomalien** vermeiden.
- **1NF:** atomare Werte (keine Listen/Felder in einer Zelle).
- **2NF:** keine **teilweisen** Abhängigkeiten vom **Teilschlüssel** (bei zusammengesetztem PK).
- **3NF:** keine **transitiven** Abhängigkeiten (Nicht-Schlüsselattribute hängen nur vom PK ab).
- **Praxis:** für Reporting/Performance manchmal **gezielte Denormalisierung** (bewusst begründen).

## SQL – Sprachbereiche & Constraints
- **DDL** (Struktur): `CREATE`, `ALTER`, `DROP`
- **DML** (Daten): `SELECT`, `INSERT`, `UPDATE`, `DELETE`
- **DCL** (Rechte): `GRANT`, `REVOKE`
- **TCL** (Transaktionen): `COMMIT`, `ROLLBACK`
- **Constraints:** `PRIMARY KEY`, `FOREIGN KEY ... REFERENCES`, `NOT NULL`, `UNIQUE`, `CHECK (...)`, `DEFAULT ...`

### Mini-Beispiele
```sql
-- Tabellen & Schlüssel
CREATE TABLE kunde (
  id        INTEGER PRIMARY KEY,
  name      VARCHAR(100) NOT NULL,
  email     VARCHAR(200) UNIQUE
);

CREATE TABLE bestellung (
  nr        INTEGER PRIMARY KEY,
  kunde_id  INTEGER NOT NULL REFERENCES kunde(id) ON DELETE CASCADE,
  datum     DATE      NOT NULL,
  betrag    DECIMAL(10,2) CHECK (betrag >= 0)
);

-- Index (beschleunigt Suchen/Join)
CREATE INDEX idx_bestellung_kunde ON bestellung(kunde_id);

-- DML & Join
INSERT INTO kunde (id, name, email) VALUES (1, 'Meyer', 'm@ex.de');
INSERT INTO bestellung (nr, kunde_id, datum, betrag) VALUES (101, 1, DATE '2025-01-10', 149.90);

SELECT k.name, b.nr, b.betrag
FROM kunde k
JOIN bestellung b ON b.kunde_id = k.id
WHERE b.betrag >= 100
ORDER BY b.datum DESC;

-- Transaktion
BEGIN;
UPDATE bestellung SET betrag = betrag + 10 WHERE nr = 101;
-- bei Fehler: ROLLBACK;
COMMIT;

## Prüfungsfokus (IHK)
- **PK/FK**, ERM→Relational, Grund-SQL (DDL/DML), JOIN-Prinzip verstehen; Zweck von SQLite im Lernkontext.

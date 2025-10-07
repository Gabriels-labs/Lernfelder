# 06 – Dateizugriff & Dateiformate

## Dateien mit Python (Kernprinzip)
1. **Öffnen** (`open(path, mode)`),  
2. **Bearbeiten** (lesen/schreiben),  
3. **Schließen** (`close()` bzw. `with`-Block).  
- **Modi:** `r` (lesen), `w` (schreiben, überschreibt), `a` (anhängen), optional **Text/Binär**.  
- Wichtige Methoden: `read()`, `readline()`, `readlines()`, `write()`, `writelines()`.  
- **Fehlerbehandlung:** `try/except` für IO-Fehler; Pfade ordentlich behandeln.

## Dateiformate (Überblick)
- **CSV:** strukturierte Texttabelle mit Trennzeichen (meist Komma/;).  
- **XML/JSON:** textbasierte, selbstbeschreibende Struktur; Austausch/Integration.  
- **Binär/Text, proprietär vs. standardisiert**; Dateigröße (Bytes), Endung ↔ Format beachten.

## Prüfungsfokus (IHK)
- Streams/Modi korrekt anwenden; einfache CSV-Ein-/Ausgabe implementieren; Vor-/Nachteile **CSV vs. XML/JSON** benennen.

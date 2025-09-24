# Daten, Informationen, Zahlensysteme & Darstellungsformen

## 1) Informationen vs. Daten
- **Daten:** rohe Werte ohne Kontext (z. B. `42`, `2025-09-23`, `Anna`).
- **Informationen:** interpretierte Daten **mit** Kontext (z. B. „Kundin *Anna* hat **42** offene Tickets am **23.09.2025**“).
- Ziel: Daten so **repräsentieren** und **strukturieren**, dass Informationen für Entscheidungen nutzbar sind.

## 2) Zahlensysteme (beschreiben & umrechnen)
**Dezimal (Basis 10):** Ziffern 0–9, Stellenwert \(10^n\).  
**Dual (Basis 2):** Ziffern 0/1, Stellenwert \(2^n\) (gerade/ungerade = letztes Bit 0/1).  
**Hexadezimal (Basis 16):** Ziffern 0–9, A–F; **1 Hex-Ziffer = 4 Bit (Nibble)**.

**Umrechnen – Kurzrezepte**
- Dez → Bin: wiederholt durch 2 teilen, Reste **von unten** lesen. Bsp.: \(25_{10} = 11001_2\).
- Bin → Dez: Stellenwerte aufsummieren. Bsp.: \(11001_2 = 16+8+1 = 25_{10}\).
- Dez → Hex: wiederholt durch 16 teilen, Reste lesen. Bsp.: \(255_{10} = FF_{16}\).
- Bin ↔ Hex: in 4-Bit-Gruppen bündeln. Bsp.: \(1011\,1100_2 = BC_{16}\).

**Zweierkomplement (negative ganze Zahlen)**
- Bereich bei **n Bit**: \([-2^{n-1},\, 2^{n-1}-1]\).
- Bildung von \(-x\): \(x\) binär → **Bits invertieren** → **+1**.
- Bsp. (8 Bit, \(-18\)): \(18_{10}=0001\,0010\) → invertiert \(1110\,1101\) → +1 \(=\) **1110 1110**.

**Gleitkommazahlen (Mantisse/Signifikand & Exponent)**
- Form: \(\pm\,\text{Mantisse} \times \text{Basis}^{\text{Exponent}}\) (Basis meist 2).
- Z. B. float32 (IEEE 754): Vorzeichen | Exponent (Bias) | Mantisse.  
- Wichtig: **Normalisierung**, Rundung, endliche Präzision ⇒ numerische Fehler möglich.

## 3) Darstellungsformen von Daten
**Zahlen:**  
- **Ganze Zahlen** (Integer, inkl. Zweierkomplement).  
- **Gleitkomma** (float/double; Mantisse/Exponent, Genauigkeit beachten).

**Zeichen & Text:**  
- **ASCII** (7 Bit, 128 Zeichen), **ISO-8859-1** (8 Bit, Westeuropa),  
- **UTF-8** (variabel, ASCII-kompatibel), **UTF-16** (2 Bytes pro Code-Unit, mit/ohne **BOM**).  
- Begriffe: **Zeichensatz** (Welche Zeichen?), **Kodierung** (Wie binär codiert?).

**Grafische Daten:**  
- **Rastergrafik** (Pixel): Auflösung (z. B. 1920×1080), **Farbtiefe** (z. B. 24 Bit = 8 Bit pro RGB-Kanal). Formate: PNG, JPEG.  
- **Vektorgrafik** (Pfade/Primitive): skalierbar ohne Qualitätsverlust. Formate: SVG, AI.  
- **Farbräume:** **RGB** (additiv, Bildschirm), **CMYK** (subtraktiv, Druck).

**Audiodaten:**  
- **Abtastrate / Sampling-Rate** (Hz) & **Sampling-Tiefe** (Bit/Sample), Kanäle (Mono/Stereo).  
- **Nyquist:** \(f_s \ge 2 \cdot f_{max}\).  
- **Unkomprimierte Bitrate:** \(f_s \times \text{Tiefe} \times \text{Kanäle}\).  
  Bsp. CD-Audio: \(44{,}100 \times 16 \times 2 \approx 1{,}411{,}200\ \text{bit/s} \approx 1{,}411\ \text{kbps}\).

**Algorithmen & Programme:**  
- **Quellcode** = Textdaten (Dateien), kompiliert oder interpretiert; als Datenobjekt versionierbar (Repos).

## 4) Daten nach Art & Herkunft vergleichen
- **Repräsentation:** binär, Text, strukturiert (CSV/JSON), halb-/unstrukturiert (Freitext, Bilder).  
- **Struktur:** Schema (Felder/Datentypen), Beziehungen, Metadaten.  
- **Quelle/Herkunft:** **Primärdaten** (Mess-/Logdaten), **Sekundärdaten** (aggregiert/abgeleitet).  
- **Sicherheit (praktisch):** Zugriffsrechte, Integrität, Nachvollziehbarkeit gemäß Sensibilität/Kontext.

## 5) Speicherung, Datenschutz, Datensicherheit
- **Speicherung:** Dateien (CSV/JSON/Binär), Datenbanken (relational/NoSQL), Versionierung, Backups.  
- **Datenschutz:** rechtlicher Schutz **personenbezogener** Daten (Zweckbindung, Datenminimierung usw.).  
- **Datensicherheit:** technische/organisatorische Maßnahmen (Berechtigungen, Backup, ggf. Verschlüsselung).

## 6) Speicherbedarf (Einheiten & Faustregeln)
- **Byte (B)**; **KB/MB/GB** = 10³/10⁶/10⁹ B; **KiB/MiB/GiB** = 2¹⁰/2²⁰/2³⁰ B.  
- **Beispiele:**  
  - Bild unkomprimiert: \( \text{Breite} \times \text{Höhe} \times \text{Farbtiefe in Bytes} \).  
    1920×1080 @ 24 Bit ≈ \(1920 \times 1080 \times 3 \approx 5{,}93\ \text{MB}\) (dezimal).  
  - Audio PCM (CD): \(44{,}100 \times 16 \times 2 \approx 1{,}411{,}200\ \text{bit/s}\).

## 7) Tagesergebnis
Unterschied **Daten vs. Informationen** sicher formulieren; **Zahlensysteme** (Dez/Bin/Hex, Umrechnung, Zweierkomplement) beherrschen; **Darstellungsformen** (Zahl, Text, Grafik, Audio, Code) und **Speicherbedarf** einschätzen; Basics zu **Datenschutz/Datensicherheit** im Kontext Speicherung kennen.

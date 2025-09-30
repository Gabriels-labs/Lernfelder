# 02 – Kabel & Medien (Gebäude, Campus, RZ)

## Strukturierte Verkabelung (ISO/IEC 11801)
- **Primär (Campus)**: Gebäude↔Gebäude (Außenstrecken).
- **Sekundär (Vertikal/Gebäude)**: Hauptverteiler↔Etagenverteiler.
- **Tertiär (Horizontal/Etage)**: Etagenverteiler↔Arbeitsplatz (TA/Dose).
- Doku ist Pflicht: Port-/Patch-Pläne, Etagenpläne, eindeutige Bezeichnungen.

## Kupfer (Twisted Pair)
- **Aufbau**: massive Leiter (Installationskabel) vs. Litze (Patch), **AWG 23/24** üblich.
- **Schirmcodes**: U/UTP (ungeschirmt), F/UTP, S/UTP, **U/FTP**, **S/FTP** (sehr robust).
- **Kategorie (Komponente) vs. Klasse (Strecke)**:
  - Cat5e → Klasse D (bis 1G), Cat6 → Klasse E (1G; 10G nur kurz/abhängig),
  - **Cat6A → Klasse EA (10G bis 100 m)** – Neubau-Standard,
  - Cat7/7A → Klasse F/FA (Spezialstecker möglich), Cat8 → Klasse I/II (25/40G kurz).
- **Regeln**: **100 m Kanal** (90 m Permanent + 2×5 m Patch); Biegeradius ≥ 4×Ø; saubere Erdung/Schirmführung.
- **PoE-Hinweise**: Bündelwärme, Querschnitt, Crimp-Qualität (DC-Unbalance) beachten.

## LWL (Lichtwellenleiter)
- **Fasern**: Multimode **OM3/OM4/OM5** (Campus/10–100G), Singlemode **OS2** (weit, ausbau-sicher).
- **Kabelaufbau**: innen *Tight-Buffered*; außen *Loose-Tube* (gelgefüllt), oft **armiert**; **dielektrisch** (ohne Metall) gegen Blitz.
- **Stecker**: **LC** (heute Standard), SC; Mehrfaser-Trunks **MPO/MTP**.
- **Transceiver**: SFP (1G), **SFP+ (10G)**, QSFP+ (40G), QSFP28 (100G). **SR/LR** = kurz/weit (wellenlängen-/faserabhängig).

## Mantel & Brandschutz (CPR)
- **LSZH/LS0H** halogenfrei (Innenräume), **PE** (außen/UV), **PVC** Standard.
- **CPR**: Eca < Dca < Cca < **B2ca** (Brandverhalten ↑); Zusätze s/d/a (Rauch/Tropfen/Säure).

### IHK-Kernanforderungen
- Ebene benennen (Tertiär/Sekundär/Primär) und Medium begründen.
- Cat/Klasse/Schirmung und 100-m-Regel sicher anwenden.
- OM/OS, LC/SC, SFP/SFP+ im Kontext einordnen; CPR/LSZH nennen.

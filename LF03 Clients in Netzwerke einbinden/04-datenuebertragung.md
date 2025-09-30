# Grundlagen der Datenübertragung

## Kenngrößen
- **Rate/Throughput**: \(R = D / t\); **Übertragungszeit**: \(t = D / R\). Saubere Einheiten (bit/s vs. Byte/s).
- **Goodput < Nennrate** (Overheads, Retransmits). Latenz/Jitter/Verluste beeinflussen den effektiven Durchsatz.

## Ethernet & TCP/IP kurz
- **Ethernet (L1/L2)**: Frames, FCS; mit VLAN-Tag (802.1Q) inkl. 12-Bit VLAN-ID. **MTU** typ. 1500 B.
- **TCP/IP**: IP adressiert/netzt, TCP/UDP adressieren Anwendungen (Ports); TCP verbindungsorientiert, UDP verbindungslos.

## Übertragungsarten (Begriffe)
- Seriell/Parallel, Simplex/Halbduplex/Vollduplex, Zeit/Frequenz/Wellenlängen-Multiplex – Einordnung kennen.

### IHK-Kernanforderungen
- Transferzeit/Rate berechnen und sauber begründen.
- MTU/VLAN-Tagging in der Praxis einordnen (Overhead/Segmentierung).
- TCP vs. UDP Eigenschaften nennen (Ports/Verbindungsart).

# Grundlagen der Datenübertragung

## Kenngrößen
- **Rate/Throughput**: \(R = D / t\); **Übertragungszeit**: \(t = D / R\). Saubere Einheiten (bit/s vs. Byte/s). :contentReference[oaicite:9]{index=9}
- **Goodput < Nennrate** (Overheads, Retransmits). Latenz/Jitter/Verluste beeinflussen den effektiven Durchsatz. :contentReference[oaicite:10]{index=10}

## Ethernet & TCP/IP kurz
- **Ethernet (L1/L2)**: Frames, FCS; mit VLAN-Tag (802.1Q) inkl. 12-Bit VLAN-ID. **MTU** typ. 1500 B. :contentReference[oaicite:11]{index=11}
- **TCP/IP**: IP adressiert/netzt, TCP/UDP adressieren Anwendungen (Ports); TCP verbindungsorientiert, UDP verbindungslos. :contentReference[oaicite:12]{index=12}

## Übertragungsarten (Begriffe)
- Seriell/Parallel, Simplex/Halbduplex/Vollduplex, Zeit/Frequenz/Wellenlängen-Multiplex – Einordnung kennen. :contentReference[oaicite:13]{index=13}

### IHK-Kernanforderungen
- Transferzeit/Rate berechnen und sauber begründen. :contentReference[oaicite:14]{index=14}  
- MTU/VLAN-Tagging in der Praxis einordnen (Overhead/Segmentierung). :contentReference[oaicite:15]{index=15}  
- TCP vs. UDP Eigenschaften nennen (Ports/Verbindungsart). :contentReference[oaicite:16]{index=16}

# 08 – Daten- & Netzwerksicherheit

## Grundprinzipien
- **CIA-Triade**: Vertraulichkeit, Integrität, Verfügbarkeit – daran Maßnahmen ausrichten.

## Speicher & Backup
- **RAID ≠ Backup**. Backup-Arten: Voll, Image, Differenziell, Inkrementell.
- **3-2-1-Regel**, **RPO/RTO** definieren; regelmäßige **Restore-Tests**.

## Netzwerk & Zugang
- **Zonierung/Segmentierung** (LAN/Server/DMZ/Gast), Firewall-Typen (Paketfilter/Stateful/DPI/NGFW), Proxy.
- **Portschutz**: 802.1X (RADIUS), Port-Security (MAC-Limit), DHCP-Snooping, Dynamic ARP Inspection, BPDU-Guard.

### IHK-Kernanforderungen
- Backup-Strategie inkl. RPO/RTO wählen und begründen.
- Zonierung + Portschutzmaßnahmen korrekt zuordnen.

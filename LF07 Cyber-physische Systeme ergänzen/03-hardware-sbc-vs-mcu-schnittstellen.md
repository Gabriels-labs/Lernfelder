# Hardware: Einplatinencomputer vs. Mikrocontroller & Schnittstellen

## Einplatinencomputer (SBC)
Alles auf einer Platine (CPU, RAM, Schnittstellen). Läuft mit **vollwertigem OS** (z. B. Linux/Raspberry Pi OS).  
**Einsatz:** Gateways, Edge-Analytics, Prototyping, Schulung.  
**Stärken:** Rechenleistung, viele Protokolle, schnelle Entwicklung.

## Mikrocontroller (MCU)
**SoC** mit CPU, Speicher, Peripherie – oft ohne OS oder mit **RTOS** (harte Latenzen, deterministisch).  
**Einsatz:** Motorsteuerungen, Robotik, Ladegeräte, Medizintechnik, Automotive.  
**Stärken:** Echtzeit, geringer Energiebedarf, robuste Einfachheit.

**Unterschied kurz:** SBC = „kleiner Computer“, MCU = „präziser Steuerchip“. In CPS arbeiten sie oft zusammen.

## Wichtige Schnittstellen (kurz & merkbar)
- **GPIO** – digitale **Ein/Aus** für Taster, LEDs, Relais.  
- **UART** – **seriell, asynchron** (TX/RX, Start/Stop/Parity), simpel & weit verbreitet.  
- **I²C** – **synchron** (SDA/SCL), **Adress-Bus** für viele Sensoren auf kurzem Weg.  
- **SPI** – **schnell, Vollduplex** (MISO/MOSI/SCLK/SS), ideal für Displays/ADCs/Flash.

> Design-Tipp: *Weniger exotisch, mehr Standard.* Das spart Zeit bei Beschaffung, Treibern und Debugging.

---

## IHK-Kernanforderungen
- SBC vs. MCU in **einem Satz** unterscheiden (OS/Leistung vs. Echtzeit/Einfachheit) und je 1 Einsatzbeispiel nennen.
- GPIO, UART, I²C, SPI funktional zuordnen (digital, seriell asynchron, Bus mit Adressen, schneller Vollduplex).
- Passende Schnittstelle zum Sensor/Aktor begründen (z. B. Display → SPI, viele kleine Sensoren → I²C).

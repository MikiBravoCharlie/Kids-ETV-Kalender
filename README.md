# Kids-ETV-Kalender

Abonnierbare Kalender mit den ETV-Hamburg-Kinderkursen (Kindersport und ETV Dance) im Sportzentrum Bundesstraße und in der Sporthalle Hohe Weide, für ein 2- und ein 6-jähriges Kind.

## Abo-Links (Kalender > Ablage > Neues Kalenderabonnement)

- 2 Jahre: https://raw.githubusercontent.com/MikiBravoCharlie/kids-etv-kalender/main/ETV-Kurse-2-Jahre.ics
- 6 Jahre: https://raw.githubusercontent.com/MikiBravoCharlie/kids-etv-kalender/main/ETV-Kurse-6-Jahre.ics

## Aufbau

- `kurse.json`: die Kursliste, einzige Datenquelle. Änderungen nur hier.
- `build_ics.py`: erzeugt beide .ics-Dateien aus `kurse.json` (`python3 build_ics.py`).
- `ETV-Kurse-*.ics`: erzeugte Dateien, nicht von Hand bearbeiten.

## Quellen

- Kindersport-Kursplan ab Januar 2026: https://www.etv-hamburg.de/_cache/downloads/5875-fde3fa2514/cms/Abteilungen/Kindersport/Downloads/Kursplan-Kindersport.pdf
- ETV Dance Kursprogramm 2026: https://www.etv-hamburg.de/_cache/downloads/5832-82ea7848f8/cms/Abteilungen/ETV-Dance/Downloads/DANCE_Kursprogramm-2026.pdf

Die Wochentage sind in den PDFs nicht eindeutig beschriftet und wurden über Raumbelegung und die Ferienhefte 2026 zugeordnet. Anmeldung zu allen Kursen über die ETV-App.

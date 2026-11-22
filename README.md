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

- Kindersport, gültig ab August 2026: https://www.etv-hamburg.de/_cache/downloads/7270-9140c03c95/cms/Verein/Kindersport/RZ_KINDERSPORTPROGRAMM-2026_Juli-1-1.pdf
- ETV Dance Kursprogramm 2026, Stand Mai: https://www.etv-hamburg.de/_cache/downloads/7100-368fa00184/cms/Abteilungen/ETV-Dance/Downloads/RZ_DANCE_Kursprogramm-2026_Mai.pdf

Wochentage der Tanzkurse aus der athletx-Kursübersicht des ETV, Kindersport aus der Blockreihenfolge im PDF. Details in CLAUDE.md. Anmeldung zu allen Kursen über die ETV-App.

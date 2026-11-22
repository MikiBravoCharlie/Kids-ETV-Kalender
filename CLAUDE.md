# Anleitung für Claude: ETV-Kinderkalender pflegen

Dieses Repository speist zwei abonnierte Kalender mit ETV-Hamburg-Kinderkursen (Kindersport und ETV Dance) für ein 2- und ein 6-jähriges Kind. Es wird von zwei Personen genutzt, Mirko und seiner Frau, jeweils mit ihrem eigenen Claude. Diese Datei ist die gemeinsame Anleitung; wer den Ablauf ändern will, ändert ihn hier.

Antworten auf Deutsch, keine Gedankenstriche als Einschub.

## Fakten

- Repo: `MikiBravoCharlie/kids-etv-kalender`, Branch `main`
- Abo-Links:
  - https://raw.githubusercontent.com/MikiBravoCharlie/kids-etv-kalender/main/ETV-Kurse-2-Jahre.ics
  - https://raw.githubusercontent.com/MikiBravoCharlie/kids-etv-kalender/main/ETV-Kurse-6-Jahre.ics
- Einzige Datenquelle: `kurse.json`. Tage Montag bis Sonntag, je Kurs: `start`, `ende`, `kurs`, `alter`, `raum`, `kind` (2 oder 6), `art` (S = Kindersport, T = Tanz).
- Räume: `HW` = Sporthalle Hohe Weide 17a, `SP` = Sportplatz Bundesstraße 103, alle anderen Kürzel = Sportzentrum Bundesstraße 96 (UH Untere Halle, GH Große Halle, KH Kleine Halle, Gym I bis V Gymnastikräume, CC Club Céronne Saal).
- `build_ics.py` erzeugt beide .ics-Dateien aus `kurse.json`. Die UIDs sind stabil, damit Abos Termine aktualisieren statt doppeln.
- Quellen der Kursdaten stehen im README. Die Wochentage sind in den ETV-PDFs unsauber beschriftet; bei Unklarheit nachfragen oder auf die ETV-App verweisen.

## Ablauf bei einer Änderung

1. Aktuellen Stand holen (`git pull`), damit Änderungen der anderen Person nicht überschrieben werden.
2. `kurse.json` anpassen. Ein Wunsch wie „nur noch X und Y für den Großen“ heißt: alle anderen Kurse mit `kind: 6` entfernen.
3. `python3 build_ics.py` ausführen und die Terminanzahl prüfen.
4. Commit mit kurzer deutscher Nachricht, die sagt, was sich geändert hat, und Push nach `main`. Bei einem abgelehnten Push erst `git pull --rebase`, dann erneut pushen.
5. In ein, zwei Sätzen sagen, was sich geändert hat und dass die abonnierten Kalender binnen etwa einer Stunde nachziehen.
6. Nur auf Wunsch: einen visuellen Wochenplan als Seite erzeugen.

## Regeln

- Die .ics-Dateien nie von Hand bearbeiten.
- Niemanden neu importieren lassen; die Abo-Links bleiben gleich.
- Das Repository ist öffentlich: keine Namen, Geburtsdaten oder anderen persönlichen Daten der Kinder oder der Familie hineinschreiben.

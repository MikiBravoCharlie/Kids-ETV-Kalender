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
- Quellen der Kursdaten stehen im Abschnitt „Prüfung auf neue ETV-Kurspläne“. Die Wochentage sind in den ETV-PDFs unsauber beschriftet; bei Unklarheit nachfragen oder auf die ETV-App verweisen.

## Ablauf bei einer Änderung

1. Aktuellen Stand holen (`git pull`), damit Änderungen der anderen Person nicht überschrieben werden.
2. `kurse.json` anpassen. Ein Wunsch wie „nur noch X und Y für den Großen“ heißt: alle anderen Kurse mit `kind: 6` entfernen.
3. `python3 build_ics.py` ausführen und die Terminanzahl prüfen.
4. Commit mit kurzer deutscher Nachricht, die sagt, was sich geändert hat, und Push nach `main`. Bei einem abgelehnten Push erst `git pull --rebase`, dann erneut pushen.
5. In ein, zwei Sätzen sagen, was sich geändert hat und dass die abonnierten Kalender binnen etwa einer Stunde nachziehen.
6. Nur auf Wunsch: einen visuellen Wochenplan als Seite erzeugen.

## Prüfung auf neue ETV-Kurspläne

Eine geplante Aufgabe in Mirkos Konto führt diese Prüfung am 1. jedes Monats und zusätzlich am 15. Dezember aus. Sie kann auch jederzeit von Hand angestoßen werden („prüf, ob der ETV neue Kurspläne hat“). Die Prüfung ändert nichts im Repository; Änderungen werden erst nach Zustimmung nach dem Ablauf oben eingespielt.

Aktuell verwendete Pläne (Stand, mit dem `kurse.json` abgeglichen ist):

- Kindersport, gültig ab Januar 2026: https://www.etv-hamburg.de/_cache/downloads/5875-fde3fa2514/cms/Abteilungen/Kindersport/Downloads/Kursplan-Kindersport.pdf
- ETV Dance Kursprogramm 2026: https://www.etv-hamburg.de/_cache/downloads/5832-82ea7848f8/cms/Abteilungen/ETV-Dance/Downloads/DANCE_Kursprogramm-2026.pdf

Vorgehen:

1. Per Websuche die aktuellen Kursplan-PDFs für Kindersport und ETV Dance auf etv-hamburg.de suchen. Ein neuer Plan erkennt sich meist an einer anderen Download-Nummer in der URL, einem neuen Gültigkeitsdatum („gültig ab …“) oder einer neuen Jahreszahl. Ferienhefte (März-, Mai-, Sommer-, Herbstferien) sind keine neuen Pläne.
2. Gibt es keinen neueren Plan: kurz melden „Keine neuen ETV-Kurspläne gefunden“ und fertig.
3. Gibt es einen neueren Plan: ihn lesen und nur die Kurse vergleichen, die für das Repository relevant sind (Sportzentrum Bundesstraße und Sporthalle Hohe Weide, Altersangaben, die 2 oder 6 Jahre einschließen). Mit `kurse.json` abgleichen.
4. Ergebnis als kurze Liste melden: neue Kurse, weggefallene Kurse, geänderte Zeiten, Tage oder Räume, jeweils mit Kind (2 oder 6). Unsichere Wochentage ausdrücklich als unsicher kennzeichnen. Link zum neuen PDF angeben.
5. Fragen, ob die Änderungen übernommen werden sollen. Nach Zustimmung nach dem Ablauf oben ändern und hier in diesem Abschnitt die Liste der aktuell verwendeten Pläne aktualisieren.

## Regeln

- Die .ics-Dateien nie von Hand bearbeiten.
- Niemanden neu importieren lassen; die Abo-Links bleiben gleich.
- Das Repository ist öffentlich: keine Namen, Geburtsdaten oder anderen persönlichen Daten der Kinder oder der Familie hineinschreiben.

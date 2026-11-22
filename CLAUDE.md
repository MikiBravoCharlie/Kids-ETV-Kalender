# Anleitung für Claude: ETV-Kinderkalender pflegen

Dieses Repository speist zwei abonnierte Kalender mit ETV-Hamburg-Kinderkursen (Kindersport und ETV Dance) für ein 2- und ein 6-jähriges Kind. Es wird von zwei Personen genutzt, Mirko und seiner Frau, jeweils mit ihrem eigenen Claude. Diese Datei ist die gemeinsame Anleitung; wer den Ablauf ändern will, ändert ihn hier.

Antworten auf Deutsch, keine Gedankenstriche als Einschub.

## Fakten

- Repo: `MikiBravoCharlie/Kids-ETV-Kalender`, Branch `main` (GitHub unterscheidet bei Repo-Namen nicht nach Groß- und Kleinschreibung; die Abo-Links bleiben bewusst klein geschrieben, damit niemand neu abonnieren muss)
- Abo-Links:
  - https://raw.githubusercontent.com/MikiBravoCharlie/kids-etv-kalender/main/ETV-Kurse-2-Jahre.ics
  - https://raw.githubusercontent.com/MikiBravoCharlie/kids-etv-kalender/main/ETV-Kurse-6-Jahre.ics
- Einzige Datenquelle: `kurse.json`. Tage Montag bis Sonntag, je Kurs: `start`, `ende`, `kurs`, `alter`, `raum`, `kind` (2 oder 6), `art` (S = Kindersport, T = Tanz, A = andere Abteilung wie Judo oder Karate).
- Räume: `HW` = Sporthalle Hohe Weide 17a, `SP` = Sportplatz Bundesstraße 103, leer = Raum unbekannt, alle anderen Kürzel = Sportzentrum Bundesstraße 96 (UH Untere Halle, GH Große Halle, KH Kleine Halle, Gym I bis V Gymnastikräume, CC Club Céronne Saal).
- `build_ics.py` erzeugt beide .ics-Dateien aus `kurse.json`. Die UIDs sind stabil, damit Abos Termine aktualisieren statt doppeln.
- Quellen und Regeln für aktuelle Daten: Abschnitt „Regeln für aktuelle Daten“. Die Wochentage sind in den ETV-PDFs unsauber beschriftet; Kurse mit `"unsicher": true` in der ETV-App prüfen lassen.

## Ablauf bei einer Änderung

1. Aktuellen Stand holen (`git pull`), damit Änderungen der anderen Person nicht überschrieben werden.
2. `kurse.json` anpassen. Ein Wunsch wie „nur noch X und Y für den Großen“ heißt: alle anderen Kurse mit `kind: 6` entfernen.
3. `python3 build_ics.py` ausführen und die Terminanzahl prüfen.
4. Commit mit kurzer deutscher Nachricht, die sagt, was sich geändert hat, und Push nach `main`. Bei einem abgelehnten Push erst `git pull --rebase`, dann erneut pushen.
5. In ein, zwei Sätzen sagen, was sich geändert hat und dass die abonnierten Kalender binnen etwa einer Stunde nachziehen.
6. Nur auf Wunsch: einen visuellen Wochenplan als Seite erzeugen.

## Wöchentlicher Abgleich mit Clubity (automatisch)

Ziel: mindestens einmal pro Woche ein erfolgreicher Abgleich der Kurse in `kurse.json` mit dem ETV-Mitgliederbereich. Eine geplante Aufgabe in Mirkos Konto versucht es jeden Abend auf seinem Mac, weil nur dort der Browser der Claude-App mit seiner Clubity-Anmeldung läuft. Der Mac ist nicht zu festen Zeiten an; ein ausgefallener Lauf ist normal. Mirko hat entschieden: Änderungen werden automatisch übernommen und danach gemeldet.

1. **Zuerst Datum prüfen.** `geprueft_am` in `kurse.json` lesen. Liegt es weniger als 7 Tage zurück: sofort beenden, nichts melden. Der Link über raw.githubusercontent.com kann bis zu etwa 5 Minuten alt sein; maßgeblich ist der Stand im geklonten Repository.
2. **Clubity öffnen** im Browser der Claude-Desktop-App (Tools `Claude_Browser`). Direkt mit Filtern, jeweils eine volle Woche ab morgen über „Weitere Termine anzeigen“ laden:
   - 2 Jahre: https://www.clubity.com/app/de/offerings?includeCanceled=false&includePast=false&includeWaitListed=false&locationIds=6f7cea26-0c21-11ed-9436-222560b74e07&locationIds=19f44114-0c24-11ed-a86e-4217ca18cd30&locationIds=2eaa464a-0ce6-11ed-8881-222560b74e07&age=2
   - 6 Jahre: dieselbe Adresse mit `age=6`
   Die Ort-IDs stehen für Sportzentrum Bundesstraße, Sporthalle Hohe Weide und Bundesstraße 103. Jeder Eintrag zeigt Kategorie, Titel, Datum mit Wochentag und Uhrzeit, Altersspanne und Ort.
3. **Nicht angemeldet?** Erscheint die Anmeldemaske oder „Wähle einen Account“: nicht anmelden, keine Zugangsdaten eingeben, nichts anklicken. Mirko per Push melden: „Bitte im Browser der Claude-App bei Clubity anmelden (als Mirko).“ Dann beenden, `geprueft_am` nicht ändern.
4. **Abgleichen.** Schlüssel ist Feld `clubity` (exakter Titel) + `kind` + Wochentag. Für jeden Kurs in `kurse.json`:
   - gleicher Titel am gleichen Wochentag, aber andere Start- oder Endzeit: **automatisch anpassen**
   - Titel kommt nur noch an einem anderen Wochentag vor: **automatisch verschieben**
   - geänderte Altersangabe: **automatisch anpassen**
   - Titel in dieser Woche gar nicht vorhanden: **nicht löschen** (kann ein einzelner Ausfall sein), nur melden. Fehlt derselbe Kurs zwei Abgleiche in Folge, im Bericht ausdrücklich empfehlen, ihn zu entfernen.
   - neues Angebot in Clubity, das nicht in `kurse.json` steht: **nicht hinzufügen**, nur melden. Nicht melden: Titel aus der Liste `ignoriert` in `kurse.json` (bewusst ausgeschlossen, meist Fortgeschrittene) sowie Angebote ohne Kinderbezug (Badminton, Tennis, Kindergeburtstage, Freies Bouldern, Prüfungen).
   - Einträge mit Status „gebucht“ in der Meldung erwähnen, nichts daran ändern.
   - Kurse, die in der geladenen Woche als abgesagt erscheinen, in der Meldung als Ausfall mit Datum nennen.
5. **Speichern.** `geprueft_am` auf das heutige Datum setzen, `python3 build_ics.py`, Commit („Clubity-Abgleich: …“) und Push nach `main`. Nur lesen in Clubity: nie buchen, stornieren, auf Wartelisten setzen oder Einstellungen ändern.
6. **Melden** per Push, nur wenn sich etwas geändert hat oder etwas auffällt, in wenigen Zeilen: was automatisch angepasst wurde, was fehlt, was neu ist, Ausfälle der kommenden Woche. Ohne Auffälligkeiten nichts melden.

Ein zweites Sicherheitsnetz läuft in der Cloud: Liegt `geprueft_am` mehr als 14 Tage zurück, wird Mirko erinnert, den Mac mit offener Claude-App laufen zu lassen.

## Prüfung auf neue ETV-Kurspläne

Eine geplante Aufgabe in Mirkos Konto führt diese Prüfung jedes Jahr am 15. Dezember aus, um einen neuen Jahresplan früh zu bemerken, bevor dessen Termine in Clubity auftauchen. Die frühere monatliche PDF-Prüfung wurde am 22.11.2026 abgeschafft, weil der wöchentliche Clubity-Abgleich dieselben Änderungen mit verlässlicheren Daten findet. Die Prüfung kann auch jederzeit von Hand angestoßen werden („prüf, ob der ETV neue Kurspläne hat“). Sie ändert nichts im Repository; Änderungen werden erst nach Zustimmung und nach Gegenprüfung in Clubity eingespielt.

Aktuell verwendete Pläne (stehen auch unter `quellen` in `kurse.json`, Stand siehe `stand`):

- Kindersport, „Gültig ab August 2026“: https://www.etv-hamburg.de/_cache/downloads/7270-9140c03c95/cms/Verein/Kindersport/RZ_KINDERSPORTPROGRAMM-2026_Juli-1-1.pdf
- ETV Dance Kursprogramm 2026, Stand Mai: https://www.etv-hamburg.de/_cache/downloads/7100-368fa00184/cms/Abteilungen/ETV-Dance/Downloads/RZ_DANCE_Kursprogramm-2026_Mai.pdf

## Regeln für aktuelle Daten

Diese Regeln gelten für die Prüfung und für jeden Neuaufbau von `kurse.json`. Hintergrund: Am Anfang wurde `kurse.json` aus dem ersten Suchtreffer gebaut, einem Plan „gültig ab Januar 2026“, obwohl längst ein Plan „gültig ab August 2026“ online war.

0. **Maßgeblich ist der ETV-Mitgliederbereich (Clubity), nicht die PDFs.** Dort wird tatsächlich gebucht. Zugang nur mit Mirkos Anmeldung im Browser der Claude-Desktop-App: https://www.clubity.com/app/?organizationId=9, dann „Angebot“. Filter Alter (2 bzw. 6) und Orte „Sportzentrum Bundesstraße“, „Sporthalle Hohe Weide“, „Bundesstraße 103“ setzen und eine volle Woche über „Weitere Termine anzeigen“ laden. Nur lesen, nie buchen oder Konto-Einstellungen ändern. Zugangsdaten gibt Mirko selbst ein. Letzter vollständiger Abgleich steht in `kurse.json` unter `geprueft`. Die geplanten Prüfungen laufen in der Cloud ohne diesen Zugang und nutzen deshalb die Programmseiten unten; findet eine Prüfung Abweichungen, wird vor dem Übernehmen in Clubity gegengeprüft, sofern der Mac verbunden ist.
1. **Einstieg für die PDFs sind immer die offiziellen Programmseiten, nicht die Websuche.** Der dort verlinkte Plan ist der aktuelle:
   - Kindersport: https://www.etv-hamburg.de/de/sportangebot/Sportprogramme/kindersport/ (Abschnitt „Kursplan“)
   - ETV Dance: https://www.etv-hamburg.de/de/sportangebot/Sportprogramme/dance/ (Abschnitt „Dance Kursprogramm“)
   Suchtreffer können alte Fassungen, Schulkooperationen oder Ferienhefte sein. Die Websuche nur nutzen, wenn eine Programmseite nicht erreichbar ist, und das dann melden.
2. **Version immer belegen.** Bei jedem verwendeten Plan Gültigkeitsdatum oder Stand und den Link notieren, in `kurse.json` unter `quellen` und `stand` und in dieser Datei.
3. **Gleicher Link heißt kein neuer Plan.** Stimmt der auf der Programmseite verlinkte Plan mit dem hier eingetragenen überein, ist nichts zu vergleichen. Dann sofort „Keine neuen ETV-Kurspläne gefunden“ melden.
4. **Wochentage aus der besten Quelle.** Die PDFs sind beim Auslesen ohne Spaltenlayout, die Tagesüberschriften rutschen. Für Tanzkurse an der Bundesstraße liefert die athletx-Kursübersicht klare Wochentage (Link auf der Dance-Seite unter „Kursprogramm“, Sportzentrum Bundesstraße): https://etv.athletx.de/ausgabe/fitgym/static.php?hash=dj768s7d6fsdfbssdv887sdvs&schwerpunkt=Screen-Dance-BU. Altersangaben stehen nur im PDF. Beim Kindersport ergeben sich die Tage aus der Blockreihenfolge im PDF, abgeglichen mit den Ferienheften. Kurse, deren Tag sich nicht belegen lässt, in `kurse.json` mit `"unsicher": true` markieren.
5. **Bestätigungen durch Mirko oder seine Frau haben Vorrang.** Bestätigt: Hip-Hop/Streetdance 6–9 J. ist dienstags 15:00.

## Ablauf der Prüfung

1. Die beiden Programmseiten öffnen und die verlinkten Plan-PDFs mit den oben eingetragenen vergleichen. Ferienhefte (März-, Mai-, Sommer-, Herbstferien) sind keine neuen Pläne.
2. Gibt es keinen neueren Plan: kurz melden „Keine neuen ETV-Kurspläne gefunden“ und fertig.
3. Gibt es einen neueren Plan: ihn lesen und nur die Kurse vergleichen, die für das Repository relevant sind (Sportzentrum Bundesstraße und Sporthalle Hohe Weide, Altersangaben, die 2 oder 6 Jahre einschließen). Wochentage nach Regel 4 bestimmen. Mit `kurse.json` abgleichen.
4. Ergebnis als kurze Liste melden: neue Kurse, weggefallene Kurse, geänderte Zeiten, Tage oder Räume, jeweils mit Kind (2 oder 6). Unsichere Wochentage ausdrücklich als unsicher kennzeichnen. Link zum neuen PDF angeben.
5. Fragen, ob die Änderungen übernommen werden sollen. Nach Zustimmung nach dem Ablauf oben ändern und hier in diesem Abschnitt die Liste der aktuell verwendeten Pläne aktualisieren.

## Regeln

- Die .ics-Dateien nie von Hand bearbeiten.
- Niemanden neu importieren lassen; die Abo-Links bleiben gleich.
- Das Repository ist öffentlich: keine Namen, Geburtsdaten oder anderen persönlichen Daten der Kinder oder der Familie hineinschreiben.

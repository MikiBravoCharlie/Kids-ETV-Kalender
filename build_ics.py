"""Erzeugt ETV-Kurse-2-Jahre.ics und ETV-Kurse-6-Jahre.ics aus kurse.json.

Aufruf im Repo-Ordner:  python3 build_ics.py
Die UIDs sind stabil (Tag, Startzeit, Kurs, Raum), damit abonnierte Kalender
Termine aktualisieren statt sie doppelt anzulegen.
"""
import datetime as dt
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).parent
ROOM = {
    "UH": "Untere Halle", "GH": "Große Halle", "KH": "Kleine Halle",
    "Gym I": "Gymnastikraum 1", "Gym II": "Gymnastikraum 2", "Gym III": "Gymnastikraum 3",
    "Gym IV": "Gymnastikraum 4", "Gym V": "Gymnastikraum 5", "CC": "Club Céronne Saal",
}
BUNDES = "ETV Sportzentrum Bundesstraße, Bundesstraße 96, 20144 Hamburg"
VTZ = "\r\n".join([
    "BEGIN:VTIMEZONE", "TZID:Europe/Berlin",
    "BEGIN:DAYLIGHT", "TZOFFSETFROM:+0100", "TZOFFSETTO:+0200", "TZNAME:CEST",
    "DTSTART:19700329T020000", "RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU", "END:DAYLIGHT",
    "BEGIN:STANDARD", "TZOFFSETFROM:+0200", "TZOFFSETTO:+0100", "TZNAME:CET",
    "DTSTART:19701025T030000", "RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU", "END:STANDARD",
    "END:VTIMEZONE",
])


def esc(s: str) -> str:
    return s.replace("\\", "\\\\").replace(",", "\\,").replace(";", "\\;")


def main() -> None:
    data = json.loads((HERE / "kurse.json").read_text(encoding="utf-8"))
    monday = dt.date.fromisoformat(data["wochenstart"])
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    for kind in (2, 6):
        lines = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//ETV Wochenplan//DE",
                 "CALSCALE:GREGORIAN", f"X-WR-CALNAME:ETV Kurse {kind} Jahre",
                 "X-WR-TIMEZONE:Europe/Berlin", "REFRESH-INTERVAL;VALUE=DURATION:PT1H",
                 "X-PUBLISHED-TTL:PT1H", VTZ]
        count = 0
        for wd, tag in enumerate(data["tage"]):
            day = (monday + dt.timedelta(days=wd)).strftime("%Y%m%d")
            for k in tag["kurse"]:
                if k["kind"] != kind:
                    continue
                count += 1
                raum = k["raum"]
                if raum == "HW":
                    loc = "Sporthalle Hohe Weide, Hohe Weide 17a, 20259 Hamburg"
                    rname = "Sporthalle Hohe Weide" + (", Gymnastikraum A" if k["art"] == "T" else "")
                elif raum == "SP":
                    loc, rname = "ETV Sportplätze, Bundesstraße 103, 20144 Hamburg", "Sportplatz (draußen)"
                elif raum == "":
                    loc, rname = BUNDES, "siehe ETV-App"
                else:
                    loc, rname = BUNDES, ROOM.get(raum, raum)
                extra = {"T": "ETV Dance, ggf. Sonderbeitrag. ",
                         "A": "Eigene Abteilung, Anmeldung und Beitrag ggf. abweichend. "}.get(k["art"], "")
                if k.get("unsicher"):
                    extra = "Wochentag unsicher, bitte in der ETV-App prüfen. " + extra
                key = f"{kind}|{tag['tag']}|{k['start']}|{k['kurs']}|{raum}"
                uid = hashlib.sha1(key.encode()).hexdigest()[:16]
                lines += [
                    "BEGIN:VEVENT", f"UID:etv-{uid}@kids-etv-kalender", f"DTSTAMP:{stamp}",
                    f"DTSTART;TZID=Europe/Berlin:{day}T{k['start'].replace(':', '')}00",
                    f"DTEND;TZID=Europe/Berlin:{day}T{k['ende'].replace(':', '')}00",
                    "RRULE:FREQ=WEEKLY",
                    "SUMMARY:" + esc(f"{k['kurs']} ({k['alter']})"),
                    "LOCATION:" + esc(loc),
                    "DESCRIPTION:" + esc(f"Raum: {rname}. {extra}Anmeldung über die ETV-App ab 48 Std. vor Kursbeginn. Nicht in den Schulferien."),
                    "END:VEVENT",
                ]
        lines.append("END:VCALENDAR")
        out = HERE / f"ETV-Kurse-{kind}-Jahre.ics"
        out.write_text("\r\n".join(lines) + "\r\n", encoding="utf-8", newline="")
        print(out.name, count, "Termine")


if __name__ == "__main__":
    main()

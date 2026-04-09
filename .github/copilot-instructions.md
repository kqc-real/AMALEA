# Project Guidelines

Diese Anweisungen gelten für Copilot-Arbeit im gesamten AMALEA-
Repository. Halte sie knapp, verbindlich und konsistent mit den
vorhandenen Kursdokumenten.

## Quellen Der Wahrheit

Nutze diese Dateien als primäre Referenzen und halte sie bei Änderungen
konsistent:

- `README.md`
- `STUDENT_SETUP.md`
- `DEVELOPER_GUIDE.md`
- `DOZENTENLEITFADEN.md`
- `SITZUNGSPLAN_7_WOCHEN.md`
- Wochen-`README.md`-Dateien und betroffene Notebook-Intros

## Kursregeln

- Docker Compose ist der studentische Standardpfad und im Kurs Pflicht.
- Lokale Python-Umgebungen sind nur Ausweich-, Wartungs- oder
  Troubleshooting-Pfade.
- Woche 1 bis 4 bilden den stabilen Kurskern.
- Woche 5 bis 7 sind Vertiefungen mit höherem technischem Risiko.
- Woche 7 ist als Demo- und Portfolio-Kontext zu behandeln, nicht als
  produktionsreife Standardarchitektur.

## Dokumentation Und Sprache

- Studentische Materialien in idiomatischem, ruhigem und gut lesbarem
  Deutsch formulieren.
- Pflicht, Optional und Kür klar trennen.
- Bei Änderungen an studentischen Abläufen zentrale Einstiegsdokumente,
  Wochen-READMEs und relevante Notebook-Intros konsistent halten.
- Docker nie als optionalen Normalweg formulieren.

## Notebooks, Apps Und Validierung

- Notebooks mit minimalem Eingriff ändern; bei reiner Textarbeit
  bevorzugt Markdown-Zellen anpassen.
- Notebook-Zellen nur neu ausführen, wenn Code, Ausgaben oder technische
  Anleitungen betroffen sind.
- Streamlit-Apps startbar halten und nur fokussierte technische Checks
  ausführen.
- Für technische Prüfungen den kleinstmöglichen belastbaren Prüfpfad
  wählen.

## Arbeitsweise

- Vor Änderungen bestehende Repository-Dokumentation lesen, statt Regeln
  zu raten.
- Änderungen klein halten und keine unnötige Komplexität einführen.
- Für allgemeine Kursarbeit bevorzugt den Kurskontext respektieren,
  statt Einzelartefakte isoliert zu optimieren.
- Für agentenspezifische Aufgaben siehe `.github/README.md` und die
  Dateien in `.github/agents/`.
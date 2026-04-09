# Copilot-Agenten im AMALEA-Repository

Diese Übersicht beschreibt die spezialisierten Copilot-Agenten in
diesem Repository und zeigt, wann welcher Agent sinnvoll ist.

## Ziel

Die Agenten trennen drei Arten von Arbeit, die im Kurs regelmäßig
zusammenkommen, aber unterschiedliche Regeln brauchen:

- allgemeine Kurs- und Konsistenzarbeit
- sprachliche Überarbeitung studentischer Materialien
- technische Prüfungen und reproduzierbare Checks

Damit bleiben Aufgaben klar geschnitten und spätere Änderungen konsistent.

## Verfügbare Agenten

### `AMALEA-Kursassistenz`

Datei:

- `agents/amalea-kursassistenz.agent.md`

Nutze diesen Agenten für:

- Änderungen an Kursmaterialien über mehrere Dateien hinweg
- Konsistenzanpassungen zwischen zentralen Dokumenten und Wochenmaterial
- Überarbeitung von Notebooks, Streamlit-Apps und Dokumentation im
  Kurskontext
- Aufgaben, bei denen didaktische, technische und organisatorische Regeln zusammenkommen

Dieser Agent kennt den Pflichtpfad des 7-Wochen-Kurses, die
Docker-Pflicht und die zentralen didaktischen Leitlinien. Er darf bei
Bedarf an die Sprachredaktion oder den Technikcheck delegieren.

### `AMALEA-Sprachredaktion`

Datei:

- `agents/amalea-sprachredaktion.agent.md`

Nutze diesen Agenten für:

- idiomatisches Deutsch in README-Einführungen
- sprachliche Überarbeitung von Setup-Hinweisen
- bessere Lesbarkeit in Notebook-Markdown
- klarere Arbeitsaufträge, Minimalziele und
  Pflicht-Optional-Abgrenzungen

Dieser Agent ist bewusst auf Sprache, Ton, Lesefluss und
Terminologiekonsistenz begrenzt. Er ist nicht für technische Diagnosen
oder Infrastrukturentscheidungen gedacht.

### `AMALEA-Technikcheck`

Datei:

- `agents/amalea-technikcheck.agent.md`

Nutze diesen Agenten für:

- Streamlit-Smoke-Tests
- Docker- und Docker-Compose-Checks
- fokussierte Notebook- oder Requirements-Prüfungen
- kurze technische Risikoabschätzungen für den Kursbetrieb

Dieser Agent bewertet Stabilität und Reproduzierbarkeit mit möglichst
kleinen, belastbaren Prüfpfaden. Er ersetzt keine Sprachredaktion und
keine inhaltliche Kursgestaltung.

## Schnelle Auswahl

Nutze `AMALEA-Kursassistenz`, wenn du nicht nur einen Text oder nur
einen Check brauchst, sondern die eigentliche Kursarbeit im Repository
ändern oder abstimmen willst.

Nutze `AMALEA-Sprachredaktion`, wenn der Schwerpunkt auf
Verständlichkeit, Ton, studentischer Ansprache oder klarerer
Aufgabenformulierung liegt.

Nutze `AMALEA-Technikcheck`, wenn du wissen willst, ob etwas startet,
baut, läuft oder reproduzierbar geprüft werden kann.

## Kursweite Konstanten

Diese Regeln gelten unabhängig vom gewählten Agenten:

- Docker Compose ist der studentische Standardpfad und im Kurs Pflicht.
- Lokale Python-Umgebungen sind nur Ausweich- oder Troubleshooting-Pfade.
- Woche 1 bis 4 bilden den stabilen Kurskern.
- Woche 5 bis 7 sind stärker vertiefungs- und demoorientiert.
- Woche 7 wird nicht als produktionsreifer Standardpfad beschrieben.

## Praktische Beispiele

- Ein Wochen-README ist fachlich richtig, aber sprachlich holprig: `AMALEA-Sprachredaktion`
- Eine Streamlit-App soll nach einer Änderung kurz validiert werden: `AMALEA-Technikcheck`
- Mehrere Doku-Dateien und ein Notebook müssen gemeinsam an eine neue
  Kursregel angepasst werden: `AMALEA-Kursassistenz`

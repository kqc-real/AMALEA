# Deployment auf Streamlit Cloud

Dieses Dokument beschreibt, wie die Dashboards aus
`07_Deployment_Portfolio` auf Streamlit Cloud veröffentlicht werden
können. Es bezieht sich ausschließlich auf die Streamlit-Anwendungen,
nicht auf das FastAPI-Backend.

## Voraussetzungen

- ein GitHub-Konto
- ein Repository mit dem aktuellen App-Code
- eine funktionierende `requirements.cloud.txt` im Ordner `07_Deployment_Portfolio`

## Abhängigkeiten

Für Streamlit Cloud wird die Datei
`07_Deployment_Portfolio/requirements.cloud.txt` verwendet. Dort stehen
die Pakete, die für die Dashboards benötigt werden. Das Backend wird auf
Streamlit Cloud nicht mitgestartet.

## Vorgehen

1. Bei Streamlit Cloud mit dem GitHub-Konto anmelden.
1. Eine neue App anlegen.
1. Repository, Branch und App-Pfad auswählen.

Geeignete App-Pfade sind zum Beispiel:

- `07_Deployment_Portfolio/04_streamlit_mlops_dashboard.py`
- `07_Deployment_Portfolio/05_streamlit_nlp_dashboard.py`

1. Die App deployen.

## Demo-Modus und Live-Modus

- Im Demo-Modus laufen die Dashboards ohne externes Backend.
- Im Live-Modus wird eine öffentlich erreichbare API benötigt.

Falls ein externer API-Endpunkt verwendet wird, kann `API_URL` in den
Secrets gesetzt werden:

```toml
API_URL="https://dein-backend.example.com"
```

Wenn das Backend zusätzliche Authentifizierung verlangt, müssen die
entsprechenden Schlüssel ebenfalls als Secrets hinterlegt werden.

## Hinweise für den Kursbetrieb

- Für Lehrveranstaltungen ist der Demo-Modus meist die robustere Wahl.
- Der Live-Modus eignet sich vor allem für gezielte Vorführungen oder Abschlussprojekte.
- Auf Streamlit Cloud sollten keine großen Datenmengen oder unnötigen
  Artefakte mitdeployt werden.

## Typische Probleme

- **Backend nicht erreichbar**: auf Demo-Modus wechseln oder `API_URL` prüfen.
- **Fehlende Pakete**: `requirements.cloud.txt` ergänzen und neu deployen.
- **Langsame Builds**: das Repository klein halten und schwere
  Zusatzabhängigkeiten vermeiden.
- **Timeouts**: API-Aufrufe knapp halten; für Vorführungen möglichst
  kurze Requests verwenden.

## Einordnung

Das Cloud-Deployment der Dashboards ist eine sinnvolle Ergänzung für
Portfolios und Abschlussarbeiten. Für den regulären Kursbetrieb bleibt
die lokale Ausführung in der Regel einfacher und verlässlicher.

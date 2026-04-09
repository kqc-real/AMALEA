# Student Setup

Kurzfassung für Studierende: Docker ist im gesamten Kurs der
verbindliche Standard. Richtet deshalb zuerst Git und Docker Desktop
ein und startet AMALEA über Docker Compose.

## Ziel

Am Ende dieses Setups sollt ihr:

- das Repository geklont haben
- Docker Desktop funktionsfähig gestartet haben
- Jupyter Lab und die Streamlit-Umgebung per Docker Compose starten
   können
- wissen, wann ihr das Slim- und wann ihr das Full-Profil verwendet

## Vor der Installation

Ihr braucht auf beiden Plattformen mindestens diese Werkzeuge:

- Git
- Docker Desktop
- optional Python nur für technische Sonderfälle, nicht für den
   regulären Kursweg

### macOS: Werkzeuge installieren

Installiert die Werkzeuge so:

1. Git installieren:
   auf vielen Macs ist Git bereits vorhanden; sonst ueber Xcode Command
   Line Tools oder den Installer von [git-scm.com](https://git-scm.com).
2. Docker Desktop installieren:
   von [docker.com](https://www.docker.com/products/docker-desktop/) und
   nach der Installation einmal komplett starten.

Prüfen könnt ihr das mit:

```bash
git --version
docker --version
docker compose version
```

### Windows: Werkzeuge installieren

Installiert die Werkzeuge so:

1. Git installieren:
   ueber den Windows-Installer von
   [git-scm.com](https://git-scm.com/download/win).
2. Docker Desktop installieren:
   von [docker.com](https://www.docker.com/products/docker-desktop/) und
   danach Docker Desktop einmal starten.

Prüfen könnt ihr das in PowerShell mit:

```powershell
git --version
docker --version
docker compose version
```

## Standardweg

### macOS: Standardweg

```bash
git clone <repository-url>
cd amalea
docker compose --profile slim up -d jupyter-lab-slim streamlit-slim
docker compose ps
```

### Windows: Standardweg

Verwendet dafür am besten PowerShell:

```powershell
git clone <repository-url>
cd amalea
docker compose --profile slim up -d jupyter-lab-slim streamlit-slim
docker compose ps
```

## Funktionstest

Prüft direkt danach:

### macOS: Funktionstest

```bash
docker compose ps
```

### Windows: Funktionstest

```powershell
docker compose ps
```

Es sollten mindestens `jupyter-lab-slim` und `streamlit-slim` als
laufend erscheinen.

## Minimaler Starttest

Öffnet danach im Browser:

- Jupyter Lab: `http://localhost:8889`
- Streamlit: `http://localhost:8502`

Wenn beide Oberflächen erreichbar sind, ist eure Umgebung korrekt
eingerichtet.

## Welches Profil Gilt Wann?

- Woche 1 bis 4: Slim-Profil
- Woche 4 mit MLflow sowie Woche 5 bis 7: Full-Profil

### Full-Profil starten

### Full-Profil auf macOS

```bash
docker compose --profile full up -d
```

### Full-Profil auf Windows

```powershell
docker compose --profile full up -d
```

Danach sind typischerweise diese Ports relevant:

- Jupyter Full: `http://localhost:8888`
- Streamlit Full: `http://localhost:8501`
- MLflow: `http://localhost:5001`

## Umgebung Beenden

### Umgebung auf macOS beenden

```bash
docker compose down
```

### Umgebung auf Windows beenden

```powershell
docker compose down
```

## Wichtige Regel

Docker ist im gesamten Kurs Pflicht. Lokale Python- oder `.venv`-Setups
sind kein regulärer Studierendenpfad.

## Wenn Etwas Nicht Startet

1. Prüft zuerst, ob Docker Desktop wirklich läuft.
2. Prüft dann `docker --version`, `docker compose version` und
   `docker compose ps`.
3. Startet den Pflichtpfad erneut mit
   `docker compose --profile slim up -d jupyter-lab-slim streamlit-slim`.
4. Wenn ein Port belegt ist, beendet den alten Prozess oder den bereits
   laufenden Container.
5. Nutzt lokale Python-Setups nur nach Rücksprache als technisches
   Troubleshooting.

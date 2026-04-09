<!-- markdownlint-disable MD013 MD022 MD031 MD032 MD058 MD060 -->
# Developer Guide

Technische Dokumentation für Aufbau, Betrieb und Entwicklung der
AMALEA-Umgebung. Das Haupt-README bleibt bewusst allgemeiner und stärker
auf den Kursablauf ausgerichtet. Für die konkrete Kursdurchführung
ergänzt [DOZENTENLEITFADEN.md](DOZENTENLEITFADEN.md) diese Datei.

Für Studierende ist das Haupt-README die primäre Einstiegshilfe. Die
dortige studentische Setup-Anleitung beschreibt jetzt den
verbindlichen Docker-Compose-Pfad fuer den Kurs. Diese Datei ist bewusst
technischer und ergänzt den studentischen Pfad um Betriebs-,
Fallback- und Troubleshooting-Details.

Für Copilot-gestützte Maintainer-Arbeit sind zusätzlich die Dateien
unter `.github/` relevant:

- [.github/README.md](.github/README.md): Übersicht über Rollen,
  Einsatzbereiche und Abgrenzung der Kursagenten.
- [.github/copilot-instructions.md](.github/copilot-instructions.md):
  immer geltende Workspace-Regeln für Copilot im Repository.
- [.github/agents](.github/agents): konkrete Agent-Dateien für
  Kursassistenz, Sprachredaktion und Technikcheck.

## Inhalt
- [Architektur & Module](#architektur--module)
- [Lokale Entwicklung (Technischer Ausnahmefall)](#lokale-entwicklung-technischer-ausnahmefall)
- [Container & Services (Docker Compose)](#container--services-docker-compose)
- [MLflow Nutzung](#mlflow-nutzung)
- [Ports, Volumes & Umgebungsvariablen](#ports-volumes--umgebungsvariablen)
- [Tests & Qualitätssicherung](#tests--qualitätssicherung)
- [Troubleshooting (technisch)](#troubleshooting-technisch)

---
## Architektur & Module

| Ebene | Beschreibung | Beispiele |
|-------|--------------|-----------|
| Kurs Notebooks | Lern- und Demonstrationsinhalte (Jupyter Notebooks) | `01_Python_Grundlagen/` bis `07_Deployment_Portfolio/` |
| Streamlit Apps | Interaktive Web-Anwendungen für ML-Modelle | `iris_ml_app.py`, `housing_regression_app.py` |
| Executed Notebooks | Referenzfassungen und erzeugte Ausgaben | `.nbconvert.ipynb`, `executed/`, `executed_notebooks/` |
| Datasets & Tests | Daten für Übungen und Qualitätssicherung | `datasets/`, `tests/` |

Die modulare Struktur ermöglicht wochenspezifische Installationen und
einen schrittweisen Betrieb im Kurs.

---
## Lokale Entwicklung (Technischer Ausnahmefall)

Fuer direkte lokale Entwicklung ohne Containerisierung. Dieser Pfad ist
nicht der studentische Kursstandard, sondern fuer Wartung,
Troubleshooting oder gezielte lokale Analysen gedacht:

```bash
# 1. Virtuelle Umgebung erstellen und aktivieren
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux; Windows: .venv\Scripts\activate

# 2. Abhängigkeiten installieren (Basis-Stack)
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

# 3. Jupyter Lab starten
jupyter lab

# 4. Streamlit-App starten (Beispiel)
streamlit run 02_Streamlit_und_Pandas/example_app.py
```

### Optionale Kernel-Registrierung
Für persistente Jupyter-Kernel:
```bash
python -m ipykernel install --user --name amalea-venv \
  --display-name "Python (AMALEA)"
```

### Wochenspezifische Installationen
- **Wochen 01–03 (Basis)**: `pip install -r requirements.txt`
- **Woche 04 (Advanced Algorithms)**: `pip install -r requirements-week04.txt`
- **Woche 05 (Deep Learning)**: `pip install -r requirements-week05.txt`
- **Woche 06 (CV/NLP)**: `pip install -r requirements-week06.txt`
- **Woche 07 (Deployment-Demo)**: `pip install -r requirements-week07.txt`

---
## Container & Services (Docker Compose)

`docker-compose.yml` definiert Services mit Profiles für flexible
Konfigurationen.

| Service | Zweck | Port (Host) | Profil | Abhängigkeiten |
|---------|------|-------------|--------|---------------|
| `jupyter-lab` | Vollständige Data/ML-Umgebung | 8888 | `full` | TF, Torch, OpenCV |
| `jupyter-lab-slim` | Leichtgewicht (ohne TF/Torch/OpenCV) | 8889 | `slim` | Basis-Stack |
| `streamlit-dev` | Vollständige Streamlit-Entwicklung | 8501 | `full` | Alle Deps |
| `streamlit-slim` | schlanke Streamlit-Umgebung | 8502 | `slim` | Minimale Deps |
| `mlflow` | Experiment-Tracking-Server | 5001 (→ 5000) | `full` | MLflow ≥3.7.0 |
| `postgres` | Datenbank für fortgeschrittene Übungen | 5432 | `full` | PostgreSQL 15 |

### Start-Befehle
```bash
# Alle Services starten
docker compose up -d

# Nur Full-Profile (vollständige Umgebung)
docker compose --profile full up -d

# Nur Slim-Profile (schnell & leicht)
docker compose --profile slim up -d

# Spezifische Services
docker compose up -d jupyter-lab-slim streamlit-slim
```

### Logs & Management
```bash
# Logs anzeigen (alle Services)
docker compose logs -f --tail=120

# Spezifische Logs
docker compose logs -f streamlit-dev

# Services neu bauen (nach Dependency-Änderungen)
docker compose build --no-cache streamlit-dev

# Stop & Cleanup
docker compose down
docker compose down --volumes  # inkl. Datenlöschung
```

### Sicherheitshinweise
- Jupyter läuft ohne Token/Passwort für Entwicklung – nicht für
  öffentlich erreichbare Systeme verwenden.
- Streamlit-Apps sind remote zugänglich – prüfe Firewall-Einstellungen.
- PostgreSQL verwendet Standard-Credentials – ändere für sensible Deployments.
- Vulnerability-Hinweise auf den Docker-Basisimages stammen derzeit aus
  den Upstream-Images `jupyter/scipy-notebook` und `python:3.12-slim`.
  Für den Kursbetrieb blockieren sie die Installierbarkeit nicht; sie
  sollten über regelmäßige Digest- oder Tag-Updates beobachtet werden.

### Empfohlener Kursstandard

Für den regulären Lehrbetrieb ist folgende Kombination derzeit am
robustesten:

- Docker Compose ist der verbindliche Kursstandard.
- Woche 1 bis 4 laufen standardmaessig im Slim-Profil.
- Fuer MLflow, Deep Learning und spaetere Deployment-Inhalte wird das
  Full-Profil verwendet.
- Lokale Python-Umgebungen bleiben ein technischer Ausnahmeweg.
- Woche 7 wird standardmaessig weiter im Demo-Modus ohne Transformers
  betrieben.

---
## MLflow Nutzung

MLflow dient als zentrales Laborbuch für Experimente.

| Kontext | URI | Verwendung |
|---------|-----|------------|
| Host (lokal) | `http://localhost:5001` | Browser-Zugriff, lokale Entwicklung |
| Container | `http://mlflow:5000` | Innerhalb von Docker-Services |
| Fallback (ohne Server) | `file:./mlruns` | Lokale Datei-Speicherung |

### Minimales Code-Beispiel
```python
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Tracking URI setzen
mlflow.set_tracking_uri("http://localhost:5001")  # oder file:./mlruns

# Experiment definieren
mlflow.set_experiment("Iris Classification")

with mlflow.start_run():
    # Daten laden
    X, y = load_iris(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Modell trainieren
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Vorhersagen & Metriken
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    # Logging
    mlflow.log_param("n_estimators", 100)
    mlflow.log_metric("accuracy", accuracy)
    mlflow.sklearn.log_model(model, "model")

print(f"Accuracy: {accuracy:.4f}")
```

### Artefakte & Reset
- **Artefakte**: Gespeichert in Volume `mlflow-data` (Ordner `/mlflow/artifacts`).
- **Reset aller Runs** (Vorsicht: Datenverlust):
```bash
docker compose down mlflow
docker volume rm $(docker volume ls -q | grep mlflow)
docker compose up -d mlflow
```

### Erweiterte Features
- **Model Registry**: für spätere Staging- oder Übergabe-Szenarien;
  im Basis-Setup nicht aktiviert.
- **UI-Zugriff**: [http://localhost:5001](http://localhost:5001) für Experiment-Vergleiche.

---
## Ports, Volumes & Umgebungsvariablen

### Ports
| Service | Intern | Extern | Zweck |
|---------|--------|--------|-------|
| jupyter-lab | 8888 | 8888 | Jupyter Lab Interface |
| jupyter-lab-slim | 8888 | 8889 | Slim Jupyter Lab |
| streamlit-dev | 8501 | 8501 | Streamlit Apps |
| streamlit-slim | 8501 | 8502 | Slim Streamlit |
| mlflow | 5000 | 5001 | MLflow UI |
| postgres | 5432 | 5432 | Datenbank |

### Volumes
| Volume | Mount / Pfad | Zweck | Persistent |
|--------|-------------|-------|------------|
| `./:/workspace` oder `./:/app` | Code-Sync | Live-Entwicklung | Nein |
| `jupyter-data` | `/home/jovyan/.jupyter` | Jupyter-Settings | Ja |
| `mlflow-data` | `/mlflow` | SQLite + Artefakte | Ja |
| `postgres-data` | `/var/lib/postgresql/data` | DB-Daten | Ja |

```bash
# Volumes prüfen
docker volume ls

# Einzelnes Volume löschen (Datenverlust!)
docker volume rm mlflow-data
```

### Umgebungsvariablen
`.env` wird automatisch von Docker Compose geladen:

```bash
# Beispiel-Inhalte (.env)
MC_TEST_ADMIN_USER=Admin
MC_TEST_ADMIN_KEY=Admin
JUPYTER_TOKEN=amalea2025
MLFLOW_TRACKING_URI=http://localhost:5001
POSTGRES_DB=iu_analytics
POSTGRES_USER=student
POSTGRES_PASSWORD=data_science_2025
```

### Streamlit Secrets
Für Cloud-Deployment: `.streamlit/secrets.toml` (alle Werte als Strings):

```toml
[api_keys]
openai = "your-openai-api-key-here"
huggingface = "your-huggingface-token-here"

[database]
host = "localhost"
port = "5432"
user = "student"
password = "data_science_2025"
database = "iu_analytics"

[mlflow]
tracking_uri = "http://localhost:5001"
```

**Hinweis**: Ersetze Platzhalter mit echten Werten. Für lokale
Entwicklung kann die Datei nach `~/.streamlit/secrets.toml` kopiert
werden.

### W07: Demo-Modus und optionaler Transformers-Modus

Das Backend in Woche 7 ist standardmäßig auf einen stabilen Demo-Betrieb
ausgelegt.

- `/predict` arbeitet mit einem lokal trainierten Iris-Modell.
- `/sentiment`, `/qa` und `/generate` nutzen standardmäßig einen
  heuristischen Demo-Modus.
- Damit bleibt das Backend ohne große Modell-Downloads startbar.

Wenn reale Hugging-Face-Pipelines gezeigt werden sollen, ist ein
erweiterter Modus möglich:

```bash
cd 07_Deployment_Portfolio
pip install -r ../requirements-week07-transformers.txt
export AMALEA_ENABLE_TRANSFORMERS=1
uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload
```

Für den regulären Kursbetrieb ist der Demo-Modus meist robuster.

---
## Tests & Qualitätssicherung

### Automatisierte Workflows (Makefile)
Verwende `Makefile` für konsistente Tasks:

```bash
# Abhängigkeiten installieren
make install

# Code linten (Ruff)
make lint

# Code formatieren (Black)
make fmt

# Tests ausführen (Pytest)
make test

# Smoke-Tests für Notebooks
make smoke-notebooks
```

### Test-Struktur
- **Unit-Tests**: `tests/test_backend.py` für Backend-Logik.
- **Integration**: Docker-Compose für End-to-End-Tests.
- **Qualität**: Ruff für Linting, Black für Formatierung, Pytest für Tests.

### Manuelle Tests
```bash
# Abhängigkeiten installieren
pip install -r requirements-dev.txt

# Tests ausführen
python -m pytest tests/ -v

# Coverage (optional)
pip install pytest-cov
python -m pytest tests/ --cov=07_Deployment_Portfolio --cov-report=html
```

---
## Troubleshooting (technisch)

| Problem | Diagnose | Lösung |
|---------|----------|--------|
| Kein Auto-Reload in Jupyter | File-Events langsam (Host) | Manuell reload; Full- statt Slim-Image verwenden |
| Port belegt | `lsof -i :8501` zeigt Prozess | `kill -9 <PID>` oder Port ändern |
| MLflow leer | URI falsch | `mlflow.get_tracking_uri()` prüfen; auf `file:./mlruns` zurückfallen |
| Schreibfehler CSV | Lock-Konflikt | Retry; Lock-Datei entfernen (letztes Mittel) |
| Container startet nicht | Logs prüfen | `docker compose logs <service>`; Dependencies checken |
| Streamlit-Fehler | Secrets fehlen | `.streamlit/secrets.toml` anlegen oder prüfen |
| PostgreSQL Verbindung | Credentials falsch | `.env` prüfen; Container neu starten |

### Logs & Debugging
```bash
# Alle Services
docker compose ps

# Spezifische Logs
docker compose logs --tail=60 streamlit-dev

# Container shell
docker compose exec streamlit-dev bash
```

### Häufige Issues
- **Jupyter Token**: Setze `JUPYTER_TOKEN` in `.env` für Sicherheit.
- **MLflow Version**: Stelle sicher, dass MLflow ≥3.7.0 installiert ist.
- **Dependencies**: Bei Build-Fehlern: `docker compose build --no-cache`.

- **W07 importiert langsam**: Prüfe, ob `AMALEA_ENABLE_TRANSFORMERS`
  gesetzt ist. Für den Standardbetrieb sollte die Variable nicht gesetzt
  sein.

---

**Letzte Aktualisierung:** 8. April 2026  
**Version:** 1.2 – Technisch konsolidiert für den aktuellen Kursstand.

<!-- markdownlint-disable MD013 -->
# Installation und Validierungsstatus

Diese Datei fasst kompakt zusammen, welche Installationspfade im
Repository vorgesehen sind, welche Kombinationen empfohlen werden und
welche in der aktuellen Überarbeitung praktisch geprüft wurden.

Stand: 8. April 2026.

## Empfohlener Standard

Für den regulären Kursbetrieb ist derzeit dieser Pfad am robustesten:

- Docker Compose als verpflichtenden Studierendenpfad verwenden
- Woche 1 bis 4 standardmaessig im Slim-Profil starten
- fuer MLflow sowie Woche 5 bis 7 bei Bedarf auf das Full-Profil wechseln
- lokale Python-Installationen nur als technischen Ausnahmefall nutzen
- Woche 7 standardmäßig im Demo-Modus ohne Transformers betreiben

## Technische Referenz: Lokale Installationen

Die folgenden lokalen Installationen bleiben fuer Wartung,
Troubleshooting und gezielte Einzeltests dokumentiert. Sie sind nicht
der primaere Studierendenpfad.

### Basis und Wochen-Stacks

Die folgenden lokalen Installationen wurden in frischen virtuellen
Umgebungen geprüft:

| Ziel | Datei | Python 3.12 | Python 3.13 | Hinweis |
| --- | --- | --- | --- | --- |
| Basis-Stack | `requirements.txt` | OK | OK | sinnvoll für den leichten Einstieg |
| Woche 1 | `requirements-week01.txt` | OK | nicht separat geprüft | Python-Grundlagen |
| Woche 2 | `requirements-week02.txt` | OK | nicht separat geprüft | Streamlit und Pandas |
| Woche 3 | `requirements-week03.txt` | OK | nicht separat geprüft | klassisches ML |
| Woche 4 | `requirements-week04.txt` | OK | nicht separat geprüft | Advanced Algorithms und MLflow |
| Woche 5 | `requirements-week05.txt` | OK | nicht separat geprüft | TensorFlow-Standardpfad |
| Woche 6 | `requirements-week06.txt` | OK | nicht separat geprüft | CV und NLP |
| Woche 7 | `requirements-week07.txt` | OK | OK | Demo-Betrieb ohne Transformers |
| Cloud-Stack | `requirements.cloud.txt` | OK | OK | schlanker W07-/Deployment-Pfad |
| Jupyter Slim | `requirements.jupyter-slim.txt` | OK | nicht separat geprüft | leichte Notebook-Umgebung |
| Streamlit Slim | `requirements.streamlit.txt` | OK | nicht separat geprüft | leichte App-Umgebung |

### Optionale Zusatz-Stacks

Diese optionalen Erweiterungen wurden ebenfalls separat geprüft:

| Ziel | Datei | Status | Hinweis |
| --- | --- | --- | --- |
| Woche 5 mit PyTorch | `requirements-week05-torch.txt` | OK unter Python 3.12 | PyTorch ist bewusst nicht mehr Teil des Default-Stacks |
| Woche 7 mit Transformers | `requirements-week07-transformers.txt` | OK unter Python 3.12 | für reale HF-Pipelines, deutlich schwergewichtiger |

## Docker-Installationen

Die folgenden Docker-Builds wurden praktisch angestoßen:

| Ziel | Datei | Status | Hinweis |
| --- | --- | --- | --- |
| Streamlit Slim | `Dockerfile.streamlit-slim` | OK | leichter Containerpfad |
| Jupyter Slim | `Dockerfile.jupyter-slim` | OK | leichter Notebook-Pfad |
| Streamlit Full | `Dockerfile.streamlit` | OK | geprüft mit `REQS_FILE=requirements-week07.txt` |
| Jupyter Full | `Dockerfile.jupyter` | OK auf disk-sicherem Pfad | geprüft mit `REQS_FILE=requirements-week06.txt` und `EXTRA_REQS_FILE=requirements-week07.txt`; letzter Nachlauf mit Zusatzcheck war noch offen |

Hinweise zum Full-Jupyter-Build:

- Das Basisimage `jupyter/scipy-notebook` bringt eigene Python-Pakete mit,
  die für den Kurs-Stack teilweise entfernt oder ersetzt werden müssen.
- `conda update` wurde bewusst entfernt, weil es im Upstream-Image zu
  Solver-Problemen führte.
- `numba` und das alte `pyOpenSSL` werden vorab entfernt, danach wird ein
  kompatibles `pyOpenSSL` wieder installiert.
- Ein zusätzlicher finaler `pip check` wurde ergänzt; falls genau dieser
  letzte Stand erneut bestätigt werden soll, sollte der Full-Build noch
  einmal komplett durchlaufen.
- Upstream-Vulnerability-Hinweise auf das Basisimage bleiben bestehen,
  blockieren den Build aber nicht.

## Konkrete Installationspfade

### Docker Slim

```bash
docker compose --profile slim up -d jupyter-lab-slim streamlit-slim
```

### Docker Full

```bash
docker compose --profile full up -d
```

### Lokaler Schnellstart (Technischer Ausnahmefall)

```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

### Woche 4 lokal

```bash
pip install -r requirements-week04.txt
```

### Woche 5 lokal

```bash
pip install -r requirements-week05.txt
```

Optional mit PyTorch:

```bash
pip install -r requirements-week05-torch.txt
```

### Woche 7 lokal

Standard:

```bash
pip install -r requirements-week07.txt
```

Optional mit Transformers:

```bash
pip install -r requirements-week07-transformers.txt
export AMALEA_ENABLE_TRANSFORMERS=1
```

## Interpretation der Matrix

- `OK` bedeutet: in dieser Überarbeitung praktisch installiert oder gebaut.
- `nicht separat geprüft` bedeutet: nicht gesondert in einer frischen
  Umgebung verifiziert, aber vom dokumentierten Requirements-Aufbau
  abgedeckt.
- Fuer den Kursbetrieb startet ihr zuerst den Docker-Pflichtpfad und
  waehlt dann das kleinste passende Compose-Profil fuer das jeweilige
  Lernziel.

## Verwandte Dokumente

- [README.md](README.md): Einstieg und Kurzüberblick
- [DEVELOPER_GUIDE.md](DEVELOPER_GUIDE.md): technischer Betriebspfad
- [05_Neural_Networks/README.md](05_Neural_Networks/README.md): Woche 5
  mit optionalem PyTorch
- [07_Deployment_Portfolio/README.md](07_Deployment_Portfolio/README.md):
  Woche 7 mit Demo- und Transformers-Modus

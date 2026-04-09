# Woche 2: Streamlit und Pandas

Woche 2 zeigt, wie aus Datenanalyse eine einfache interaktive Anwendung
wird. Der Schwerpunkt liegt auf Pandas, dem Ausführungsmodell von
Streamlit und dem Aufbau kleiner Dashboards.

## Lernziele

- Daten mit Pandas effizient verarbeiten
- das Streamlit-Rerun-Modell verstehen
- einfache Interaktionselemente gezielt einsetzen
- kleine Datenansichten und Visualisierungen in einer App zusammenführen

## Materialien

- `01_Erste_Streamlit_App_fixed.ipynb`: Einführung in Streamlit,
  Datenfluss und Vektorisierung
- `example_app.py`: Referenz-App mit Struktur, Caching und typischen Widgets
- `hello_streamlit.py`: kompakter Einstieg in einfache Streamlit-Komponenten

## Empfohlene Reihenfolge

1. `01_Erste_Streamlit_App_fixed.ipynb`
2. `hello_streamlit.py`
3. `example_app.py`

## Start

### Docker-Standardpfad

```bash
cd ..
docker compose --profile slim up -d jupyter-lab-slim streamlit-slim
```

Für Woche 2 arbeitet ihr in der Regel über die vorbereitete Docker-
Umgebung und startet Streamlit anschließend im passenden Ordner.

### Streamlit-App starten

```bash
cd 02_Streamlit_und_Pandas
streamlit run example_app.py
```

### Lokaler Zusatzpfad (nur technischer Ausnahmefall)

```bash
cd 02_Streamlit_und_Pandas
pip install -r requirements.txt
streamlit run example_app.py
```

## Hinweise

- Streamlit führt das Skript bei jeder Interaktion erneut aus. Dieser
  Ablauf sollte in Übungen explizit thematisiert werden.
- Für den regulären Kursbetrieb bleibt Docker auch in Woche 2 der
  Standardpfad.
- Für größere Datenmengen sind Vektorisierung und Caching wichtiger als
  komplexe Oberflächen.
- Für erste Übungen reicht meist `hello_streamlit.py`;
  `example_app.py` eignet sich besser als Referenz für Struktur und
  Ausbau.

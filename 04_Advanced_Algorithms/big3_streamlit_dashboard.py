import os
import streamlit as st
from pathlib import Path
import requests

st.set_page_config(page_title="AMALEA Big‑3 Dashboard", page_icon="📊", layout="wide")

st.title("📊 AMALEA — Big 3 Algorithms (Dashboard)")
st.write("Kurzüberblick: Dashboard, MLflow‑Links und Zugriff auf das registrierte / lokale Modell.")

# --- Dashboard image ---
img_path = Path("04_Advanced_Algorithms/outputs/big3_dashboard.png")
if img_path.exists():
    st.subheader("Performance Dashboard")
    # use explicit width (use_column_width deprecated)
    st.image(str(img_path), width=920)
    with st.expander("Datei-Info"):
        st.write(f"`{img_path}` — {img_path.stat().st_size:,} bytes")
else:
    st.error(f"Dashboard-Bild nicht gefunden unter: {img_path}")

# --- MLflow links & runs ---
st.subheader("MLflow Experiment")
MLFLOW_URI = os.getenv("MLFLOW_TRACKING_URI", "http://localhost:5001")
st.write("MLflow Tracking URI:", MLFLOW_URI)

# Quick connectivity check to avoid long blocking calls when MLflow is down
def mlflow_reachable(uri: str, timeout: float = 1.0) -> bool:
    if not uri.startswith("http"):
        return True  # file store or other non-http URIs are considered 'local'
    try:
        resp = requests.get(uri, timeout=timeout)
        return resp.status_code < 500
    except Exception:
        return False

if mlflow_reachable(MLFLOW_URI, timeout=0.8):
    try:
        import mlflow
        from mlflow.tracking import MlflowClient

        mlflow.set_tracking_uri(MLFLOW_URI)
        client = MlflowClient()
        exp = client.get_experiment_by_name("AMALEA_2025_Big3_Algorithms")
        if exp is None:
            st.info("Kein MLflow-Experiment gefunden (AMALEA_2025_Big3_Algorithms).")
        else:
            st.markdown(f"**Experiment:** `{exp.name}` (id={exp.experiment_id})")
            try:
                runs = client.search_runs(exp.experiment_id, order_by=["attributes.start_time DESC"], max_results=10)
            except Exception as e:
                st.warning(f"Fehler beim Abrufen der Runs: {e}")
                runs = []

            if runs:
                st.write("Letzte MLflow‑Runs:")
                for r in runs:
                    run_link = None
                    if MLFLOW_URI.startswith("http"):
                        run_link = f"{MLFLOW_URI.rstrip('/')}/#/experiments/{exp.experiment_id}/runs/{r.info.run_id}"
                    st.markdown(f"- **{r.info.run_id[:8]}** — status: `{r.info.status}` — metrics: {r.data.metrics} " + (f"[UI]({run_link})" if run_link else ""))
            else:
                st.info("Keine Runs im Experiment gefunden.")

    except Exception as e:
        st.warning(f"MLflow-Client Fehler: {e}")
else:
    st.info("MLflow-Server nicht erreichbar — überspringe Remote-Abfrage (verwende lokales FileStore / Joblib-Fallback).")

# --- Model download / example inference ---
st.subheader("Modellzugriff")
local_model = Path("04_Advanced_Algorithms/outputs/AMALEA_Best_Classifier.joblib")
if local_model.exists():
    st.write(f"Lokales Modell vorhanden: `{local_model}`")
    with st.expander("Modell testen (Beispielvorhersage)"):
        import joblib
        import numpy as np
        mdl = joblib.load(local_model)
        sepal_length = st.number_input("sepal_length", 4.0, 8.0, 5.8)
        sepal_width = st.number_input("sepal_width", 2.0, 4.5, 3.0)
        petal_length = st.number_input("petal_length", 1.0, 7.0, 4.3)
        petal_width = st.number_input("petal_width", 0.1, 2.5, 1.3)
        if st.button("Vorhersage mit lokalem Modell"):
            x = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
            pred = mdl.predict(x)
            st.success(f"Vorhersage: {pred[0]}")
    with open(local_model, "rb") as f:
        st.download_button("Modell herunterladen (joblib)", f, file_name=local_model.name)
else:
    st.info("Kein lokales Fallback-Modell gefunden.")

st.sidebar.header("Aktionen")
st.sidebar.markdown("- Öffne MLflow UI (falls lokal): `http://localhost:5001`\n- Nutze `MLFLOW_TRACKING_URI` für Remote-Server.")

st.sidebar.markdown("---")
st.sidebar.write("💡 Tipp: Setze `MLFLOW_TRACKING_URI` in den Streamlit‑Cloud‑Secrets, wenn du die Registry verwenden willst.")

import sys
from pathlib import Path

from fastapi.testclient import TestClient

# Ensure backend package is importable
BACKEND_ROOT = Path(__file__).resolve().parents[1] / "07_Deployment_Portfolio"
sys.path.insert(0, str(BACKEND_ROOT))

from backend.main import app  # noqa: E402

client = TestClient(app)


def test_health_ok():
    resp = client.get("/health")
    assert resp.status_code == 200
    body = resp.json()
    assert body.get("status") == "ok"
    assert body.get("model_loaded") is True
    assert body.get("target_classes")
    assert body.get("nlp_mode") in {"heuristic", "transformers"}


def test_predict_iris():
    payload = {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2,
    }
    resp = client.post("/predict", json=payload)
    assert resp.status_code == 200
    body = resp.json()
    assert body["prediction_label"] in body["target_classes"]
    assert 0.0 <= body["confidence"] <= 1.0


def test_sentiment_demo_response():
    resp = client.post("/sentiment", json={"text": "good day"})
    assert resp.status_code == 200
    assert resp.json()["label"] == "POSITIVE"


def test_qa_demo_response():
    resp = client.post("/qa", json={"context": "Sky is blue.", "question": "What color?"})
    assert resp.status_code == 200
    assert "answer" in resp.json()

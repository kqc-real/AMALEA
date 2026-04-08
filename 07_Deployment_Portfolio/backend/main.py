from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from functools import lru_cache
import os
import re
from typing import Any, List

import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel, Field
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


@dataclass
class IrisService:
    pipeline: Pipeline
    target_names: List[str]
    version: str = "0.1.0"

    @classmethod
    def create(cls) -> "IrisService":
        iris = load_iris()
        X_train, _, y_train, _ = train_test_split(
            iris.data, iris.target, test_size=0.2, random_state=42
        )
        pipe = Pipeline(
            [
                ("scaler", StandardScaler()),
                ("clf", LogisticRegression(max_iter=200)),
            ],
            memory=None,
        )
        pipe.fit(X_train, y_train)
        return cls(pipeline=pipe, target_names=list(iris.target_names))

    def predict(self, features: List[float]) -> dict:
        arr = np.array(features, dtype=float).reshape(1, -1)
        probs = self.pipeline.predict_proba(arr)[0]
        idx = int(np.argmax(probs))
        now_utc = datetime.now(timezone.utc)
        return {
            "prediction_label": self.target_names[idx],
            "confidence": float(probs[idx]),
            "timestamp": now_utc.isoformat(),
            "target_classes": self.target_names,
            "model_version": self.version,
        }


class PredictRequest(BaseModel):
    sepal_length: float = Field(..., ge=0)
    sepal_width: float = Field(..., ge=0)
    petal_length: float = Field(..., ge=0)
    petal_width: float = Field(..., ge=0)


class PredictResponse(BaseModel):
    prediction_label: str
    confidence: float
    timestamp: str
    target_classes: List[str]
    model_version: str


class SentimentRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=1000)


class SentimentResponse(BaseModel):
    label: str
    confidence: float


class QARequest(BaseModel):
    context: str = Field(..., min_length=1, max_length=2000)
    question: str = Field(..., min_length=1, max_length=200)


class QAResponse(BaseModel):
    answer: str
    confidence: float


class GenerateRequest(BaseModel):
    prompt: str = Field(..., min_length=1, max_length=400)
    max_length: int = Field(50, ge=10, le=200)
    temperature: float = Field(0.7, ge=0.1, le=1.2)


class GenerateResponse(BaseModel):
    generated_texts: List[str]
    model_info: str


SENTIMENT_MODEL_ID = "distilbert-base-uncased-finetuned-sst-2-english"
QA_MODEL_ID = "distilbert-base-cased-distilled-squad"
GEN_MODEL_ID = "sshleifer/tiny-gpt2"
ENABLE_TRANSFORMERS = os.getenv("AMALEA_ENABLE_TRANSFORMERS", "").lower() in {
    "1",
    "true",
    "yes",
    "on",
}
POSITIVE_WORDS = {
    "good",
    "great",
    "excellent",
    "happy",
    "love",
    "like",
    "success",
    "clear",
    "strong",
    "positive",
}
NEGATIVE_WORDS = {
    "bad",
    "poor",
    "sad",
    "hate",
    "angry",
    "weak",
    "negative",
    "problem",
    "fail",
    "broken",
}


def nlp_mode() -> str:
    if ENABLE_TRANSFORMERS:
        return "transformers"
    return "heuristic"


def load_hf_pipeline() -> Any:
    if not ENABLE_TRANSFORMERS:
        return None
    try:
        from transformers import pipeline as pipeline_factory
    except Exception:
        return None

    return pipeline_factory


def tokenize(text: str) -> List[str]:
    return re.findall(r"[\wäöüÄÖÜß-]+", text.lower())


def heuristic_sentiment(text: str) -> SentimentResponse:
    tokens = tokenize(text)
    positive_hits = sum(token in POSITIVE_WORDS for token in tokens)
    negative_hits = sum(token in NEGATIVE_WORDS for token in tokens)

    if negative_hits > positive_hits:
        label = "NEGATIVE"
    else:
        label = "POSITIVE"

    total_hits = positive_hits + negative_hits
    if total_hits == 0:
        confidence = 0.55
    else:
        confidence = min(0.55 + abs(positive_hits - negative_hits) / total_hits * 0.35, 0.9)
    return SentimentResponse(label=label, confidence=float(confidence))


def heuristic_qa(context: str, question: str) -> QAResponse:
    sentences = [segment.strip() for segment in re.split(r"(?<=[.!?])\s+", context) if segment.strip()]
    if not sentences:
        return QAResponse(answer="", confidence=0.0)

    question_tokens = set(tokenize(question))
    best_sentence = sentences[0]
    best_overlap = -1
    for sentence in sentences:
        overlap = len(question_tokens.intersection(tokenize(sentence)))
        if overlap > best_overlap:
            best_overlap = overlap
            best_sentence = sentence

    confidence = 0.45 if best_overlap <= 0 else min(0.45 + best_overlap * 0.1, 0.85)
    return QAResponse(answer=best_sentence, confidence=float(confidence))


def heuristic_generate(prompt: str, max_length: int) -> GenerateResponse:
    completion = (
        f"{prompt.strip()}\n\n"
        "Diese Demo ergänzt den Prompt mit einer kurzen, lokalen Beispielantwort. "
        "Für realistische Generierung kann optional der Transformers-Modus aktiviert werden."
    )
    words = completion.split()
    trimmed = " ".join(words[:max_length])
    return GenerateResponse(generated_texts=[trimmed], model_info="heuristic-demo")


@lru_cache(maxsize=1)
def get_sentiment_pipeline():
    if nlp_mode() != "transformers":
        return None
    pipeline_factory = load_hf_pipeline()
    if pipeline_factory is None:
        return None
    return pipeline_factory("sentiment-analysis", model=SENTIMENT_MODEL_ID)


@lru_cache(maxsize=1)
def get_qa_pipeline():
    if nlp_mode() != "transformers":
        return None
    pipeline_factory = load_hf_pipeline()
    if pipeline_factory is None:
        return None
    return pipeline_factory("question-answering", model=QA_MODEL_ID)


@lru_cache(maxsize=1)
def get_generate_pipeline():
    if nlp_mode() != "transformers":
        return None
    pipeline_factory = load_hf_pipeline()
    if pipeline_factory is None:
        return None
    return pipeline_factory("text-generation", model=GEN_MODEL_ID)


app = FastAPI(title="AMALEA Demo API", version="0.1.0")
iris_service = IrisService.create()


@app.get("/health")
def health():
    return {
        "status": "ok",
        "model_version": iris_service.version,
        "model_loaded": True,
        "target_classes": iris_service.target_names,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "nlp_mode": nlp_mode(),
        "transformers_enabled": ENABLE_TRANSFORMERS,
        "nlp_models": {
            "sentiment": SENTIMENT_MODEL_ID,
            "qa": QA_MODEL_ID,
            "generate": GEN_MODEL_ID,
        },
    }


@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    return iris_service.predict(
        [req.sepal_length, req.sepal_width, req.petal_length, req.petal_width]
    )


@app.post("/sentiment", response_model=SentimentResponse)
def sentiment(req: SentimentRequest):
    sentiment_pipe = get_sentiment_pipeline()
    if sentiment_pipe is None:
        return heuristic_sentiment(req.text)

    result = sentiment_pipe(req.text, truncation=True)[0]
    label = result["label"]
    if label == "LABEL_1":
        label = "POSITIVE"
    elif label == "LABEL_0":
        label = "NEGATIVE"
    return SentimentResponse(label=label, confidence=float(result["score"]))


@app.post("/qa", response_model=QAResponse)
def qa(req: QARequest):
    qa_pipe = get_qa_pipeline()
    if qa_pipe is None:
        return heuristic_qa(req.context, req.question)

    result = qa_pipe(question=req.question, context=req.context)
    return QAResponse(answer=result.get("answer", ""), confidence=float(result.get("score", 0.0)))


@app.post("/generate", response_model=GenerateResponse)
def generate(req: GenerateRequest):
    generate_pipe = get_generate_pipeline()
    if generate_pipe is None:
        return heuristic_generate(req.prompt, req.max_length)

    outputs = generate_pipe(
        req.prompt,
        max_new_tokens=req.max_length,
        do_sample=True,
        temperature=req.temperature,
        num_return_sequences=1,
        return_full_text=True,
    )
    texts = [out["generated_text"] for out in outputs]
    return GenerateResponse(generated_texts=texts, model_info=GEN_MODEL_ID)


@app.get("/")
def root():
    return {
        "message": "AMALEA demo API running",
        "endpoints": ["/health", "/predict", "/sentiment", "/qa", "/generate"],
        "nlp_mode": nlp_mode(),
        "nlp_models": {
            "sentiment": SENTIMENT_MODEL_ID,
            "qa": QA_MODEL_ID,
            "generate": GEN_MODEL_ID,
        },
    }

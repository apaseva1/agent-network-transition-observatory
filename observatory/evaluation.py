from __future__ import annotations

import math

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import average_precision_score, brier_score_loss, roc_auc_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


FEATURES = [
    "unsafe_fraction",
    "propagation_rate",
    "activity_entropy",
    "avg_clustering",
    "algebraic_connectivity",
    "edge_turnover",
]
BASELINE_FEATURES = ["unsafe_fraction"]


def matrix(rows, features=FEATURES):
    x = np.asarray([[r[f] for f in features] for r in rows], dtype=float)
    y = np.asarray([r["future_cascade"] for r in rows], dtype=int)
    return x, y


def fit_predictor(rows, features=FEATURES):
    x, y = matrix(rows, features)
    if len(np.unique(y)) < 2:
        raise ValueError("training data must contain both cascade classes")
    model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000, random_state=0))
    model.fit(x, y)
    return model


def evaluate(model, rows, features=FEATURES):
    x, y = matrix(rows, features)
    p = model.predict_proba(x)[:, 1]
    if len(np.unique(y)) < 2:
        auroc = float("nan")
    else:
        auroc = float(roc_auc_score(y, p))
    auprc = float(average_precision_score(y, p))
    brier = float(brier_score_loss(y, p))
    return {
        "auroc": auroc,
        "auprc": auprc,
        "brier": brier,
        "prevalence": float(np.mean(y)),
        "n": int(len(y)),
    }


def transfer_retention(
    source_full: float,
    source_baseline: float,
    target_full: float,
    target_baseline: float,
    min_source_uplift: float = 0.01,
) -> float | None:
    denom = source_full - source_baseline
    if not all(math.isfinite(x) for x in [source_full, source_baseline, target_full, target_baseline]):
        return None
    if denom < min_source_uplift:
        return None
    return (target_full - target_baseline) / denom

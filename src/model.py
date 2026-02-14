from sklearn.ensemble import IsolationForest
import pandas as pd


def train_isolation_forest(
    X: pd.DataFrame,
    contamination: float = 0.05,
    random_state: int = 42,
):
    """
    Train Isolation Forest model.
    """
    model = IsolationForest(
        n_estimators=100,
        contamination=contamination,
        random_state=random_state,
    )
    model.fit(X)
    return model


def score_anomalies(model, X: pd.DataFrame) -> pd.DataFrame:
    """
    Add anomaly scores and labels.
    """
    results = X.copy()
    results["anomaly_score"] = model.decision_function(X)
    results["is_anomaly"] = model.predict(X)
    return results

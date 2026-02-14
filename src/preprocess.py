import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    """Load dataset from CSV."""
    return pd.read_csv(path)


def prepare_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Select numeric features for anomaly detection.
    """
    numeric_df = df.select_dtypes(include=["int64", "float64"])
    return numeric_df

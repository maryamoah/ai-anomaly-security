import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def plot_anomaly_distribution(df: pd.DataFrame, output_path: str):
    """
    Plot anomaly score distribution.
    """
    plt.figure(figsize=(6, 4))
    sns.histplot(df["anomaly_score"], bins=30, kde=True)
    plt.title("Anomaly Score Distribution")
    plt.xlabel("Score")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

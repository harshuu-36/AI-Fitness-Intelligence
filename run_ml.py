"""
==============================================================
Run Machine Learning Pipeline
==============================================================
"""

from src.models.train_weight_model import (
    load_dataset,
    train_model
)


def run():

    # Load Feature Engineered Dataset
    dataset = load_dataset(
        "artifacts/processed_data/feature_engineered_data.csv"
    )

    print("\nDataset Loaded Successfully")
    print(dataset.head())

    # Train Model
    train_model(dataset)


if __name__ == "__main__":

    run()
import json
from pathlib import Path


DATASET_PATH = Path(__file__).parent / "golden_dataset.json"


def load_dataset():
    with open(DATASET_PATH, "r", encoding="utf-8") as f:
        return json.load(f)
        
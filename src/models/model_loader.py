
from pathlib import Path
import pickle

BASE_DIR = Path(__file__).resolve().parents[1]

MODEL_PATH = BASE_DIR / "models" / "priority_model.pkl"
SCALER_PATH = BASE_DIR / "models" / "scaler.pkl"

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

with open(SCALER_PATH, "rb") as f:
    scaler = pickle.load(f)







from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# Windows
PYTHON_EXE_FILE = r"C:/Python/envimageclassifier/Scripts/python.exe"  # specify python executable file
HOST = "127.0.0.1"  # localhost
PORT = 8000

# # Linux
# PYTHON_EXE_FILE = "/home/paw/envimageclassifier/bin/python3.10"  # specify python executable file
# HOST = "127.0.0.1"
# PORT = 8000

MODEL_PATH = Path(BASE_DIR, "appmain", "model", "best_model_2.12.0.h5")

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# Windows
PYTHON_EXE_FILE = r"C:/Python/envcic/Scripts/python.exe"  # specify python executable file
HOST = "127.0.0.1"  # localhost
PORT = 8000

# # Linux
# PYTHON_EXE_FILE = "/home/paw/envcic/bin/python3.10"  # specify python executable file
# HOST = "127.0.0.1"
# PORT = 8000

MODEL_PATH = Path(BASE_DIR, "appmain", "model", "best_model_2.14.0.h5")

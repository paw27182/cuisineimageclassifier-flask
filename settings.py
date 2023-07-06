from pathlib import Path

# Windows
PYTHON_EXE_FILE = r"C:/Python/envimageclassifier/Scripts/python.exe"  # specify python executable file
# BASE_DIR = r"C:/temp/cuisineimageclassifier-flask"  # specify base directory

HOST = "127.0.0.1"  # localhost
PORT = 8000

# # Linux
# PYTHON_EXE_FILE = "/home/paw/envimageclassifier/bin/python3.10"  # specify python executable file
# BASE_DIR = "/home/paw/cuisineimageclassifier-flask"  # specify base directory

# HOST = "127.0.0.1"
# PORT = 8000


MODEL_PATH = Path(BASE_DIR, "appmain", "model", "best_model_2.12.0.h5")

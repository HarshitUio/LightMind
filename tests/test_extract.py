from pathlib import Path
from lm.extract import extract

def scan(folder : str):
    fPath = Path(folder).expanduser()
    
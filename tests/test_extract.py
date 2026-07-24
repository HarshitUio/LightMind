from pathlib import Path
from lm.extract import extract

def scan(folder : str):
    fPath = Path(folder).expanduser()
    for filepath in fPath.rglob("*"):
        if filepath.is_file():
            text = extract(filepath)
            if(text):
                print(f"{filepath.name} : {len(text)} characters")
            else:
                print(f"{filepath.name} : Extraction failed / empty")
if __name__ == "__main__":
    scan("C:\\Users\\harsh\\OneDrive\\Desktop\\test")
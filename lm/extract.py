from pathlib import Path
import pdfplumber
from docx import Document
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

plainText = {".md", ".txt", ".py", ".c", '.cpp', '.js', '.h'}

def extractPlain(filepath : Path):
    try:
        return filepath.read_text(encoding = 'utf8')
    except UnicodeDecodeError:
        return filepath.read_text(encoding = 'latin-1', errors = 'ignore')

def extractPdf(filepath : Path):
    text = []
    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            pText = page.extract_text()
            if(pText):
                text.append(pText)
    return "\n".join(text)

def extractDoc(filepath : Path):
    doc = Document(filepath)
    return "\n".join(para.text for para in doc.paragraphs)

def extract(filepath : Path):
    suf = filepath.suffix.lower()

    try:
        if suf in plainText:
            text = extractPlain(filepath)
        
        elif suf == ".pdf":
            text = extractPdf(filepath)
        
        elif suf == ".docx" or suf == ".doc":
            text = extractDoc(filepath)

        else:
            logger.info(f"Skipping unsupported file : {filepath}")
            return None
        
        if not text or not text.strip():
            logger.warning(f"No Extractable Text : {filepath}")
            return None
        return text
    except Exception as e:
        logger.error(f"Failed to extract text : {filepath.name} : {e}")
        return None
    

          





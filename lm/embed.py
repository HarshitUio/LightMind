from dotenv import load_dotenv
load_dotenv()

from sentence_transformers import SentenceTransformer

_model = None

def getModel():
    global _model
    if _model is None:
        _model = SentenceTransformer("all-MiniLM-L6-v2")  
    return _model

def embed(text):
    return getModel().encode(text)

def embedBatch(texts):
    return getModel().encode(texts, size=32, show_progress_bar = True)





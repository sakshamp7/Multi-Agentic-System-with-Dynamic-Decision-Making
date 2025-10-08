from sentence_transformers import SentenceTransformer
import os

_model = None

def get_model(model_name=None):
    global _model
    if _model is None:
        name = model_name or os.environ.get('EMBED_MODEL','all-MiniLM-L6-v2')
        _model = SentenceTransformer(name)
    return _model

def embed_texts(texts, model_name=None):
    model = get_model(model_name)
    return model.encode(texts, show_progress_bar=False)

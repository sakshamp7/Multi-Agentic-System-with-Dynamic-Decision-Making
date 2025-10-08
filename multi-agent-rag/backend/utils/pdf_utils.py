import fitz
import re

def extract_pages_text(path):
    doc = fitz.open(path)
    pages = []
    for p in doc:
        pages.append(p.get_text())
    return pages

def clean_text(s):
    # remove long sequences of whitespace and control chars
    s = re.sub(r'\s+', ' ', s).strip()
    return s

def chunk_text_by_chars(text, chunk_size=1200, overlap=200):
    chunks = []
    start = 0
    L = len(text)
    while start < L:
        end = min(start + chunk_size, L)
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

import os, uuid
from .utils.pdf_utils import extract_pages_text, clean_text, chunk_text_by_chars
from .utils.embeddings import embed_texts
from .faiss import FaissStore  # ← fixed relative import

INDEX_DIR = os.environ.get('FAISS_INDEX_DIR','./faiss_index')
store = FaissStore(index_dir=INDEX_DIR, dim=384)

def ingest_pdf(path, source_name=None):
    pages = extract_pages_text(path)
    all_chunks = []
    metadatas = []
    for p_idx, page in enumerate(pages, start=1):
        text = clean_text(page)
        chunks = chunk_text_by_chars(text)
        for c_idx, chunk in enumerate(chunks, start=1):
            uid = str(uuid.uuid4())
            meta = {'id': uid, 'source': source_name or os.path.basename(path), 'page': p_idx, 'chunk': c_idx, 'text': chunk}
            all_chunks.append(chunk)
            metadatas.append(meta)
    if not all_chunks:
        return []
    vectors = embed_texts(all_chunks)
    store.add(vectors, metadatas)
    return metadatas

def retrieve(file_id_or_query, query_text=None, top_k=5):
    q = query_text or file_id_or_query
    if not q:
        return []
    q_vec = embed_texts([q])[0]
    return store.search(q_vec, top_k=top_k)

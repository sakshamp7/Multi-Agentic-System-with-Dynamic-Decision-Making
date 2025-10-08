import os, faiss, numpy as np, json
from pathlib import Path

class FaissStore:
    def __init__(self, index_dir=None, dim=384):
        self.index_dir = Path(index_dir or os.environ.get('FAISS_INDEX_DIR','./faiss_index'))
        self.index_dir.mkdir(parents=True, exist_ok=True)
        self.index_file = self.index_dir / 'index.faiss'
        self.meta_file = self.index_dir / 'metadata.jsonl'
        self.dim = dim
        self._load()

    def _load(self):
        if self.index_file.exists():
            self.index = faiss.read_index(str(self.index_file))
        else:
            self.index = faiss.IndexFlatL2(self.dim)
        self.metadata = []
        if self.meta_file.exists():
            with open(self.meta_file,'r',encoding='utf-8') as f:
                for line in f:
                    self.metadata.append(json.loads(line))

    def add(self, vectors, metadatas):
        vecs = np.array(vectors).astype('float32')
        if vecs.ndim == 1:
            vecs = vecs.reshape(1, -1)
        self.index.add(vecs)
        with open(self.meta_file,'a',encoding='utf-8') as f:
            for m in metadatas:
                f.write(json.dumps(m, ensure_ascii=False) + '\n')
        self._save_index()

    def _save_index(self):
        faiss.write_index(self.index, str(self.index_file))

    def search(self, query_vec, top_k=5):
        q = np.array(query_vec).astype('float32').reshape(1,-1)
        D, I = self.index.search(q, top_k)
        results = []
        for dist, idx in zip(D[0], I[0]):
            if idx < len(self.metadata):
                m = self.metadata[idx].copy()
                m['score'] = float(dist)
                results.append(m)
        return results

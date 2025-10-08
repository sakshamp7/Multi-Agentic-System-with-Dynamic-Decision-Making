from backend.agents.faiss_store import FaissStore
import numpy as np

def test_add_and_search():
    s = FaissStore(index_dir='./faiss_test', dim=8)
    vecs = np.random.rand(2,8).astype('float32')
    metas = [{'id':'a'},{'id':'b'}]
    s.add(vecs, metas)
    q = vecs[0].tolist()
    res = s.search(q, top_k=2)
    assert len(res) >= 1

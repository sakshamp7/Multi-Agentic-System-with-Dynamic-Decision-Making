def search(q):
    q = q or ''
    return [{'id':f'web_{i}','title':f'Result {i} for {q}','url':'https://example.com','snippet':'Sample snippet'} for i in range(1,6)]

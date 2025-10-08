import arxiv

def search(q, max_results=5):
    if not q:
        return []
    search_obj = arxiv.Search(query=q, max_results=max_results, sort_by=arxiv.SortCriterion.SubmittedDate)
    results = []
    for r in search_obj.results():
        results.append({
            'id': r.entry_id,
            'title': r.title,
            'authors':[a.name for a in r.authors],
            'summary': r.summary
        })
    return results

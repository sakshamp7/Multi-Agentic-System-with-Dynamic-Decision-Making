import time
from ..agents import pdf_rag, web_search, arxiv_agent, synthesize
from ..db.models import save_trace

def init_controllers(app=None):
    pass

def route_request(req):
    text = (req.get('text') or '').lower()
    trace = {'input': req, 'timestamp': time.time(), 'decision': None, 'agents_called': [], 'docs': []}

    if req.get('file_id') and 'summarize' in text:
        trace['decision'] = 'pdf_rag'
        trace['agents_called'].append('pdf_rag')
        docs = pdf_rag.retrieve(req['file_id'], req.get('text'))
    elif 'arxiv' in text or 'recent papers' in text:
        trace['decision'] = 'arxiv'
        trace['agents_called'].append('arxiv')
        docs = arxiv_agent.search(req.get('text') or '')
    elif 'latest' in text or 'recent' in text:
        trace['decision'] = 'web_search'
        trace['agents_called'].append('web_search')
        docs = web_search.search(req.get('text') or '')
    else:
        if req.get('file_id'):
            trace['decision'] = 'pdf_rag + synthesize'
            trace['agents_called'] += ['pdf_rag','synthesize']
            docs = pdf_rag.retrieve(req['file_id'], req.get('text'))
        else:
            trace['decision'] = 'web_search + synthesize'
            trace['agents_called'] += ['web_search','synthesize']
            docs = web_search.search(req.get('text') or '')[:5]

    trace['docs'] = [{'id': d.get('id','unknown'), 'title': d.get('title', d.get('filename', ''))} for d in docs]
    answer = synthesize.compose_answer(req.get('text') or '', docs)
    trace['answer'] = answer[:2000]
    save_trace(trace)
    return {'answer': answer, 'trace': trace}

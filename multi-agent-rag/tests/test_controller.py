import json
from backend.controllers.controller import route_request

def test_route_web_search_default():
    req = {'text':'What are the latest developments in AI?'}
    res = route_request(req)
    assert 'answer' in res
    assert 'web_search' in res['trace']['agents_called'][0]

def test_route_pdf_summarize():
    req = {'text':'Please summarize this document','file_id':'nebula_dialog_1.pdf'}
    res = route_request(req)
    assert 'pdf_rag' in res['trace']['decision'] or 'pdf_rag' in str(res['trace']['agents_called'])

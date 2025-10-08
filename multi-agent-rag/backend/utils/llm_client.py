import os, time, requests

def call_groq(prompt, max_tokens=512):
    key = os.environ.get('GROQ_API_KEY')
    if not key:
        raise RuntimeError('GROQ_API_KEY not set')
    url = 'https://api.groq.ai/v1'  # placeholder
    headers = {'Authorization': f'Bearer {key}', 'Content-Type':'application/json'}
    payload = {'prompt': prompt, 'max_tokens': max_tokens}
    for attempt in range(3):
        r = requests.post(url, headers=headers, json=payload, timeout=20)
        if r.status_code == 200:
            return r.json()
        time.sleep(2 ** attempt)
    raise RuntimeError('LLM call failed: ' + r.text)

def call_gemini(prompt, max_tokens=512):
    key = os.environ.get('GEMINI_API_KEY')
    if not key:
        raise RuntimeError('GEMINI_API_KEY not set')
    url = 'https://gemini.api.google/v1'  # placeholder
    headers = {'Authorization': f'Bearer {key}', 'Content-Type':'application/json'}
    payload = {'prompt': prompt, 'maxTokens': max_tokens}
    for attempt in range(3):
        r = requests.post(url, headers=headers, json=payload, timeout=20)
        if r.status_code == 200:
            return r.json()
        time.sleep(2 ** attempt)
    raise RuntimeError('Gemini call failed: ' + r.text)

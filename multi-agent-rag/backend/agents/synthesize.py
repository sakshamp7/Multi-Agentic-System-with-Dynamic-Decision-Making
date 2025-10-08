from backend.utils.llm_client import call_groq, call_gemini

def compose_answer(query, docs):
    # Build a short context from docs
    ctx = '\n'.join([f"Source: {d.get('source', d.get('filename',''))} - {d.get('id')}\n{d.get('text','(no text)')[:800]}" for d in docs[:6]])
    prompt = f"You are an assistant. Use only the sources below to answer the question. Sources:\n{ctx}\nQuestion: {query}\nProvide a concise answer and a list of sources."

    # Try Groq then Gemini as fallback
    try:
        res = call_groq(prompt)
        return res.get('text') or str(res)
    except Exception:
        try:
            res = call_gemini(prompt)
            return res.get('text') or str(res)
        except Exception:
            # fallback: simple composition
            lines = [f"(fallback) Answer based on {len(docs)} sources for query: {query}"]
            for d in docs[:5]:
                lines.append(f"- {d.get('source', d.get('filename','unknown'))} (id:{d.get('id')})")
            return '\n'.join(lines)

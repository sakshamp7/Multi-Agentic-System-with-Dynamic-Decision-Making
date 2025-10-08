from .init_db import SessionLocal, Trace
import json, time

def save_trace(trace):
    session = SessionLocal()
    t = Trace(timestamp=str(time.time()), data=json.dumps(trace))
    session.add(t)
    session.commit()
    session.close()

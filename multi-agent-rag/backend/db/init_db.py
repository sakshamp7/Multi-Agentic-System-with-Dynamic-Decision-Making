import os
from sqlalchemy import create_engine, Column, Integer, Text, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

BASE = declarative_base()
DB_PATH = os.environ.get('DEV_DB','./backend_logs.db')
engine = create_engine(f'sqlite:///{DB_PATH}', connect_args={'check_same_thread':False})
SessionLocal = sessionmaker(bind=engine)

class Trace(BASE):
    __tablename__ = 'traces'
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(String)
    data = Column(Text)

def init_db(app=None):
    BASE.metadata.create_all(bind=engine)

def get_recent_traces(limit=20):
    session = SessionLocal()
    rows = session.query(Trace).order_by(Trace.id.desc()).limit(limit).all()
    return [{'id':r.id, 'timestamp':r.timestamp, 'data': r.data[:1000]} for r in rows]

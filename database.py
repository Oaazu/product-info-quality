from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import DBModelBase
import os

# This makes it work both locally and on Streamlit Cloud
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, 'test.db')}"

engine = create_engine(DATABASE_URL)
DBModelBase.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)
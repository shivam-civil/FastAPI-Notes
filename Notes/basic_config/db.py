
# THIS IS DATABASE CONFIGURATION INSIDE SRC/UTILS/DB.PY OF TASK MANAGEMENT APP LEARNING FROM TECHSIMPLUS LEARNING
from sqlalchemy import create_engine 
from sqlalchemy.orm import declarative_base, sessionmaker 
from src.utils.settings import settings 

Base = declarative_base()
engine = create_engine(url=settings.DB_CONNECTION)
LocalSession = sessionmaker(bind=engine)

def get_db():
    session = LocalSession()
    try :
        yield session 
    finally : 
        session.close()
 
        
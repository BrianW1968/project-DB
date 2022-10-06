from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
import config


SQLALCHEMY_DATABASE_URL = f'postgresql://{config.settings.database_username}:{config.settings.database_password}@{config.settings.database_hostname}:{config.settings.database_port}/{config.settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


#while True:
#  try:
#      conn = psycopg2.connect(host='localhost',database= 'fastapi', user='postgres', password= '7501Fitness!', cursor_factory=RealDictCursor)
#      cursor = conn.cursor()
#     print ("Database connection was successfull!")
#      break
#  except Exception as error:
#      print("Connection to database failed")
#      print("Error: ", error)
#      time.sleep(2)
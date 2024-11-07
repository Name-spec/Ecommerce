import pymysql
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
engine = create_engine('mysql+pymysql://root:Throttle_12q@localhost:3306/store_db')
Session = sessionmaker(bind=engine)
Base = declarative_base()
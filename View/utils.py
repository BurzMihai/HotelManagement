from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine('mysql+pymysql://root:@127.0.0.1:3305/hotel', echo=False)
Session = sessionmaker(bind=engine)
my_session = Session()

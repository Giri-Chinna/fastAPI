from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .secret import DB_PWD

SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:{DB_PWD}@localhost/TodoApplicationDatabase"
#mysql+pymysql://username:password@host:port/database

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
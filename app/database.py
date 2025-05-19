from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base

engine = create_engine("mysql+pymysql://root:password@localhost:3306/testdb", echo=True, pool_pre_ping=True)

with engine.connect() as conn:
    conn.execute(text("CREATE DATABASE IF NOT EXISTS testdb"))

Base = declarative_base()

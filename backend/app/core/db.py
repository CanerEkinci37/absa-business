import os
from dotenv import dotenv_values
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


config = dotenv_values(".env")
# Postgres
engine = create_engine(config["SQLALCHEMY_DATABASE_URL"])
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

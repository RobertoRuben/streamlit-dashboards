import os
from sqlalchemy import create_engine, Engine
from dotenv import load_dotenv

load_dotenv()

RAW_DB_URL = os.getenv("RAW_DB_URL")

engine: Engine = create_engine(RAW_DB_URL)
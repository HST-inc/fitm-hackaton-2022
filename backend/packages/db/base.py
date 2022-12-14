from databases import Database
from sqlalchemy import create_engine, MetaData
from packages.core.config import DB_URL

database = Database(DB_URL)
metadata = MetaData()
engine = create_engine(DB_URL)

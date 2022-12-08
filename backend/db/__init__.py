from .base import metadata, engine
from .users import users_table

metadata.create_all(bind=engine)

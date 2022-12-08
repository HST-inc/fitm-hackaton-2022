import sqlalchemy
from .base import metadata
import datetime

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer,
                      autoincrement=True, unique=True, primary_key=True),
    sqlalchemy.Column("first_name", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("second_name", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("age", sqlalchemy.Integer),
    sqlalchemy.Column("created_time", sqlalchemy.DateTime,
                      default=datetime.datetime.utcnow),
    sqlalchemy.Column("hashed_password", sqlalchemy.String,
                      unique=True, primary_key=True),
)

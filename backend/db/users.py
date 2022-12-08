import sqlalchemy
from .base import metadata
import datetime

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer,
                      autoincrement=True, unique=True, primary_key=True),
    sqlalchemy.Column("first_name", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("patronymic_name", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("birth_date", sqlalchemy.DateTime, ptimary_key=True),
    sqlalchemy.Column("last_name", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("created_time", sqlalchemy.DateTime,
                      default=datetime.datetime.utcnow),
    sqlalchemy.Column("hashed_password", sqlalchemy.String,
                      unique=True, primary_key=True),
    sqlalchemy.Column("sex", sqlalchemy.String, deault="male"),
    sqlalchemy.Column("phone_number", sqlalchemy.String),
    sqlalchemy.Column("snus", sqlalchemy.String),
    sqlalchemy.Column("passport_series", sqlalchemy.String),
    sqlalchemy.Column("passport_number", sqlalchemy.String)
)

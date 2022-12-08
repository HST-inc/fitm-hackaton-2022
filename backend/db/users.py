import sqlalchemy
from .base import metadata
import datetime

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer,
                      autoincrement=True, unique=True, primary_key=True),
    sqlalchemy.Column("firstName", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("patronymicName", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("birthDate", sqlalchemy.DateTime, ptimary_key=True),
    sqlalchemy.Column("lastName", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("createdTime", sqlalchemy.DateTime,
                      default=datetime.datetime.utcnow),
    sqlalchemy.Column("hashedPassword", sqlalchemy.String,
                      unique=True, primary_key=True),
    sqlalchemy.Column("sex", sqlalchemy.String, deault="male"),
    sqlalchemy.Column("phoneNumber", sqlalchemy.String),
    sqlalchemy.Column("snus", sqlalchemy.String),
    sqlalchemy.Column("passportSeries", sqlalchemy.String),
    sqlalchemy.Column("passportNumber", sqlalchemy.String)
)

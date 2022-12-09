import os

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")

DB_URL = "postgresql://{}:{}@db/{}".format(POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB)

ROUTES_DEFAULT_PATH = "/api/v1" #переиспользовать #delete

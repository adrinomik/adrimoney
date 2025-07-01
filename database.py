from databases import Database
from sqlalchemy import MetaData

DATABASE_URL = "postgresql+asyncpg://postgres:4874980@localhost:5432/adrimoney"

database = Database(DATABASE_URL)
metadata = MetaData()
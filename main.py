from fastapi import FastAPI, Request # импортируем FastAPI из fastapi
from database import database, DATABASE_URL, metadata # импортируем database из database.py
from sqlalchemy import Table, Column, Integer, String, MetaData, Boolean, DateTime # импортируем Table, Column, Integer, String, MetaData из sqlalchemy
from sqlalchemy.sql import func # импортируем func из sqlalchemy
from datetime import datetime # импортируем datetime из datetime
from pydantic import BaseModel # импортируем BaseModel из pydantic

class Transaction(BaseModel):
    type: str
    amount: int
    description: str

class User(BaseModel):
    name: str
    password: str
    email: str
    status: bool

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.on_event("startup")
async def startup():
    await database.connect()
    print("Database connected")
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
    print("Database disconnected")

transactions = Table( # создаем таблицу transactions
    "transactions",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("type", String),
    Column("amount", Integer),
    Column("description", String),
)


users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, unique=True),
    Column("password", String),
    Column("email", String, unique=True),
    Column("status", Boolean),
    Column("created_at", DateTime, server_default=func.now()),
)


from sqlalchemy import create_engine # импортируем create_engine из sqlalchemy для создания соединения с базой данных

sync_database_url = DATABASE_URL.replace("+asyncpg", "")
engine = create_engine(sync_database_url) # соединение с базой данных
metadata.create_all(engine) # создание таблиц


# Создадим функцию которая будет добавлять новую транзакцию в базу данных


@app.post("/add-transaction")

async def add_transaction(transaction: Transaction):
    query = transactions.insert().values(
        type=transaction.type,
        amount=transaction.amount,
        description=transaction.description,
    )
    last_record_id = await database.execute(query)
    return {"message": "Transaction added successfully", "id": last_record_id}


@app.post("/add-user")

async def add_user(user: User):
    query = users.insert().values(
        name=user.name,
        password=user.password,
        email=user.email,
        status=user.status,
    )
    last_record_id = await database.execute(query)
    return {"message": "User added successfully", "id": last_record_id}

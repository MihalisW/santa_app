from peewee import *
import os  

db = PostgresqlDatabase(os.getenv("DATABASE_NAME"), 
                        user=os.getenv("DATABASE_USER"),
                        password=os.getenv("DATABASE_PASSWORD"), 
                        host=os.getenv("DATABASE_HOST"),
                        port=os.getenv("DATABASE_PORT"))

class BaseModel(Model):
    class Meta:
        database = db

class Present(BaseModel):
    name = CharField()
    sku = CharField()
    site = CharField()

class User(BaseModel):
    username = CharField(unique=True)
    email = CharField(unique=True) 

class Behaviour(BaseModel):
    id = UUIDField(unique=True)
    user = ForeignKeyField(User, backref='id')
    year = IntegerField()
    is_good = BooleanField()
    observed_at = TimestampField()

class PresentRequest(BaseModel):
    id = UUIDField(unique=True)
    user = ForeignKeyField(User, backref='id')
    present = ForeignKeyField(Present, backref='id')
    request_timestamp = TimestampField()

    class Meta:
        db_table = 'present_request'

def open_close_connection(func):
    def wrapper(*args, **kwargs):
        db.connect()
        func(*args, **kwargs)
        db.close()
    return wrapper

@open_close_connection
def create_all_tables() -> None:
    db.create_tables([Present, User, Behaviour, PresentRequest])

from peewee import *
import os  

db = PostgresqlDatabase(user=os.getenv("DATABASE_NAME"), 
user=os.getenv("DATABASE_USER")
password=os.getenv("DATABASE_PASSWORD"), 
host=os.getenv("DATABASE_HOST"))

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

class PresentRequests(BaseModel):
    id = UUIDField(unique=True)
    user = ForeignKeyField(User, backref='id')
    present = ForeignKeyField(Present, backref='id')
    request_timestamp = TimestampField()
    
db.connect()

db.create_tables([Present, User, PresentRequests])
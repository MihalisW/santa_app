from peewee import *
import os  

db = PostgresqlDatabase(user=os.getenv("DATABASE_NAME"), 
user=os.getenv("DATABASE_USER")
password=os.getenv("DATABASE_PASSWORD"), 
host=os.getenv("DATABASE_HOST"))


class Presents(Model):
    name = CharField()
    sku = CharField()
    site = CharField()


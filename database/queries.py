from database.model import *

def open_close_connection(func):
    def wrapper(*args, **kwargs):
        db.connect()
        func(*args, **kwargs)
        db.close()
    return wrapper

@open_close_connection
def create_all_tables() -> None: 
    db.create_tables([Present, User, PresentRequest])

class Queries(object):
    def __init__(self) -> None:
        pass



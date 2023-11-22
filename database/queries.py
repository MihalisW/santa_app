from database.model import *

class Queries(object):
    def __init__(self) -> None:
        pass
    
    def check_health(self) -> bool: 
        cursor = db.execute_sql("SELECT TRUE AS \"value\"").fetchone()[0]
        return cursor
from database.model import *
from typing import List

class Queries(object):
    def __init__(self) -> None:
        pass
    
    def check_health(self) -> bool: 
        cursor = db.execute_sql("SELECT TRUE AS \"value\"").fetchone()[0]
        return cursor
    
    def insert_presents(self, 
                        present_data: List[dict | tuple]
                        ) -> tuple:
        cursor = Present.insert_many(present_data)
        return cursor

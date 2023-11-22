from database.queries import *

class ElfService(object):
    def __init__(self, name: str | None = None) -> any:
        self.name = name
        self.queries = Queries() 
    
    def check_health(self) -> bool:
        return self.queries.check_health()
    
    def find_present(self) -> any:
        self.name 
        #TODO do something with name
    
    def ask_for_present() -> None:
        #TODO log present in database
        pass 
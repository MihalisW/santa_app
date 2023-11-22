from pydantic import (BaseModel, 
                      HttpUrl, 
                      EmailStr, 
                      UUID1, 
                      PastDatetime)

class Present(BaseModel):
    name: str
    sku: str
    site: HttpUrl

class User(BaseModel):
    username: str
    email: EmailStr 

class Behaviour(BaseModel):
    id: UUID1
    user: UUID1
    year: int
    is_good: bool
    observed_at: PastDatetime

class PresentRequest(BaseModel):
    id: UUID1
    user: UUID1
    present: UUID1
    request_timestamp: PastDatetime

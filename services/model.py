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
    user: type[User.email]
    year: int
    is_good: bool
    observed_at: PastDatetime

class PresentRequest(BaseModel):
    id: UUID1
    user: User.email
    present: type[Present]
    request_timestamp: PastDatetime

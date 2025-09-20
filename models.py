from pydantic import BaseModel

class User(BaseModel):
    id : int
    name : str
    phone: int

class AdminLogin(BaseModel):
    username: str
    password: str



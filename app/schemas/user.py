from pydantic import BaseModel


class AddUser(BaseModel):
    name: str
    username: str
    password: str
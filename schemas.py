from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional


class UserCreateSchemas(BaseModel):
    username: str = Field(min_length=3, max_length=20, example="johndoe")
    email: EmailStr = Field(example="john@example.com")
    password: str = Field(min_length=6, example="strongpassword123")


class UserSchemas(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: str

    model_config = {
        "from_attributes": True
    }


class TokenSchemas(BaseModel):
    access_token: str
    token_type: str = "Bearer"



class AuthorCreateSchemas(BaseModel):
    name: str = Field( example="Jane Doe")
    bio: Optional[str] = Field(None, example="Writes hystorical books")

class AuthorSchemas(AuthorCreateSchemas):
    id: int

    class Config:
        from_attributes = True


class BookCreateSchemas(BaseModel):
    title: str = Field(example="The Great Gatsby")
    year: int = Field(example=1925)
    available: bool = Field(default=True)
    author_id: int = Field(example=1)

class BookSchemas(BookCreateSchemas):
    id: int

    class Config:
        from_attributes = True



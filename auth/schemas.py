import re
from typing import Optional

from pydantic import BaseModel, EmailStr, UUID4, validator, Field


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str = Field(None, min_length=8, max_length=20)
    confirm_password: str = Field(None, min_length=8, max_length=20)

    @validator("password")
    def is_password_valid(cls, v):
        if not re.search("(?=.*[a-z])(?=.*[A-Z])", v):
            raise ValueError(
                "password should contain at least one lowercase and uppercase letter"
            )
        elif not re.search("\d", v):
            raise ValueError("password should contain at least one digit")
        elif not re.search("[@$!%*#?&]", v):
            raise ValueError(
                "password should contain at least one special symbol ($!%*#?&)"
            )
        return v

    @validator("confirm_password")
    def password_match(cls, v, values):
        if v != values.get("password"):
            raise ValueError("passwords do not match")
        return v


class User(UserBase):
    id: UUID4
    is_active: bool

    class Config:
        orm_mode = True


class UserInDB(User):
    hashed_password: str

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None

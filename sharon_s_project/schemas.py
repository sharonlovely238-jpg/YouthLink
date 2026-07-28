from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserCreate(BaseModel):
    username: str = Field(min_length=2, max_length=50)
    email: EmailStr
    password: str = Field(min_length=6, max_length=128)
    student_id: str | None = Field(default=None, max_length=50)


class UserLogin(BaseModel):
    username: str
    password: str


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    email: EmailStr
    student_id: str | None
    created_at: datetime


class PetitionCreate(BaseModel):
    username: str = Field(min_length=1, max_length=50)
    title: str = Field(min_length=1, max_length=200)
    text: str = Field(min_length=1)


class PetitionUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=200)
    text: str | None = Field(default=None, min_length=1)


class PetitionResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    title: str
    text: str
    created_at: datetime


class CommentCreate(BaseModel):
    username: str = Field(min_length=1, max_length=50)
    comment: str = Field(min_length=1)


class CommentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    comment: str
    created_at: datetime


class PetitionVoteCreate(BaseModel):
    username: str = Field(min_length=1, max_length=50)
    value: int = Field(ge=-1, le=1)


class PetitionSignatureCreate(BaseModel):
    username: str = Field(min_length=1, max_length=50)


class PetitionStatusResponse(BaseModel):
    petition_id: int
    thumbs_up: int
    thumbs_down: int
    signature_count: int
    user_vote: int | None = None
    user_signed: bool = False


class ThreadCreate(BaseModel):
    username: str = Field(min_length=1, max_length=50)
    title: str = Field(min_length=1, max_length=150)
    text: str = Field(min_length=1)


class ThreadUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=150)
    text: str | None = Field(default=None, min_length=1)


class ThreadResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    title: str
    text: str
    created_at: datetime

class OpportunityCreate(BaseModel):
    username: str = Field(min_length=1, max_length=50)
    title: str = Field(min_length=1, max_length=200)
    organization: str = Field(min_length=1, max_length=150)
    deadline: str | None = Field(default=None, max_length=50)
    link: str | None = Field(default=None, max_length=500)
    text: str = Field(min_length=1)


class OpportunityUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=200)
    organization: str | None = Field(default=None, min_length=1, max_length=150)
    deadline: str | None = Field(default=None, max_length=50)
    link: str | None = Field(default=None, max_length=500)
    text: str | None = Field(default=None, min_length=1)


class OpportunityResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    title: str
    organization: str
    deadline: str | None
    link: str | None
    text: str
    created_at: datetime
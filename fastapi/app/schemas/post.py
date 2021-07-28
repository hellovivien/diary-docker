from typing import Optional

from pydantic import BaseModel


# Shared properties
class PostBase(BaseModel):
    content: Optional[str] = None
    


# Properties to receive on Post creation
class PostCreate(PostBase):
    content: str


# Properties to receive on Post update
class PostUpdate(PostBase):
    pass


# Properties shared by models stored in DB
class PostInDBBase(PostBase):
    id: int
    content: str
    author_id: int
    emotion: str
    love: float
    caring: float
    admiration: float
    approval: float
    gratitude: float        
    realization: float
    pride: float
    desire: float
    joy: float
    optimism: float
    relief: float
    excitement: float
    neutral: float
    surprise: float
    curiosity: float
    remorse: float
    amusement: float
    grief: float
    nervousness: float
    confusion: float
    sadness: float
    fear: float
    embarrassment: float
    disapproval: float
    annoyance: float
    anger: float
    disgust: float
    disappointment: float    

    class Config:
        orm_mode = True


# Properties to return to client
class Post(PostInDBBase):
    pass


# Properties properties stored in DB
class PostInDB(PostInDBBase):
    pass

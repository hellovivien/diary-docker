from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User

class Post(Base):
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
    content = Column(String)
    emotion = Column(String)
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="posts")
    love = Column(Float)
    caring = Column(Float)
    admiration = Column(Float)
    approval = Column(Float)
    gratitude = Column(Float)
    realization = Column(Float)
    pride = Column(Float)
    desire = Column(Float)
    joy = Column(Float)
    optimism = Column(Float)
    relief = Column(Float)
    excitement = Column(Float)
    neutral = Column(Float)
    surprise = Column(Float)
    curiosity = Column(Float)
    remorse = Column(Float)
    amusement = Column(Float)
    grief = Column(Float)
    nervousness = Column(Float)
    confusion = Column(Float)
    sadness = Column(Float)
    fear = Column(Float)
    embarrassment = Column(Float)
    disapproval = Column(Float)
    annoyance = Column(Float)
    anger = Column(Float)
    disgust = Column(Float)
    disappointment = Column(Float)
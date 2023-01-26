from sqlalchemy import Column, Integer, String
from db.database import Base


class Movies(Base):
    __tablename__ = "Movies"

    id: int = Column(Integer, primary_key=True, index=True)
    title: str = Column(String(100), nullable=False)
    director: str = Column(String(255), nullable=False)
    duration_in_minutes: int = Column(Integer, nullable=False)
    rating: int = Column(Integer, nullable=False)

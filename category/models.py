from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app import Base
from user.models import User


class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship(User)

    @property
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "user_id": self.user_id
        }

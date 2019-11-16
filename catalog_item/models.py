from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app import Base
from user.models import User
from category.models import Category


class CatalogItem(Base):
    __tablename__ = "catalog_item"
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    description = Column(String(500))
    user_id = Column(Integer, ForeignKey("user.id"))
    category_id = Column(Integer, ForeignKey("category.id"))
    user = relationship(User)
    category = relationship(Category)

    @property
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "user_id": self.user_id,
            "category_id": self.category_id
        }

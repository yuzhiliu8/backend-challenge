
from globals import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String
from models.relationship_tables import club_to_tag_table

class Tag(db.Model):
    __tablename__ = "tags"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)

class Club(db.Model):
    __tablename__ = "clubs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    code: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    description: Mapped[str] = mapped_column(String)
    fav_count: Mapped[int] = mapped_column(Integer, server_default="0")

    tags: Mapped[list[Tag]] = relationship(secondary=club_to_tag_table)

    def dto_dict(self):
        return {
            "id": self.id,
            "code": self.code,
            "name": self.name,
            "description": self.description,
            "fav_count": self.fav_count
        }

    def __str__(self):
        return f'{self.dto_dict()}'
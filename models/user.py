from globals import db
from globals import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String
from models.club import Club
from models.relationship_tables import club_to_user_table


class User(db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    phone: Mapped[str] = mapped_column(String)
    major: Mapped[str] = mapped_column(String)
    year: Mapped[int] = mapped_column(Integer)
    fav_club_name: Mapped[str] = mapped_column(String, server_default="")

    clubs: Mapped[list[Club]] = relationship(secondary=club_to_user_table)

    def dto_dict(self):       # Data transfer object
        return {
            "id": self.id,
            "name": self.name,
            "username": self.username,
            "email": self.email,
            "phone": self.phone,
            "major": self.major,
            "year": self.year,
            "fav_club_name": self.fav_club_name
        }
    
    def __str__(self):
        return f'{self.dto_dict()}'


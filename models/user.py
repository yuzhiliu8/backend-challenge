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

    clubs: Mapped[list[Club]] = relationship(secondary=club_to_user_table)

    def dto_dict(self):       # Data transfer object
        return {
            "name": self.name,
            "username": self.username,
            "email": self.email,
            "phone": self.phone,
            "major": self.major,
            "year": self.year
        }


from models.club import Club
from globals import db

class ClubService:

    def __init__(self, db):
        self.db = db
    
    def get_all_clubs(self):
        stmt = self.db.select(Club)
        clubs = self.db.session.execute(stmt).scalars().all()
        return clubs

    def search_clubs(self, search_string):
        stmt = self.db.select(Club).where(Club.name.like(f'%{search_string}%'))
        clubs = self.db.session.execute(stmt).scalars().all()
        return clubs

#singleton object, to be imported
club_service = ClubService(db)
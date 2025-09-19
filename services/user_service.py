from models.user import User
from globals import db


class UserService:

    def __init__(self, club_service=None):
        self.club_service = club_service

    def get_user_by_id(self, id):
        stmt = db.select(User).where(User.id == id)
        row = db.session.execute(stmt)
        print(row)
    
    def get_user_by_username(self, username):
        stmt = db.select(User).where(User.username == username)
        user = db.session.execute(stmt).scalar()
        return user
    
    def update_favorite_club(self, username, club_name):
        user = self.get_user_by_username(username)
        if user is None:
            raise ValueError(f"{username} doesn't exist!")
        
        previous_fav = user.fav_club_name
        user.fav_club_name = club_name
        db.session.commit()
        self.club_service.update_club_fav_count(club_name) #update newly favorited club

        if previous_fav != "":
            self.club_service.update_club_fav_count(previous_fav) #update previous favorite to get rid of a favorite
        return user
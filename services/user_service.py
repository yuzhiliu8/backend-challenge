from models.user import User
from globals import db


class UserService:

    def __init__(self, db):
        self.db = db

    def get_user_by_id(self, id):
        stmt = self.db.select(User).where(User.id == id)
        row = self.db.session.execute(stmt)
        print(row)
    
    def get_user_by_username(self, username):
        stmt = self.db.select(User).where(User.username == username)
        user = self.db.session.execute(stmt).scalar()
        return user

#singleton object, to be imported
user_service = UserService(db)
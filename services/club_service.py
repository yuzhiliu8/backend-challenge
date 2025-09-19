from models.club import Club, Tag
from models.user import User
from globals import db
from sqlalchemy.exc import IntegrityError

class ClubService:

    def __init__(self, user_service=None, club_to_tag_table=None):
        self.user_service = user_service
        self.club_to_tag_table = club_to_tag_table
    
    def get_club_by_name(self, name):
        stmt = db.select(Club).where(Club.name == name)
        club = db.session.execute(stmt).scalar()
        return club
    
    def get_all_clubs(self):
        stmt = db.select(Club)
        clubs = db.session.execute(stmt).scalars().all()
        return clubs

    def search_clubs(self, search_string):
        stmt = db.select(Club).where(Club.name.like(f'%{search_string}%'))
        clubs = db.session.execute(stmt).scalars().all()
        return clubs
    
    def create_new_club(self, club_data: dict):
        club_tag_names = club_data['tags']

        #get existing tags that the new club has
        tag_map = {}
        stmt = db.select(Tag).where(Tag.name.in_(club_tag_names))
        existing_tags = db.session.execute(stmt).scalars().all()
        for tag in existing_tags:
            tag_map[tag.name] = tag
        
        tag_list = []
        for tag_name in club_tag_names: #if this club has tags that don't exist yet, create them
            if tag_name not in tag_map:
                tag_map[tag_name] = Tag(name=tag_name)
            tag_list.append(tag_map[tag_name])
        new_club = Club(
            code = club_data.get('code'),
            name = club_data.get('name'),
            description = club_data.get('description'),
            tags = tag_list
        )
        db.session.add(new_club)
        try:
            db.session.commit()
            return new_club
        except IntegrityError as e:
            db.session.rollback()
            raise
    
    def update_club_fav_count(self, club_name):
        club = self.get_club_by_name(club_name)
        stmt = db.select(User).where(User.fav_club_name == club_name)
        users = db.session.execute(stmt).scalars().all()

        club.fav_count = len(users)
        db.session.commit()
    
    #Updates basic data of club, such as the club code, name and description. We shouldn't 
    # change club members too, since we should have a separate endpoint with more authentication for that
    def update_club_data(self, club_name, club_data):
        club = self.get_club_by_name(club_name)
        if club is None:
            raise ValueError(f"{club_name} does not exist")
        
        name = club_data.get("name")
        if name is not None:
            club.name = name
        code = club_data.get("code")
        if code is not None:
            club.code = code
        description = club_data.get("description")
        if description is not None:
            club.description = description
        
        db.session.commit()
        return club
    
    def get_tag_frequency(self, tag_name):
        stmt = db.select(self.club_to_tag_table).where(self.club_to_tag_table.c.tag_name == tag_name)
        resp = db.session.execute(stmt).scalars().all()
        print(resp)
        return {"tag": tag_name, "frequency": len(resp)}
    
    def get_all_tag_frequencies(self):
        stmt = db.select(Tag)
        tags = db.session.execute(stmt).scalars().all()
        tag_names = list(map(lambda t: t.name, tags))
        print(tag_names)

        resp = []
        for tag_name in tag_names:
            freq_map = self.get_tag_frequency(tag_name)
            resp.append(freq_map)
        return resp


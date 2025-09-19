import os
from app import app, db, DB_FILE
from models.club import Club, Tag
from models.user import User
import json

def create_user(): # need app context
    print("Creating josh")
    josh = User(
        name = "Josh",
        username = "joshy",
        email = "josh@joshmail.com",
        phone = "111-111-1111",
        major = "Computer Science",
        year = 1,
        clubs = []
    )

    club_codes = ['pppp', 'locustlabs']
    stmt = db.select(Club).where(Club.code.in_(club_codes))
    for row in db.session.execute(stmt):
        josh.clubs.append(row.Club)

    db.session.add(josh)
    db.session.commit()

def load_data(): # need app context
    print("Loading clubs.json...")
    with open('./clubs.json', 'r') as data_file:
        clubs = json.load(data_file)

    tag_map = {}
    for club in clubs:
        tag_list: list[Tag] = []
        for tag in club['tags']:
            if tag not in tag_map: #create new tag row if not previously encountered
                tag_map[tag] = Tag(name=tag)

            tag_list.append(tag_map[tag])
        c = Club(
            code = club['code'],
            name = club['name'],
            description = club['description'],
            tags = tag_list
        )
        db.session.add(c)
    db.session.commit()


# No need to modify the below code.
if __name__ == "__main__":

    # Delete any existing database before bootstrapping a new one.
    LOCAL_DB_FILE = "instance/" + DB_FILE
    if os.path.exists(LOCAL_DB_FILE):
        os.remove(LOCAL_DB_FILE)
    
    # t1 = Tag(name="Undergraduate")
    # t2 = Tag(name="Math")
    # c = Club(
    #     code = "ccc",
    #     name = "competitive coding club",
    #     tags = [t1, t2]
    # )

    with app.app_context():
        db.create_all()
        load_data()
        create_user()
        # db.session.add(c)
        # db.session.commit()
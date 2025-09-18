import os
from app import app, db, DB_FILE
from models import *
import json



def create_user():
    print("TODO: Create a user called josh")
    

def load_data(): # need app context
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
    # print("TODO: Load in clubs.json to the database.")


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
        create_user()
        load_data()
        # db.session.add(c)
        # db.session.commit()
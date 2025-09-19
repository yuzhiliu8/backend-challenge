from globals import db
from sqlalchemy import ForeignKey, Table

# Your database models should go here.
# Check out the Flask-SQLAlchemy quickstart for some good docs!
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/

# many to many relationship
club_to_tag_table = Table(
    "club_to_tag",
    db.metadata,
    db.Column("club_name", ForeignKey("clubs.name")),
    db.Column("tag_name", ForeignKey("tags.name"))
)

club_to_user_table = Table(
    "club_to_user",
    db.metadata,
    db.Column("user_username", ForeignKey("users.username")),
    db.Column("club_name", ForeignKey("clubs.name"))
)




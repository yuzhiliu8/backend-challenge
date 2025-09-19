from flask import Flask, request, jsonify
from blueprints.club_controller import club_controller
from blueprints.user_controller import user_controller
from services.club_service import ClubService
from services.user_service import UserService
from models.relationship_tables import club_to_tag_table
from globals import db

DB_FILE = "clubreview.db"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_FILE}"
app.register_blueprint(club_controller)
app.register_blueprint(user_controller)

club_service = ClubService(club_to_tag_table=club_to_tag_table)
user_service = UserService()
# dependency injection
club_service.user_service = user_service
user_service.club_service = club_service

db.init_app(app)
app.user_service = user_service
app.club_service = club_service

@app.route("/")
def main():
    return "Welcome Penn Club Review!"

@app.route("/api")
def api():
    return jsonify({"message": "Welcome to the Penn Club Review API!."})

if __name__ == "__main__":
    app.run(debug=True)

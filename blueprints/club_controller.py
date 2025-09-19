from flask import Blueprint, jsonify, request, current_app
from sqlalchemy.exc import IntegrityError


club_controller = Blueprint("club_controller", __name__)

@club_controller.route("/api/clubs", methods=['GET'])
def get_clubs():
    club_service = current_app.club_service
    clubs = club_service.get_all_clubs()
    if len(clubs) == 0:
        return {"msg": "No clubs found"}, 400
    
    clubs_dto_list = list(map(lambda c: c.dto_dict(), clubs))
    resp = {"clubs": clubs_dto_list}
    return jsonify(resp)

@club_controller.route("/api/search-clubs/<search_string>", methods=['GET'])
def search_clubs(search_string):
    club_service = current_app.club_service
    clubs = club_service.search_clubs(search_string)
    if len(clubs) == 0:
        return {"msg": "No clubs found"}, 400

    clubs_dto_list = list(map(lambda c: c.dto_dict(), clubs))
    resp = {"clubs": clubs_dto_list}
    return jsonify(resp)

@club_controller.route("/api/new-club", methods=['POST'])
def new_club():
    club_service = current_app.club_service
    club_data = request.get_json()
    print(club_data)
    try:
        club = club_service.create_new_club(club_data)
        return jsonify(club.dto_dict())
    except IntegrityError as e:
        msg = str(e.orig)
        return jsonify({"msg": msg}), 400

@club_controller.route("/api/update-club/<club_name>", methods=['PUT'])
def update_club(club_name):
    rq_data = request.get_json()
    club_service = current_app.club_service
    try:
        club = club_service.update_club_data(club_name, rq_data)
        return jsonify(club.dto_dict())
    except Exception as e:
        return jsonify({"msg": str(e)}), 400


@club_controller.route('/api/all-tag-frequencies', methods=['GET'])
def tag_frequency():
    club_service = current_app.club_service
    tf = club_service.get_all_tag_frequencies()
    return jsonify(tf)
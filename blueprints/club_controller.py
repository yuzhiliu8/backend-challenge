from flask import Blueprint, jsonify
from services.club_service import club_service


club_controller = Blueprint("club_controller", __name__)



@club_controller.route("/api/search-clubs/<search_string>", methods=['GET'])
def search_clubs(search_string):
    clubs = club_service.search_clubs(search_string)
    if len(clubs) == 0:
        return {"msg": "No clubs found"}, 400

    clubs_dto_list = list(map(lambda c: c.dto_dict(), clubs))
    resp = {"clubs": clubs_dto_list}
    return jsonify(resp)
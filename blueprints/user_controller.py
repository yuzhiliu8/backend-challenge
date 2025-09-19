from flask import Blueprint, jsonify
from services.user_service import user_service

user_controller = Blueprint("user_controller", __name__)

@user_controller.route("/api/get-user-profile/<username>", methods=['GET'])
def get_user_profile(username):
    user = user_service.get_user_by_username(username)
    if user is None:
        return {"msg": "No user found"}, 400
    return jsonify(user.dto_dict())
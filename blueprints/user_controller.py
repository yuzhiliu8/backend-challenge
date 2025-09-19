from flask import Blueprint, jsonify, request, current_app


user_controller = Blueprint("user_controller", __name__)

@user_controller.route("/api/get-user-profile/<username>", methods=['GET'])
def get_user_profile(username):
    user_service = current_app.user_service
    user = user_service.get_user_by_username(username)
    if user is None:
        return {"msg": "No user found"}, 400
    return jsonify(user.dto_dict())


@user_controller.route('/api/update-fav-club/<username>', methods=['PUT'])
def update_fav_club(username):
    user_service = current_app.user_service
    req = request.get_json()
    club_name = req.get('name', '')
    user = user_service.update_favorite_club(username, club_name)

    return jsonify(user.dto_dict())
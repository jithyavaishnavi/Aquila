from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.extensions import db
from app.models import Bug, User
from app.utils.decorators import role_required

bug_bp = Blueprint("bug", __name__)

@bug_bp.route("/", methods=["POST"])
@jwt_required()
@role_required("Tester", "Admin")
def create_bug():
    data = request.get_json()
    bug = Bug(title=data["title"], description=data.get("description"),
              priority=data.get("priority", "Medium"),
              reporter_id=get_jwt_identity(),
              project_id=data["project_id"])
    db.session.add(bug)
    db.session.commit()
    return jsonify({"msg": "Bug logged successfully"}), 201


@bug_bp.route("/", methods=["GET"])
@jwt_required()
def list_bugs():
    bugs = Bug.query.all()
    return jsonify([
        {"id": b.id, "title": b.title, "status": b.status, "priority": b.priority}
        for b in bugs
    ])


@bug_bp.route("/<int:bug_id>", methods=["PATCH"])
@jwt_required()
@role_required("Developer", "Admin")
def update_bug(bug_id):
    data = request.get_json()
    bug = Bug.query.get_or_404(bug_id)
    if "status" in data:
        bug.status = data["status"]
    if "assignee_id" in data:
        bug.assignee_id = data["assignee_id"]
    db.session.commit()
    return jsonify({"msg": "Bug updated"}), 200

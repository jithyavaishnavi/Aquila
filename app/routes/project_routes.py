from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.extensions import db
from app.models import Project, User
from app.utils.decorators import role_required

project_bp = Blueprint("project", __name__)

@project_bp.route("/", methods=["POST"])
@jwt_required()
@role_required("Admin")
def create_project():
    data = request.get_json()
    project = Project(name=data["name"], description=data.get("description"),
                      created_by=get_jwt_identity())
    db.session.add(project)
    db.session.commit()
    return jsonify({"msg": "Project created"}), 201


@project_bp.route("/", methods=["GET"])
@jwt_required()
def list_projects():
    projects = Project.query.all()
    return jsonify([{"id": p.id, "name": p.name, "description": p.description} for p in projects])

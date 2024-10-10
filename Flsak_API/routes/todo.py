from flask import Blueprint, request, jsonify
from middleware.auth import authenticate_token

todos_bp = Blueprint("todos", __name__)

todos = []  # In-memory storage for todos

# Middleware applied to all routes in this blueprint
@todos_bp.before_request
def before_request():
    authenticate_token()

# GET endpoint to fetch all todo items
@todos_bp.route("/", methods=["GET"])
def get_todos():
    return jsonify(todos)

# POST endpoint to create a new todo item
@todos_bp.route("/", methods=["POST"])
def create_todo():
    todo = {
        "id": len(todos) + 1,
        "title": request.json.get("title"),
        "completed": request.json.get("completed", False),
    }
    todos.append(todo)
    return jsonify(todo), 201

# PUT endpoint to update an existing todo item by id
@todos_bp.route("/<int:id>", methods=["PUT"])
def update_todo(id):
    todo = next((t for t in todos if t["id"] == id), None)
    if todo is None:
        return jsonify({"error": "Todo not found"}), 404
    todo["title"] = request.json.get("title", todo["title"])
    todo["completed"] = request.json.get("completed", todo["completed"])
    return jsonify(todo)

# DELETE endpoint to remove an existing todo item by id
@todos_bp.route("/<int:id>", methods=["DELETE"])
def delete_todo(id):
    global todos
    todos = [t for t in todos if t["id"] != id]
    return '', 204

from flask import Flask, request, jsonify

app = Flask(__name__)

# Hardcoded token for simplicity
TOKEN = "mysecrettoken"

todos = []  # In-memory storage for todos

# Middleware: Token authentication check
@app.before_request
def authenticate_token():
    token = request.headers.get("Authorization")
    if not token or token != f"Bearer {TOKEN}":
        return jsonify({"error": "Unauthorized"}), 401

# GET endpoint to fetch all todo items
@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(todos)

# POST endpoint to create a new todo item
@app.route("/todos", methods=["POST"])
def create_todo():
    todo = {
        "id": len(todos) + 1,
        "title": request.json.get("title"),
        "completed": request.json.get("completed", False),
    }
    todos.append(todo)
    return jsonify(todo), 201

# PUT endpoint to update an existing todo item by id
@app.route("/todos/<int:id>", methods=["PUT"])
def update_todo(id):
    todo = next((t for t in todos if t["id"] == id), None)
    if todo is None:
        return jsonify({"error": "Todo not found"}), 404
    todo["title"] = request.json.get("title", todo["title"])
    todo["completed"] = request.json.get("completed", todo["completed"])
    return jsonify(todo)

# DELETE endpoint to remove an existing todo item by id
@app.route("/todos/<int:id>", methods=["DELETE"])
def delete_todo(id):
    global todos
    todos = [t for t in todos if t["id"] != id]
    return '', 204

# 404 handler for unknown routes
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Resource not found"}), 404

if __name__ == "__main__":
    app.run(port=3000)


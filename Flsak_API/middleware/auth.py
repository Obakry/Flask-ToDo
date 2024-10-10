from flask import request, jsonify

# Hardcoded token for simplicity
TOKEN = "mysecrettoken"

def authenticate_token():
    token = request.headers.get("Authorization")
    if not token or token != f"Bearer {TOKEN}":
        return jsonify({"error": "Unauthorized"}), 401

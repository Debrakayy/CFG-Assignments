from flask import Flask, jsonify, request
from db_utils import execute_user, get_all_records, delete_users_by_id

app = Flask(__name__)

@app.route("/", methods=["GET"])
def root():
    return jsonify("Welcome To The Privacy API")

# GET all users
@app.route("/api/users", methods=["GET"])
def get_all_users():
    try:
        users = get_all_records()
        return jsonify(users), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# DELETE user by ID
@app.route("/api/users/remove/<int:id>", methods=["DELETE"])
def del_user_by_id(id):
    try:
        deleted_users= delete_users_by_id(id)  # Fetch remaining users after deletion
        return jsonify({
            "message": f"User with ID {id} deleted successfully",
            "remaining_users": deleted_users
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# POST: Add new user
@app.route("/api/users/add", methods=["POST"])
def add_user():
    try:
        data = request.get_json()
        if not data or not all(k in data for k in ("name", "email", "request_type")):
            return jsonify({"error": "Missing required fields"}), 400

        new_user = {
            "name": data["name"],
            "email": data["email"],
            "request_type": data["request_type"],
            "request_status": data.get("request_status", "PENDING")
        }

        # Insert into database using correct function
        execute_user(new_user)

        return jsonify({"message": "User added successfully", "user": new_user}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the app
if __name__ == "__main__":
    app.run(debug=True)

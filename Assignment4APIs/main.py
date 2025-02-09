import requests
import json,APIs

BASE_URL = "http://127.0.0.1:5000"  # Base API URL


def get_all_users_front_end():
    """Retrieve all users from the API (GET request)."""
    endpoint = f"{BASE_URL}/api/users"
    try:
        response = requests.get(endpoint)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error fetching users:", e)
        return None


def add_user():
    """Send a new user to the API (POST request)."""
    name = input("Enter name: ").strip()
    email = input("Enter email: ").strip()
    request_type = input("Enter request type (DELETE/ACCESS): ").strip().upper()

    if request_type not in ["DELETE", "ACCESS"]:
        print("Invalid request type. Please enter DELETE or ACCESS.")
        return None

    request_status = input("Enter request status (Press Enter to default to PENDING): ").strip().upper() or "PENDING"

    user_data = {
        "name": name,
        "email": email,
        "request_type": request_type,
        "request_status": request_status
    }

    endpoint = f"{BASE_URL}/api/users/add"
    try:
        response = requests.post(endpoint,
                                 headers={'Content-Type': 'application/json'},
                                 data=json.dumps(user_data))
        response.raise_for_status()  # Raise an error for bad status codes

        print("User added successfully:", response.json())
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Failed to add user:", e)
        return None


def delete_user_by_id(user_id):
    """Delete a user by ID (DELETE request)."""
    try:
        user_id = int(user_id)  # Ensure user_id is an integer
    except ValueError:
        print("Invalid ID. Please enter a valid numeric user ID.")
        return None

    endpoint = f"{BASE_URL}/api/users/remove/{user_id}"  # Corrected DELETE endpoint
    try:
        response = requests.delete(endpoint)
        response.raise_for_status()  # Raise an error for bad status codes
        print(f"User with ID {user_id} deleted successfully.")
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error deleting user:", e)
        return None


if __name__ == "__main__":
    print("Client-side API Interaction")

    # Test GET all users
    users = get_all_users_front_end()
    if users:
        print("Users:", users)

    # Test POST (Adding a new user)
    add_user()

    # Test DELETE (Removing a user)
    user_id = input("Enter the ID of the user to delete: ")
    delete_user_by_id(user_id)


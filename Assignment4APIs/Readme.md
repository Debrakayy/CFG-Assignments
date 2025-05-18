# Running the Privacy API

## Overview

The **Privacy API** is designed to manage user privacy requests, allowing users to:

Retrieve all user records (GET)

Add a new user (POST)

Delete a user by ID (DELETE)

This API interacts with a MySQL database to store and manage user requests related to data privacy.

This guide provides step-by-step instructions on how to set up, configure, and run my Privacy API.

---

## Complete before running

Before running the API, ensure you have the following installed:

- **Python (3.x)**
- **MySQL Server** (Ensure it's running)
- **pip** (Python package manager)


## Database Configuration

1. Create a MySQL database:
```sql
CREATE DATABASE privacy_db;
```
2. Edit the `config.py` file with your database credentials:
```python
USER = "your_mysql_user"
PASSWORD = ""
HOST = "localhost"
DATABASE = "privacy_db"
```

3. Run the database setup script created `users` table:
```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    request_type ENUM('DELETE', 'ACCESS') NOT NULL,
    request_status ENUM('PENDING', 'APPROVED', 'REJECTED') DEFAULT 'PENDING'
);
```

## Running the API

### 1. Install the Flask and import into api 
### 2. Start the Flask Server
```sh
python app.py
```

If you want to restart Flask:
```sh
CTRL+C  # Stop the server
python app.py  # Restart the server
```

### 2. Verify API is Running
Once the server starts, you should see an output similar to:
```
 * Running on http://127.0.0.1:5000/
```
Test it by opening the following URL in your browser:
```
http://127.0.0.1:5000/
```
It should return:
```json
"Welcome To The Privacy API"
```

## API Endpoints

| Method | Endpoint                     | Description                 |
|--------|------------------------------|-----------------------------|
| GET    | `/api/users`                 | Retrieve all users          |
| POST   | `/api/users/add `            | Add a new user              |
| DELETE | `/api/users/remove/<int:id>` | Remove a user by ID         |

## Testing the API

Use**cURL** to test the API.

### 1. Get All Users
```sh
GET- http://127.0.0.1:5000/api/users
```

### 2. Add a New User example
```sh
POST - http://127.0.0.1:5000/api/users \
     - "Content-Type: application/json" \
     -'{"name": "Natan Don", "email": "Nathan@email.com", "request_type": "ACCESS"}'
```

### 3. Delete a User Example
```sh
DELETE - http://127.0.0.1:5000/api/users/remove/1
```
## Expected Behavior

When the API is running, users can send requests to manage user privacy records.

Any errors will return JSON responses with appropriate status codes.


## Troubleshooting

- **500 Internal Server Error**: Check if MySQL is running and database credentials are correct.
- **405 Method Not Allowed**: Verify that you're using the correct HTTP method for the endpoint.
- **Connection Refused**: Ensure Flask is running before making API requests.

---

You're now ready to use the Privacy API!


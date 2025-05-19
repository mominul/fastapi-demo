# fastapi-demo
This demo uses FastAPI and SQLAlchemy to demo simple CRUD operations. It uses SQLAlchemy ORM for declaring models (table structures) and uses raw SQL queries for the CRUD operations.

This project uses MySQL version 8 as the database and has been containerized using Docker.

## Running the project :rocket:
```
docker compose build && docker compose up
```

## HTTP REST Methods
* `POST /users/` - Creates a new user
* `GET /users/{id}` - Shows details about the user.
* `PUT /users/{id}` - Updates the user info.
* `DELETE /users/{id}` - Deletes the user.

## Swagger
`http://127.0.0.1:8000/docs` endpoint shows the Swagger docs for the REST APIs exposed by this backend:

<img width="921" alt="Image" src="https://github.com/user-attachments/assets/d1130e9a-208b-40a8-b8cf-0fdd3529d67e" />

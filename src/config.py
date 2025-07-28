from datetime import timedelta
from os import path
import secrets

class Config:
    BASE_DIRECTORY = path.abspath(path.dirname(__file__))
    SECRET_KEY = secrets.token_hex(16)
    UPLOAD_PATH = path.join(BASE_DIRECTORY, "static", "uploads")
    FLASK_ADMIN_SWATCH = "simplex"
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    JWT_SECRET_KEY = "super-secret-key"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(seconds=10)
    SWAGGER_AUTHORIZATION = {
        "JsonWebToken": {
            "type": "apiKey",
            "in": "header",
            "name": "Authorization"
        }
    }
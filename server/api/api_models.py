from flask_restx import fields
from api import rest_api


user_model = rest_api.model(
    "User",
    {
        "id": fields.Integer,
        "first_name": fields.String,
        "last_name": fields.String,
        "username": fields.String,
        "profile_picture": fields.String,
        "email": fields.String,
        "password": fields.String,
        "gender": fields.String,
        "identification_card": fields.String,
        "date_of_birth": fields.Date,
        "contact": fields.String,
    },
)
post_model = rest_api.model(
    "Post",
    {
        "id": fields.Integer,
        "description": fields.String,
        "likes": fields.Integer,
        "created_at": fields.Date,
        "user": fields.Nested(user_model),
    },
)

post_input_model = rest_api.model(
    "Post",
    {
        "user_id": fields.Integer,
        "description": fields.String,
    },
)

post_input_description_model = rest_api.model(
    "Post",
    {"description": fields.String},
)


create_user_model = rest_api.model(
    "User",
    {
        "first_name": fields.String,
        "last_name": fields.String,
        "username": fields.String,
        "profile_picture": fields.String,
        "email": fields.String,
        "password": fields.String,
        "gender": fields.String,
        "identification_card": fields.String,
        "date_of_birth": fields.Date,
        "contact": fields.String,
    },
)

user_login_input_model = rest_api.model(
    "User",
    {
        "username": fields.String,
        "password": fields.String,
    },
)

like_model = rest_api.model(
    "Like",
    {"id": fields.Integer, "user_id": fields.Integer, "post_id": fields.Integer},
)

likes_input_model = rest_api.model(
    "Like",
    {"user_id": fields.Integer, "post_id": fields.Integer},
)

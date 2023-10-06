from api import app, db
from .models import User, Location, Post, Like, Comment
from flask import request, jsonify, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
import uuid
from datetime import date

from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from datetime import datetime, timedelta
from functools import wraps
from flask_restx import Resource, Namespace
from .api_models import (
    post_model,
    post_input_model,
    post_input_description_model,
    user_model,
    create_user_model,
    user_login_input_model,
    likes_input_model,
    like_model,
)

authorizations = {
    "jsonWebToken": {
        "type": "apiKey",
        "in": "header",
        "name": "Authorization"
    }
}

ns = Namespace("/", authorizations=authorizations)


class SignupResource(Resource):
    def post(self):
        pass


@ns.route("/posts")
class PostListResource(Resource):
    @ns.marshal_list_with(post_model)
    def get(self):
        posts = Post.query.all()
        return posts, 200

    @ns.expect(post_input_model)
    @ns.marshal_with(post_model)
    def post(self):
        new_post = Post(
            description=ns.payload["description"], user_id=ns.payload["user_id"]
        )
        db.session.add(new_post)
        db.session.commit()

        return new_post, 201


@ns.route("/posts/<int:id>")
class PostResource(Resource):
    @ns.marshal_with(post_model)
    def get(self, id):
        post = Post.query.filter_by(id=id).first()
        if post:
            return post, 200
        else:
            return {"error": "Post not found"}, 404

    @ns.expect(post_input_description_model)
    @ns.marshal_with(post_model)
    def patch(self, id):
        post = Post.query.filter_by(id=id).first()
        if post:
            for attr in ns.payload:
                setattr(post, attr, ns.payload[attr])
            db.session.add(post)
            db.session.commit()
            return post, 200
        else:
            return {"error": "Post not found"}, 404

    def delete(self, id):
        post = Post.query.filter_by(id=id).first()
        if post:
            db.session.delete(post)
            db.session.commit()
            return {}, 204
        else:
            return {"error": "Post not found"}, 404


@ns.route("/users")
class UsersListRersource(Resource):
    
    @ns.marshal_list_with(user_model)
    def get(self):
        users = User.query.all()
        return users, 200

    @ns.expect(user_model)
    @ns.marshal_with(create_user_model)
    def post(self):
        try:
            dob = date.fromisoformat(ns.payload["date_of_birth"])
            hashed_password = generate_password_hash(password=ns.payload["password"])
            new_user = User(
                first_name=ns.payload["first_name"],
                last_name=ns.payload["last_name"],
                username=ns.payload["username"],
                email=ns.payload["email"],
                password=hashed_password,
                profile_picture=ns.payload["profile_picture"],
                gender=ns.payload["gender"],
                date_of_birth=dob,
                identification_card=ns.payload["identification_card"],
                contact=ns.payload["contact"],
            )
            db.session.add(new_user)
            db.session.commit()

            return new_user, 201
        except Exception as e:
            print(e.args)
            return {"error": f"User registration error {str(e)}"}, 400


@ns.route("/users/<int:id>")
class UserResourse(Resource):
    @ns.marshal_with(user_model)
    def get(self, id):
        user = User.query.filter_by(id=id).first()
        if user:
            return user, 200
        else:
            return {"error": "User not found"}, 404

    @ns.marshal_with(user_model)
    @ns.expect(create_user_model)
    def patch(self, id):
        user = User.query.filter_by(id=id).first()
        if user:
            for attr in ns.payload:
                setattr(user, attr, ns.payload[attr])
            db.session.add(user)
            db.session.commit()
            return user, 200
        else:
            return {"error": "User not found"}, 404


@ns.route("/login")
class UserLoginResource(Resource):
    @ns.expect(user_login_input_model)
    def post(self):
        user = User.query.filter_by(username=ns.payload["username"]).first()
        if not user:
            return {"error": "User does not exist"}, 401
        if not check_password_hash(user.password, ns.payload["password"]):
            return {"error": "Incorrect password, Try Again"}, 401
        user_dic = {"id": user.id,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "profile_picture": user.profile_picture}
        return {"access_token": create_access_token(user_dic)}


@ns.route("/likes")
class LikesResource(Resource):
    @ns.expect(likes_input_model)
    @ns.marshal_with(like_model)
    def post(self):
        try:
            new_like = Like(
                user_id=ns.payload["user_id"], post_id=ns.payload["post_id"]
            )
            db.session.add(new_like)
            db.session.commit()
            return new_like, 201
        except Exception:
            return {"error": f"Like not created error"}, 400

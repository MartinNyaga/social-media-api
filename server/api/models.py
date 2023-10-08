from api import db
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    username = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    profile_picture = db.Column(db.String)
    gender = db.Column(db.String)
    bio = db.Column(db.String(500))
    date_of_birth = db.Column(db.DateTime)
    identification_card = db.Column(db.Integer)
    contact = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )

    locations = db.relationship("Location", backref="user")
    posts = db.relationship("Post", backref="user")
    liked_posts = db.relationship(
        "Post", secondary="likes", back_populates="user_likes"
    )
    # comments = db.relationship('Comment', backref='user', lazy=True)


class Location(db.Model):
    __tablename__ = "locations"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    city = db.Column(db.String)
    country = db.Column(db.String)


class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    description = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )

    user_likes = db.relationship(
        "User", secondary="likes", back_populates="liked_posts"
    )
    # comments = db.relationship("Comment", backref="post", lazy=True)

    @property
    def likes(self):
        post_likes = Like.query.filter_by(post_id=self.id).all()
        return len(post_likes)


class Like(db.Model):
    __tablename__ = "likes"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))

    # liked_by_user = db.relationship('User', backref='likes', lazy=True)
    # liked_post = db.relationship('Post', backref='likes', lazy=True)


class Comment(db.Model):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))
    description = db.Column(db.String)

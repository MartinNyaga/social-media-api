from faker import Faker
import random
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app import app
from api.models import db, User, Location, Post, Like, Comment

fake = Faker()

with app.app_context():
    db.create_all()

    # Clear existing data
    db.session.query(User).delete()
    db.session.query(Location).delete()
    db.session.query(Post).delete()
    db.session.query(Like).delete()
    db.session.query(Comment).delete()
    db.session.commit()

    # Create users
    users = []
    for _ in range(20):
        user = User(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            username=fake.user_name(),
            email=fake.email(),
            password=fake.password(),
            gender=fake.random_element(elements=("Male", "Female")),
            date_of_birth=fake.date_of_birth(minimum_age=18, maximum_age=65),
            identification_card=fake.random_int(min=100000, max=999999),
            contact=fake.random_int(min=1000000000, max=9999999999),
        )
        users.append(user)
    db.session.add_all(users)
    db.session.commit()

    # Create locations
    locations = []
    for user in users:
        location = Location(
            user=user,
            city=fake.city(),
            country=fake.country(),
        )
        locations.append(location)
    db.session.add_all(locations)
    db.session.commit()

    # Create posts
    posts = []
    for user in users:
        for _ in range(random.randint(1, 5)):
            post = Post(
                user=user,
                description=fake.text(max_nb_chars=200),
                likes=random.randint(0, 100),
                created_at=fake.date_time_between(start_date='-1y', end_date='now', tzinfo=None),
            )
            posts.append(post)
    db.session.add_all(posts)
    db.session.commit()

    # Create likes
    likes = []
    for user in users:
        for post in posts:
            if random.random() < 0.3:  # Likelihood of liking a post
                like = Like(
                    user=user,
                    post=post,
                )
                likes.append(like)
    db.session.add_all(likes)
    db.session.commit()

    # Create comments
    comments = []
    for user in users:
        for post in posts:
            if random.random() < 0.5:  # Likelihood of commenting on a post
                comment = Comment(
                    user=user,
                    post=post,
                    description=fake.text(max_nb_chars=100),
                )
                comments.append(comment)
    db.session

from faker import Faker
import random
from api import app

from api.models import db, User, Location, Post, Like, Comment

with app.app_context():
    fake = Faker()

    User.query.delete()
    Location.query.delete()
    Post.query.delete()
    Like.query.delete()
    Comment.query.delete()
    db.session.commit()

    users = []
    for i in range(20):
        user = User(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            username=fake.email(),
            email=fake.email(),
            password=fake.password(),
            gender=random.choice(["M", "F"]),
            date_of_birth=fake.date_of_birth(),
            identification_card=fake.random_number(digits=8),
            contact=fake.random_number(digits=10),
            created_at=fake.date_time(),
            updated_at=fake.date_time(),
        )
        users.append(user)

    db.session.add_all(users)
    db.session.commit()

    locations = []
    for i in range(20):
        location = Location(
            user_id=random.randint(1, 20), city=fake.city(), country=fake.country()
        )
        locations.append(location)
    db.session.add_all(locations)
    db.session.commit()

    posts = []
    for i in range(20):
        post = Post(
            user_id=random.randint(1, 20),
            description=fake.text(),
            created_at=fake.date_time(),
            updated_at=fake.date_time(),
        )
        posts.append(post)
    db.session.add_all(posts)
    db.session.commit()

    likes = []
    for i in range(20):
        like = Like(
            user_id=random.randint(1, 20),
            post_id=random.randint(1, 20),
        )
        likes.append(like)
    db.session.add_all(likes)
    db.session.commit()

    comments = []
    for i in range(20):
        comment = Comment(
            user_id=random.randint(1, 20),
            post_id=random.randint(1, 20),
            description=fake.text(),
        )
        comments.append(comment)
    db.session.add_all(comments)
    db.session.commit()

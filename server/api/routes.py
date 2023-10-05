from api import app, db
from .models import User, Location, Post, Like, Comment
from flask import  request, jsonify, make_response
import uuid 
from  werkzeug.security import generate_password_hash, check_password_hash
import jwt
from datetime import datetime, timedelta
from functools import wraps

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        
        if not token:
            return jsonify({'message' : 'Token is missing !!'}), 401
  
        try:
            
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = User.query\
                .filter_by(public_id = data['public_id'])\
                .first()
        except:
            return jsonify({
                'message' : 'Token is invalid !!'
            }), 401
        
        return  f(current_user, *args, **kwargs)
  
    return decorated

# signup route
@app.route('/signup', methods =['POST'])
def signup():
    
    data = request.get_json()
  
    
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    username = data.get('username')
    profil_picture = data.get('profil_picture')
    gender = data.get('gender')
    date_of_birth = data.get('date_of_birth')
    identification_card = data.get('identification_card')
    contact = data.get('contact')
    email = data.get('email') 
    password = data.get('password')
  
    
    user = User.query\
        .filter_by(email = email)\
        .first()
    if not user:
        
        user = User(
            public_id = str(uuid.uuid4()),
            first_namename = first_name,
            last_name = last_name,
            username = username,
            profil_picture = profil_picture,
            gender = gender,
            date_of_birth = date_of_birth,
            identification_card = identification_card,
            contact = contact,
            email = email,
            password = generate_password_hash(password)
        )
        
        db.session.add(user)
        db.session.commit()
  
        return make_response('Successfully registered.', 201)
    else:
        
        return make_response('User already exists. Please Log in.', 202)

# Route for user login
@app.route('/login', methods =['POST'])
def login():
    
    auth = request.get_json()
  
    if not auth or not auth.get('email') or not auth.get('password'):
        
        return make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate' : 'Basic realm ="Login required !!"'}
        )
  
    user = User.query\
        .filter_by(email = auth.get('email'))\
        .first()
  
    if not user:
        
        return make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate' : 'Basic realm ="User does not exist !!"'}
        )
  
    if check_password_hash(user.password, auth.get('password')):
        
        token = jwt.encode({
            'public_id': user.public_id,
            'exp' : datetime.utcnow() + timedelta(minutes = 30)
        }, app.config['SECRET_KEY'])
  
        return make_response(jsonify({'token' : token.decode('UTF-8')}), 201)
    
    return make_response(
        'Could not verify',
        403,
        {'WWW-Authenticate' : 'Basic realm ="Wrong Password !!"'}
    )


@app.route('/')
def home():
    return make_response(jsonify({"msg": "CONNECTING"}), 200)



@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.serialize() for user in users])

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    return jsonify(user.serialize())


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    data = request.get_json()
    for key, value in data.items():
        setattr(user, key, value)
    db.session.commit()
    return jsonify(user.serialize())

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    return '', 204

@app.route('/locations', methods=['GET'])
def get_locations():
    locations = Location.query.all()
    return jsonify([location.serialize() for location in locations])

@app.route('/locations/<int:location_id>', methods=['GET'])
def get_location(location_id):
    location = Location.query.get(location_id)
    return jsonify(location.serialize())

@app.route('/locations', methods=['POST'])
def create_location():
    data = request.get_json()
    new_location = Location(**data)
    db.session.add(new_location)
    db.session.commit()
    return jsonify(new_location.serialize())

@app.route('/locations/<int:location_id>', methods=['PUT'])
def update_location(location_id):
    location = Location.query.get(location_id)
    data = request.get_json()
    for key, value in data.items():
        setattr(location, key, value)
    db.session.commit()
    return jsonify(location.serialize())

@app.route('/locations/<int:location_id>', methods=['DELETE'])
def delete_location(location_id):
    location = Location.query.get(location_id)
    db.session.delete(location)
    db.session.commit()
    return '', 204

@app.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return jsonify([post.serialize() for post in posts])

@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = Post.query.get(post_id)
    return jsonify(post.serialize())

@app.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    new_post = Post(**data)
    db.session.add(new_post)
    db.session.commit()
    return jsonify(new_post.serialize())

@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    post = Post.query.get(post_id)
    data = request.get_json()
    for key, value in data.items():
        setattr(post, key, value)
        db.session.commit()
        return jsonify(post.serialize())

@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
        post = Post.query.get(post_id)
        db.session.delete(post)
        db.session.commit()
        return '', 204

@app.route('/likes', methods=['GET'])
def get_likes():
        likes = Like.query.all()
        return jsonify([like.serialize() for like in likes])

@app.route('/likes/<int:like_id>', methods=['GET'])
def get_like(like_id):
        like = Like.query.get(like_id)
        return jsonify(like.serialize())

@app.route('/likes', methods=['POST'])
def create_like():
        data = request.get_json()
        new_like = Like(**data)
        db.session.add(new_like)
        db.session.commit()
        return jsonify(new_like.serialize())

@app.route('/likes/<int:like_id>', methods=['PUT'])
def update_like(like_id):
        like = Like.query.get(like_id)
        data = request.get_json()
        for key, value in data.items():
            setattr(like, key, value)
            db.session.commit()
            return jsonify(like.serialize())

@app.route('/likes/<int:like_id>', methods=['DELETE'])
def delete_like(like_id):
            like = Like.query.get(like_id)
            db.session.delete(like)
            db.session.commit()
            return '', 204


@app.route('/comments/<int:id>', methods=['GET'])
def get_comment(id):
    comment = Comment.query.get_or_404(id)
    return jsonify({
        'id': comment.id,
        'user_id': comment.user_id,
        'post_id': comment.post_id,
        'description': comment.description
    })





            
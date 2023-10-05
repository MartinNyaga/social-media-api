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





            
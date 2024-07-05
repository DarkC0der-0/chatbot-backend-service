from flask import Blueprint, request, jsonify
from .models import User, Conversation
from . import db, bcrypt
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from .nlp.nlp_service.py import get_response

main = Blueprint('main', __name__)

@main.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    user = User(username=data['username'], password=hashed_password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@main.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and bcrypt.check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity=user.id)
        return jsonify({'access_token': access_token}), 200
    return jsonify({'message': 'Login failed'}), 401

@main.route('/chat', methods=['POST'])
@jwt_required()
def chat():
    data = request.get_json()
    user_id = get_jwt_identity()
    user_message = data['message']
    bot_response = get_response(user_message)
    
    conversation = Conversation(user_id=user_id, message=user_message, response=bot_response)
    db.session.add(conversation)
    db.session.commit()
    
    return jsonify({'response': bot_response}), 200

@main.route('/history', methods=['GET'])
@jwt_required()
def history():
    user_id = get_jwt_identity()
    conversations = Conversation.query.filter_by(user_id=user_id).all()
    output = []
    for conv in conversations:
        output.append({'message': conv.message, 'response': conv.response, 'timestamp': conv.timestamp})
    return jsonify({'history': output}), 200

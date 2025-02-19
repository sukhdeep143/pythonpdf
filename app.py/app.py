from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import bcrypt

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "secretkey"  # Change this in production
jwt = JWTManager(app)

users_db = {}

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data["username"]
    password = bcrypt.hashpw(data["password"].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    users_db[username] = password
    return jsonify({"message": "User registered"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data["username"]
    user_password = users_db.get(username)

    if not user_password or not bcrypt.checkpw(data["password"].encode('utf-8'), user_password.encode('utf-8')):
        return jsonify({"message": "Invalid credentials"}), 401

    token = create_access_token(identity=username)
    return jsonify({"token": token})

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify({"message": "You are authenticated!", "user": current_user})

if __name__ == '__main__':
    app.run(debug=True)

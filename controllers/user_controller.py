from flask import jsonify, request
from models.user_model import db, User

def register_user():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")
    confirm_password = data.get("confirm")

    if not username or not password or not email or not confirm_password:
        return jsonify({"message": "Username dan password wajib diisi"}), 400

    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({"message": "Username sudah terdaftar"}), 409

    new_user = User(username, email, password, confirm_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "Registrasi berhasil"}), 201


def login_user():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"message": "User tidak ditemukan"}), 404

    if not user.check_password(password):
        return jsonify({"message": "Password salah"}), 401

    return jsonify({"message": "Login berhasil", "username": username}), 200

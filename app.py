from flask import Flask, request, jsonify, render_template
from models.user_model import db
from controllers.user_controller import register_user, login_user




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)




# Inisialisasi database
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return jsonify({"message": "API aktif"})


@app.route('/register', methods=['POST'])
def register():
    return register_user()

@app.route('/login', methods=['GET','POST'])
def login():
    return user_controller.login_user()

@app.route('/dashboard')
def dashboard():
    return render_template('pages/dashboard/dashboard.html')


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///game.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a Player model
class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route("/api/hello")
def hello():
    return jsonify({"message": "Hello from Flask backend on Vercel!"})

@app.route("/api/players", methods=["GET"])
def get_players():
    players = Player.query.all()
    return jsonify([{"id": p.id, "username": p.username} for p in players])

@app.route("/api/players", methods=["POST"])
def add_player():
    data = request.get_json()
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if Player.query.filter_by(username=username).first():
        return jsonify({"error": "Username already exists"}), 400
    new_player = Player(username=username)
    db.session.add(new_player)
    db.session.commit()
    return jsonify({"message": f"Player '{username}' added successfully."}), 201

if __name__ == "__main__":
    app.run()

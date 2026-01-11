from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from models import db, Episode, Guest, Appearance

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)


@app.route('/episodes', methods=['GET'])
def episodes():
    episodes = Episode.query.all()
    return jsonify([e.to_dict() for e in episodes]), 200

@app.route('/episodes/<int:id>', methods=['GET'])
def episode_by_id(id):
    episode = Episode.query.get(id)

    if not episode:
        return jsonify({"error": "Episode not found"}), 404

    return jsonify({
        **episode.to_dict(),
        "appearances": [
            {
                "id": a.id,
                "rating": a.rating,
                "episode_id": a.episode_id,
                "guest_id": a.guest_id,
                "guest": a.guest.to_dict()
            }
            for a in episode.appearances
        ]
    }), 200


@app.route('/guests', methods=['GET'])
def guests():
    guests = Guest.query.all()
    return jsonify([g.to_dict() for g in guests]), 200


@app.route('/appearances', methods=['POST'])
def create_appearance():
    data = request.get_json()

    try:
        appearance = Appearance(
            rating=data['rating'],
            episode_id=data['episode_id'],
            guest_id=data['guest_id']
        )

        db.session.add(appearance)
        db.session.commit()

        return jsonify(appearance.to_dict()), 201

    except Exception as e:
        return jsonify({"errors": [str(e)]}), 400

if __name__ == "__main__":
    app.run(debug=True)
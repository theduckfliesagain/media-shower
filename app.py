import sqlite3
from dataclasses import dataclass, asdict
from flask import Flask, jsonify, request
from flask_cors import CORS
import json
# from controllers import planets
from werkzeug import exceptions
# from db import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///planets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

CORS(app)


class Planet(db.Model):
    __tablename__ = 'planets'
    id = db.Column('planet_id', db.Integer, primary_key = True)
    name = db.Column(db.String(30))
    num_moons = db.Column(db.Integer)
    
    def __repr__(self):
        return '<Planet %r>' % self.name
    
    def __init__(self, name, num_moons):
        self.name = name
        self.num_moons = num_moons

    

@app.route('/')
def home():
    try:
        db.session.query(text('1')).from_statement(text('SELECT 1')).all()
        return '<h1>Planets</h1>' + '<p>In the beginning the Universe was created. This has made a lot of people very angry and has been widely regarded as a bad move.</p>'
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text
    # return jsonify({'message': 'Welcome to the Media Shower API!'}), 200

@app.route('/planets', methods=['GET'])
def index():
    try:
        hed = '<h1>Wow planets</h1>'
        planets = Planet.query.all()

        planet_text = '<ul>'
        for planet in planets:
            planet_text += f"<li>{planet.name} has {planet.num_moons} moons </li>"
        planet_text += '</ul>'
        return (hed + planet_text), 200
    except Exception as e:
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text, 404


@app.route('/planets', methods=['POST'])
def create():
        body = request.get_json()
        db.session.add(Planet(body["name"], body["num_moons"]))
        db.session.commit()
        return jsonify(body), 200

@app.route('/planets/:id', methods=['GET'])
def show(id):
    try:
        planet = Planet.filter_by(id= id).first()
        return f"{planet.name} has {planet.num_moons} moons", 200
    except Exception as e:
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text






if __name__ == "__main__":
    app.run(debug=True)

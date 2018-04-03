from __main__ import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

#Tabel
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class Country(db.Model):
    country_code = db.Column(db.String(2), primary_key=True)
    country_name = db.Column(db.String(45), nullable=False)

    cities = db.relationship('City', backref='country', lazy='dynamic')

    def __repr__(self):
        return '<Country %r>' % self.country_code

class City(db.Model):
    city_code = db.Column(db.String(3), primary_key=True)
    country_code = db.Column(db.String(2), db.ForeignKey('country.country_code'), nullable=False)
    city_name = db.Column(db.String(255), nullable=False)
    zone_id = db.Column(db.Integer(), nullable=False)
    has_airport = db.Column(db.Integer(), nullable=False)

    def __repr__(self):
        return '<Country %r>' % self.city_code

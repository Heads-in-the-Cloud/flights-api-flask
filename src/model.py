from src import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


####################
# Create DB Models #
####################

class Flight(db.Model):
    __tablename__ = 'flight'

    id = db.Column(db.Integer, primary_key=True)
    route_id = db.Column(db.Integer, ForeignKey('route.id'), nullable=False)
    airplane_id = db.Column(db.Integer, ForeignKey('airplane.id'), nullable=False)
    departure_time = db.Column(db.DateTime)
    reserved_seats = db.Column(db.Integer)
    seat_price = db.Column(db.Float(precision=None, decimal_return_scale=2))


class Route(db.Model):
    __tablename__ = 'route'

    id = db.Column(db.Integer, primary_key=True)
    destination_id = db.Column(db.String(3), ForeignKey('airport.iata_id'))
    origin_id = db.Column(db.String(3), ForeignKey('airport.iata_id'))
    # flights = relationship('Flight', backref='route', lazy='subquery', cascade='all')
    # origin_airport = relationship('Airport', primaryjoin='Airport.iata_id == Route.origin_id')
    # destination_airport = relationship('Airport', primaryjoin='Airport.iata_id == Route.destination_id')


class Airport(db.Model):
    __tablename__ = 'airport'

    iata_id = db.Column(db.String(3), primary_key=True)
    city = db.Column(db.String(45))


class Airplane(db.Model):
    __tablename__ = "airplane"

    id = db.Column(db.Integer, primary_key=True)
    type_id = db.Column(db.Integer, ForeignKey('airplane_type.id'))
    # flights = relationship('Flight', backref='airplane', lazy='subquery', cascade='all')
    # airplane_type = relationship('AirplaneType', primaryjoin='AirplaneType.id == Airplane.id')


class AirplaneType(db.Model):
    __tablename__ = "airplane_type"

    id = db.Column(db.Integer, primary_key=True)
    max_capacity = db.Column(db.Integer)

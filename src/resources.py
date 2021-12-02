from flask import request
from flask_restful import Api, Resource
from src.schema import *
from src.model import *

# from flask_jwt_extended import JWTManager
#
# jwt = JWTManager(app)

########################
# Create API functions #
########################


# AIRPORTS

class AllAirports(Resource):
    # get all
    def get(self):
        airports = Airport.query.all()
        return airports_schema.dump(airports)

    # post new
    def post(self):
        airport = Airport(
            iata_id=request.json['iata_id'],
            city=request.json['city']
        )
        db.session.add(airport)
        db.session.commit()
        return airport_schema.dump(airport)


class SingleAirport(Resource):
    # get one
    def get(self, iata_id):
        airport = Airport.query.get_or_404(iata_id)
        return airport_schema.dump(airport)

    # update
    def put(self, iata_id):
        airport = Airport.query.get_or_404(iata_id)
        airport.city = request.json['city']
        db.session.commit()
        return airport_schema.dump(airport)

    # delete
    def delete(self, iata_id):
        airport = Airport.query.get_or_404(iata_id)
        db.session.delete(airport)
        db.session.commit()
        return '', 204


# ROUTES

class AllRoutes(Resource):
    # get all
    def get(self):
        routes = Route.query.all()
        return routes_schema.dump(routes)

    # post new
    def post(self):
        route = Route(
            destination_id=request.json['destination'],
            origin_id=request.json['origin']
        )
        db.session.add(route)
        db.session.commit()
        return route_schema.dump(route)


class SingleRoute(Resource):
    # get one
    def get(self, id):
        route = Route.query.get_or_404(id)
        return route_schema.dump(route)

    # update
    def put(self, id):
        route = Route.query.get_or_404(id)
        route.origin_id = request.json['origin']
        route.destination_id = request.json['destination']
        db.session.commit()
        return route_schema.dump(route)

    # delete
    def delete(self, id):
        route = Route.query.get_or_404(id)
        db.session.delete(route)
        db.session.commit()
        return '', 204


# AIRPLANE TYPES

class AllAirplaneTypes(Resource):
    # get all
    def get(self):
        airplane_types = AirplaneType.query.all()
        return airplane_types_schema.dump(airplane_types)

    # post new
    def post(self):
        airplane_type = AirplaneType(
            max_capacity=request.json['maxCapacity']
        )
        db.session.add(airplane_type)
        db.session.commit()
        return airplane_type_schema.dump(airplane_type)


class SingleAirplaneType(Resource):
    # get one
    def get(self, id):
        airplane_type = AirplaneType.query.get_or_404(id)
        return airplane_type_schema.dump(airplane_type)

    # update
    def put(self, id):
        airplane_type = AirplaneType.query.get_or_404(id)
        airplane_type.max_capacity = request.json['maxCapacity']
        db.session.commit()
        return airplane_type_schema.dump(airplane_type)

    # delete
    def delete(self, id):
        airplane_type = AirplaneType.query.get_or_404(id)
        db.session.delete(airplane_type)
        db.session.commit()
        return '', 204


# AIRPLANES

class AllAirplanes(Resource):
    # get all
    def get(self):
        airplanes = Airplane.query.all()
        return airplanes_schema.dump(airplanes)

    # post new
    def post(self):
        airplane = Airplane(
            type_id=request.json['airplaneType']
        )
        db.session.add(airplane)
        db.session.commit()
        return airplane_schema.dump(airplane)


class SingleAirplane(Resource):
    # get one
    def get(self, id):
        airplane = Airplane.query.get_or_404(id)
        return airplane_schema.dump(airplane)

    # update
    def put(self, id):
        airplane = Airplane.query.get_or_404(id)
        airplane.type_id = request.json['airplaneType']
        db.session.commit()
        return airplane_schema.dump(airplane)

    # delete
    def delete(self, id):
        airplane = Airplane.query.get_or_404(id)
        db.session.delete(airplane)
        db.session.commit()
        return '', 204


# FLIGHTS

class AllFlights(Resource):
    # get all
    def get(self):
        flights = Flight.query.all()
        return flights_schema.dump(flights)

    # post new
    def post(self):
        flight = Flight(
            route_id=request.json['route'],
            airplane_id=request.json['airplane'],
            departure_time=request.json['dateTime'],
            reserved_seats=request.json['reservedSeats'],
            seat_price=request.json['seatPrice']
        )
        db.session.add(flight)
        db.session.commit()
        return flight_schema.dump(flight)


class SingleFlight(Resource):
    # get one
    def get(self, id):
        flight = Flight.query.get_or_404(id)
        return flight_schema.dump(flight)

    # update
    def put(self, id):
        flight = Flight.query.get_or_404(id)
        flight.route_id = request.json['route']
        flight.airplane_id = request.json['airplane']
        flight.departure_time = request.json['dateTime']
        flight.reserved_seats = request.json['reservedSeats']
        flight.seat_price = request.json['seatPrice']
        db.session.commit()
        return flight_schema.dump(flight)

    # delete
    def delete(self, id):
        flight = Flight.query.get_or_404(id)
        db.session.delete(flight)
        db.session.commit()
        return '', 204


######################
# Create Restful Api #
######################


api = Api()

api.add_resource(AllAirports, '/api/v1/airports')
api.add_resource(SingleAirport, '/api/v1/airports/<iata_id>')

api.add_resource(AllRoutes, '/api/v1/routes')
api.add_resource(SingleRoute, '/api/v1/routes/<id>')

api.add_resource(AllAirplaneTypes, '/api/v1/airplaneTypes')
api.add_resource(SingleAirplaneType, '/api/v1/airplaneTypes/<id>')

api.add_resource(AllAirplanes, '/api/v1/airplanes')
api.add_resource(SingleAirplane, '/api/v1/airplanes/<id>')

api.add_resource(AllFlights, '/api/v1/flights')
api.add_resource(SingleFlight, '/api/v1/flights/<id>')

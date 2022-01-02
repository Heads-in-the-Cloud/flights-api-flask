from src import ma, model


##################
# Create Schemas #
##################

class FlightSchema(ma.Schema):
    class Meta:
        fields = ("id", "route_id", "airplane_id", "departure_time", "reserved_seats", "seat_price")
        model = model.Flight


class RouteSchema(ma.Schema):
    class Meta:
        fields = ("id", "origin_id", "destination_id")
        model = model.Route


class AirportSchema(ma.Schema):
    class Meta:
        fields = ("iata_id", "city")
        model = model.Airport


class AirplaneSchema(ma.Schema):
    class Meta:
        fields = ("id", "type_id")
        model = model.Airplane


class AirplaneTypeSchema(ma.Schema):
    class Meta:
        fields = ("id", "max_capacity")
        model = model.AirplaneType


###################
# Declare Schemas #
###################

flight_schema = FlightSchema()
flights_schema = FlightSchema(many=True)

route_schema = RouteSchema()
routes_schema = RouteSchema(many=True)

airport_schema = AirportSchema()
airports_schema = AirportSchema(many=True)

airplane_schema = AirplaneSchema()
airplanes_schema = AirplaneSchema(many=True)

airplane_type_schema = AirplaneTypeSchema()
airplane_types_schema = AirplaneTypeSchema(many=True)

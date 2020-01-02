class Report:
    def __init__(self, _date, _time, _no_empty_tracks, _no_occupied_tracks, _no_empty_gates, _no_occupied_gates):
        self.date = _date
        self.time = _time
        self.no_empty_tracks = _no_empty_tracks
        self.no_occupied_tracks = _no_occupied_tracks
        self.no_empty_gates = _no_empty_gates
        self.no_occupied_gates = _no_occupied_gates

    def write_file(self):
        statistics_file = open("data/statistics.csv", "w+")
        statistics_file.write("date,time,# of empty tracks,# of occupied tracks, # of empty gates,# of occupied gates\n")
        statistics_file.write(self.date+",")
        statistics_file.write(self.time+",")
        statistics_file.write(str(self.no_empty_tracks)+",")
        statistics_file.write(str(self.no_occupied_tracks)+",")
        statistics_file.write(str(self.no_empty_gates)+",")
        statistics_file.write(str(self.no_occupied_gates)+",")



class Airport:
    def __init__(self):
        self.tracks = None
        self.airplanes = None
        self.passengers = None
        self.pilots = None
        self.attendants = "vacío"
        self.travellers = None

    def populate_airport(self):
        data_loader = AirportAD()
        self.pilots = data_loader.read_pilots()
        self.flights = data_loader.read_flights()
        self.attendants = data_loader.read_attendants()

    def generate_statistics(self, _date, _time):

        number_empty_tracks = 0
        number_of_occupied_tracks = 0
        number_of_empty_gates = 0
        number_of_occupied_gates = 0

        for flight in self.flights.values():
            # origin
            if flight.origin == "Ciudad de Mexico - MEXICO":
                date = flight.departure.split("_")[0]
                time = flight.departure.split("_")[1]
            else:
                date = flight.arriving.split("_")[0]
                time = flight.arriving.split("_")[1]

            if date == _date and int(time) == int(_time):
                # counting tracks
                if flight.status in ["boarded", "landing"]:
                    number_of_occupied_tracks += 1
                else:
                    number_empty_tracks += 1

                # counting gates
                if flight.status in ["boarded", "landing", "in transit"]:
                    number_of_empty_gates += 1
                else:
                    number_of_occupied_gates += 1

        report = Report(_date, _time, number_empty_tracks,
                        number_of_occupied_tracks,
                        number_of_empty_gates, number_of_occupied_gates)

        report.write_file()








class Flight:
    def __init__(self, _id, _plate, _origin, _destiny,
                 _departure, _arriving, _status, _departure_gate,
                 _take_off_track, _arriving_gate, _landing_track,
                 _pilot, _copilot, _attendants):

        self.id = _id
        self.plate = _plate
        self.origin = _origin
        self.destiny = _destiny
        self.departure = _departure
        self.arriving = _arriving
        self.status = _status
        self.departure_gate = _departure_gate
        self.take_off_track = _take_off_track
        self.arriving_gate = _arriving
        self.landing_track = _landing_track
        self.pilot = _pilot
        self.copilot = _copilot
        self.attendants = _attendants


class Crew:
    def __init__(self, _passport, _forename, _surname, _date_of_birth,
                 _country, _gender, _marital_status):
        self.passport = _passport
        self.forename = _forename
        self.surname = _surname
        self.date_of_birth = _date_of_birth
        self.country = _country
        self.gender = _gender
        self.marital_status = _marital_status


class Attendant(Crew):
    pass


class Pilot(Crew):
    pass


class AirportAD:

    def read_attendants(self):
        attendants_file = open("data/attendants.csv", "r", encoding="utf-8")
        lines = attendants_file.readlines()
        attendants_file.close()
        lines.pop(0)

        attendants = {}

        for l in lines:
            fields = l.split(",")
            passport = fields[0]
            attendant = Attendant(passport, fields[1], fields[2],
                                  fields[3], fields[4], fields[5], fields[6])
            attendants[passport] = attendant
        return attendants

    def read_pilots(self):
        pilots_file = open("data/pilots.csv", "r", encoding="utf-8")
        lines = pilots_file.readlines()
        pilots_file.close()
        lines.pop(0)

        pilots = {}

        for l in lines:
            fields = l.split(",")
            passport = fields[0]
            pilot = Pilot(passport, fields[1], fields[2],
                           fields[3], fields[4], fields[5], fields[6])
            pilots[passport] = pilot
        return pilots

    def read_flights(self):
        flights_file = open("data/flights.csv", "r", encoding="utf-8")
        lines = flights_file.readlines()
        flights_file.close()
        lines.pop(0)

        flights = {}

        for l in lines:
            fields = l.split(",")
            id = fields[0]
            plate = fields[1]
            flight = Flight(id, plate, fields[2],
                            fields[3], fields[4], fields[5], fields[6],
                            fields[7], fields[8], fields[9], fields[10],
                            fields[11], fields[12], fields[13])
            flights[id+plate] = flight

        return flights

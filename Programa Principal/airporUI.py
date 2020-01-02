class AirportUI:
    def get_user_input(self):
        print("Introduce date in format YYMMDD")
        date = input()
        print("Introduce time in format HHMM")
        time = input()

        return date, time

#Ricardo Adolfo Gonzalez Terán
#ITESM Campus Toluca
#A01769410

#-*- coding:utf-8 -*-

class Flights:

    def __init__(self, identificator, departure, arrive, no_passengers):

        self.identificator = identificator
        self.departure = departure
        self.arrive = arrive
        self.passenegers = no_passengers

    def create_diccionary(self):

        file = open("datos_vuelos.csv", "r")
        lines = file.readlines()
        lines.pop(0)

        flights_d = {}

        for line in lines:

            fields = line.split(",")
            identificator = fields[0]
            departure = fields[1]
            arrive = fields[2]
            no_passengers = fields[3]

            flight = Flights(identificator, departure, arrive, no_passengers)

            flights_d[identificator+departure] = flight

        return flights_d


class Statistics:

    def read_input_file(self):
        input_file = open("datos_vuelos.csv", "r")  # Abrimos el archivo con los datos
        lines_in_file = input_file.readlines()  # Leemos todos lod datos como una lista que contenga cada una de las líneas
        input_file.close()  # Cerramos el archivo
        lines_in_file.pop(0)  # Removemos la primer línea que es el encabezado del archivo

        return lines_in_file

    def data_flight(self):
        data_loader = Flights()
        #Carga de datos
        flight = data_loader.read_input_file()

    def convert_plate_to_country(self, plate):
        plates = {  # Creamos un diccionario que mapeé los prefijos de las matrículas hacia el país que le corresponden
            "D": "Alemania",
            "PP": "Brasil",
            "CF": "Canadá",
            "A7": "Catar",
            "CC": "Chile",
            "B": "China",
            "OY": "Dinamarca",
            "HC": "Ecuador",
            "A6": "Emiratos Árabes",
            "EC": "España",
            "N": "Estados Unidos",
            "PK": "Indonesia",
            "JA": "Japón",
            "XA": "México",
            "9V": "Singapur",
            "HS": "Tailandia"
        }

        for i in range(3, 0, -1):
            plate_prefix = plate[0:i]
            if plate_prefix in plates.keys():
                country = plates[plate_prefix]
                print("Country found for prefix ", plate_prefix, "is ", country)
                return country

        return "Otro"

    def convert_date_to_month(self, date):
        months = {  # Creamos un diccionario que mapeé el número de mes a su nombre
            "01": "Enero",
            "02": "Febrero",
            "03": "Marzo",
            "04": "Abril",
            "05": "Mayo",
            "06": "Junio",
            "07": "Julio",
            "08": "Agosto",
            "09": "Septiembre",
            "10": "Octubre",
            "11": "Noviembre",
            "12": "Diciembre"
        }

        month_number = date[3:5] # Obtenermos del número del mes a partir del tercer y hasta el quinto caracter
        #print("Month number: ", month_number)
        if month_number in months.keys():
            month_name = months[month_number]  # Si el número está en las llaves, obtenemos el nombre del mes correspondiente a ese número de mes
            print("Month name found for month number ", month_number, "is ", month_name)
            return month_name  # Regresamos el nombre del mes correspondiente

        return "Otro"  # Si el número de mes no está en el diccionario (porque la fecha esté mal), regresamos "Otro" para el nombre del mes

class Data_processing:

    def process_input_data(self, input_lines):
        total_per_month = {}
        total_per_month_per_country = {}

        for line in input_lines:  # Procesamos cada línea individualmente

            convertidores = Statistics()

            fields = line.split(",")  # Separamos la línea para obtener una lista con cada uno de los campos
            plate = fields[0]  # Obtenemos la matrícula del vuelo del campo 0
            departure_date = fields[1]  # Obtenemos la fecha de salida del campo 1
            country = convertidores.convert_plate_to_country(plate)  # Convertimos la matrícula en el país correspondiente utilizando la función creada arriba
            month = convertidores.convert_date_to_month(departure_date)  # Convertimos la fecha de llegada en el nombre del mes correspondiente utilizando la otra función creada arriba

            # Agregamos el vuelo al total por mes
            if month not in total_per_month.keys():  # Revisamos si el mes actual del vuelo no se encuentra en el diccionario
                total_per_month[month] = 1  # Si el mes NO se encuentra, entonces lo agregamos y le asignamos el valor 1, pues es la primera entrada
            else:
                total_per_month[month] += 1  # Si el mes YA se encuentra en el total por mes, se le agrega 1 a la cuenta que ya se tenía

            # Agregamos el vuelo al total por mes y por pais
            if month not in total_per_month_per_country.keys():  # Revisamos si el mes actual del vuelo NO se encuentra en el total por mes por país
                total_per_month_per_country[month] = {country: 1}  # Si no se encuentra el mes actual, lo agregamos como llave, y al país actual que tampoco se encontraba en ese mes le agregamos 1 por ser el primer registro de ese mes en ese país
            else:  # Si el mes ua está en el total de mes y país
                if country not in total_per_month_per_country[month]:  # Revisamos si el país del vuelo actual NO está en el registro del mes actual
                    total_per_month_per_country[month][country] = 1  # Si el país no está en el mes actual, lo agregamos con un conteo de 1 por ser el primer registro
                else:  # Si el país ya está en el mes actual
                    total_per_month_per_country[month][country] += 1  # Le sumamos uno al país del mes actual

        return total_per_month, total_per_month_per_country  # Regresamos el total por mes, y el total por mes y por país

    def compute_percentages(self, total_per_month, total_per_month_per_country):
        percentages = {}  # Creamos un diccionari en el que guadaremos los porcentajes que queremos imprimir separados por mes y país

        for month in total_per_month_per_country:  # Recorremos todos los meses del total por més y por paíes, pues es el que nos interesa
            percentages[month] = {}  # Cada vez que avanzamos de mes, creamos para cada mes un diccionario nuevo en el que se guardarán cada uno de los países para ese mes
            for country in total_per_month_per_country[month]:  # Recorremos todos los países de cada mes
                percentage = total_per_month_per_country[month][country] / total_per_month[month]*100 # Calculamos el porcentaje de vuelos por mes y por país dividiendo el total de vuelos de ése país en ese mes, entre el total de vuelos que hubo ese mes.
                if percentage >= 20:  # Revisamos si el porcentaje es mayor o igual a 20
                    percentages[month][country] = percentage  # De ser mayor o igual a 20 entonces lo guardamos en el dicionario de porcentajes, dentro del mes y el país correspondiente
        return percentages  # Una vez calculados y filtrados los porcentajes regresamos el diccionario con los resultados


class Results:

    def write_results(self, percentages):
        results_file = open("resultados.csv", "w+")  # Creamos y abrimos el archivo de resultados
        results_file.write("Mes, País, %% de vuelos\n")  # Escribimos los encabezados del archivo
        for month in percentages:  # Recorremos cada mes del diccionario de porcentajes
            for country in percentages[month]:  # Recorremos cada país dentro de cada mes
                line = month+", "+country+", "+str(percentages[month][country])+"\n"  # Generamos un string con los datos del mes, el país y el porcentaje
                results_file.write(line)  # Escribimos el string generado como una línea en el archivo
        results_file.close()  # Cerramos el archivo


if __name__ == "__main__":

    #Objetos asignados a variables

    my_statistics = Statistics()
    my_data = Data_processing()
    my_result = Results()


    #Metodos de clases para ejecutar el programa

    input_data = my_statistics.read_input_file()

    total_per_month, total_per_month_per_country = my_data.process_input_data(input_data)

    percentages = my_data.compute_percentages(total_per_month, total_per_month_per_country)

    results = my_result.write_results(percentages)

    print("-"*60)
    print("Programa ejecutado exitosamente!")
    print("-"*60)



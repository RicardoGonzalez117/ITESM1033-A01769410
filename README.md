# **Tarea 2**

## Descripcion del Problema

En la tarea 1 ayudaste a un aeropuerto en México a implementar una política de asignación de pistas con base en información histórica. En esta tarea ayudaras al mismo aeropuerto a mejorar su sistema de captura de información. Para ello debes primero entender mejor los componentes y el funcionamiento de aeropuerto a través de un diagrama de clases.
Cada vuelo tiene un identificador único que se genera a partir de las iniciales de la aerolínea y un número secuencial, por ejemplo, BA123. Así mismo tiene una fecha y hora de salida y de llegada, tal como se especificó en la tarea 1 (AAMMDD_HHMM_TZ).
Existen dos tipos de vuelos en el aeropuerto: locales e internacionales. Los primeros ocurren entre destinos nacionales, y los segundos hacia el extranjero. Además, cada vuelo es operado por una aerolínea principal, y puede tener otras aerolíneas asociadas. Cada vuelo puede tener los siguientes estados: estacionado, abordando, abordado, en tránsito y arribado. Cada vuelo despega de y aterriza en una puerta y una pista en específico. Las puertas se identifican por una combinación de letras y números, por ejemplo, A1, B21, etc. Las pistas se identifican por un número ordinal: 1, 2, etc.
Así mismo, cada vuelo tiene asociado un avión que se identifica por su matrícula (ver tarea 1 para ejemplos de matrícula). Además, de cada avión se registra su fabricante (Boeing, Airbus, etc.), el número de modelo (787, a380, etc.) [1], su capacidad en pasajeros (número de pasajeros), capacidad de equipaje en kilos y su velocidad máxima en km/h. Un mismo avión puede asociarse con dos o más vuelos diferentes, siempre y cuando los tiempos de salida y llegada de cada vuelo no se empalmen.
Cada vuelo es responsabilidad de un piloto, un copiloto y de 3 a 20 asistentes de vuelo, dependiendo el tamaño del avión. Tanto los pasajeros como los pilotos y asistentes de vuelo se identifican por su número de pasaporte. Adicionalmente se mantiene un registro de su nombre, su apellido, su fecha y país de nacimiento, su género, y su estado civil.
Para cada vuelo, los pasajeros pueden pertenecer a la clase turista, la clase ejecutiva o a la clase preferente. Cada pasajero se rastrea dentro del aeropuerto en diferentes puntos. El primer punto es el de registro, el cual no es obligatorio para pasajeros que no documentan equipaje, y que realizaron su registro en línea. El siguiente punto es seguridad, mismo que es obligatorio para todos los pasajeros. Y el último punto es abordaje, el cual se cumple cuando el pasajero se encuentra a bordo del avión.
El aeropuerto mantiene un reporte en tiempo real del estado de cada pista, y el conteo de pasajeros por cada punto de control. Así mismo mantiene un conteo de aviones, pasajeros, pilotos y asistentes en el aeropuerto en cada instante.

## Especificacion Tecnica

1. Utiliza Lucidchart para crear un nuevo diagrama de clases que modele los elementos del problema del aeropuerto descrito anteriormente.

2. Genera un PNG de tu diagrama de clases con el nombre diagrama.png

3. Utiliza la funcionalidad de Lucidchart para exportar tu diagrama de clases a un CSV con el nombre datos_diagrama.csv

ESTADO: --Completada--

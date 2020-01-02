# **Tarea 1**

## Descripcion del Problema

Un aeropuerto en México desea implementar una nueva y simplificada política de asignación de pistas basada en la frecuencia y el país de origen de los vuelos que aterrizan en el aeropuerto. El aeropuerto ha identificado cada país de origen con base en el prefijo de la matrícula de los aviones.

El problema consiste en determinar cuáles son los países con los que se tiene mayor contacto. Para ello se deben identificar desde el log de vuelos del año anterior los países desde los cuales provengan al menos el 20% de los vuelos de cada mes.

## Especificacion Tecnica

1. Lee el archivo de logs de vuelos denominado datos_vuelos.csv

2. Las fechas de salida y llegada tienen el formato AAMMDD_HHMM_TZ donde AA representa los dos dígitos del año, MM dos dígitos del mes, DD dos dígitos del día, HH dos dígitos de la hora en formato de 24 horas, MM dos dígitos para los minutos, y TZ el código de la zona horaria.

3. Con base en estos datos deberás calcular por cada mes del año anterior cuáles son los países que tengan 20% o más de los vuelos.

4.  Deberás escribir tus resultados en un archivo CSV denominado resultados.csv que contenga el mes, el país de origen y el porcentaje de vuelos.

ESTADO: --Completada--
#Ricardo Adolfo Gonzalez Terán
#ITESM Campus Toluca
#A01769410

#-*- coding:utf-8 -*-
import csv
import time

#Matriculas
#Alemania			D
#Brasil				PP
#Canada				CF
#Catar				A7
#Chile				CC
#China				B
#Dinamarca			OY
#Ecuador			HC
#Emiratos Arabes	A6
#España 			EC
#USA				N
#Indonesia			PK
#Japon				JA
#Mexico				XA
#Singapur			9V
#Tailandia			HS





print("-"*70)
print("Creando Diccionario...")
print("-"*70)
print("\n")
time.sleep(1)
print("-"*70)
print("Abriendo archivo...")
print("-"*70)
print("\n")
time.sleep(1)
dic_datos={}
total={}
file=open("datos_vuelos.csv","r+")
st=file.readlines()
st.pop(0)
print("-"*70)
print("Analizando lineas...")
print("-"*70)
print("\n")
time.sleep(1)
print("-"*70)
print("Creando lista...")
print("-"*70)
print("\n")
time.sleep(1)

for x in st:

    datos=x.split(",")
    flights=datos[0]
    months=datos[2].replace("{"," ")
    months=str(months[3:5])
    if months not in total:
    	total[months]=1
    	dic_datos[months]={}
    else :
    	total[months]+=1
    if flights not in dic_datos[months].keys():
    	dic_datos[months][flights]=1
    elif flights in dic_datos[months].keys():
        dic_datos[months][flights]+=1

file.close()

print("-"*70)
print("Calculando porcentajes...")
print("-"*70)
print("\n")
time.sleep(1)

percentages={}

print("-"*70)
print("Creando archivo con los resultados...")
print("-"*70)
print("\n")
time.sleep(1)
file=open("resultados.csv","w+")
file.write("Mes,País,Porcentaje de Vuelos\n")
print("-"*70)
print("Actualizando Porcentajes...")
print("-"*70)
print("\n")
time.sleep(1)
for months in dic_datos.keys():
	percentages[months]={}
	for flights in dic_datos[months].keys():
		average=round((((dic_datos[months][flights])/total[months])*100),2)
		if average>=20:
			percentages[months][flights]=average
		elif average<20:
			percentages[months][flights]="Sin información suficientes_0"
		file.write(months)
		file.write(",")
		file.write(flights)
		file.write(",")
		file.write(str(percentages[months][flights])+"%")
		file.write("\n")
file.close()

print("-"*70)
print("Matriculas de los paises (Solo los 2 primeros carateres)\n\r")

print("Matriculas")
print("Alemania---------------->  D")
print("Brasil------------------>  PP")
print("Canada------------------>  CF")
print("Catar------------------->  A7")
print("Chile------------------->  CC")
print("China------------------->  B")
print("Dinamarca--------------->  OY")
print("Ecuador----------------->  HC")
print("Emiratos Arabes--------->  A6")
print("España------------------>  EC")
print("USA--------------------->  N")
print("Indonesia--------------->  PK")
print("Japon------------------->  JA")
print("Mexico------------------>  XA")
print("Singapur---------------->  9V")
print("Tailandia--------------->  HS")
print("-"*70)

print("\n")
print("-"*70)
print("✅COMPLETADO...\nPara visualizar los resultados abra el archivo \"resultados.csv\"")
print("-"*70)
print("\n")


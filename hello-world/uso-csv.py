# Usar la biblioteca integrada 'csv'


# Aqui un ejemplo de como leer un archivo CSV y mostrar su contenido

import csv 
with open('archivo.csv', newline='' ) as archivo:
    lector_csv = csv.reader(archivo, delimiter=',')
    for fila in lector_csv:
        print(fila)
        
# En este ejemplo, archivo.csv es el nombre del archivo CSV que deseas leer.
# newline='' se utiliza para que no se interpreten las líneas en blanco dentro del archivo.



# El csv.reader() es un objeto que permite leer el archivo CSV y 
# divide cada fila en una lista de valores separados por comas, que se imprimen en el bucle for.


# Para escrinir en un archivo CSV, podemos usar 'csv.writer()' de la siguiente manera:

import csv 

with open ('archivo.csv', 'w', newline='') as archivo:
    escritor_csv = csv.writer(archivo, delimiter='')
    escritor_csv = csv.writerow(['Nombre', 'Edad', 'Sexo'])
    escritor_csv = csv.writerow(['Juan', '25', 'M'])
    escritor_csv = csv.writerow(['Maria', '32', 'F'])
   
#  En este ejemplo, archivo.csv es el nombre del archivo CSV que deseas escribir. w indica que deseas escribir en el archivo. 
# csv.writer() es un objeto que te permite escribir en el archivo CSV y writerow() es un método que te permite escribir una fila en el archivo.


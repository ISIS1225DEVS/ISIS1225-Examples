import csv
import sys

# Agregar la siguiente linea si aparece el siguiente error:
# _csv.Error: field larger than field limit (131072)
csv.field_size_limit(sys.maxsize)


archivo = './Data/ejemplo.csv'
reader = csv.DictReader(open(archivo, encoding='utf-8'), delimiter=",")
for e in reader:
    print(e)    # e es un diccionario con una linea del archivo


print()


reader = csv.reader(open(archivo, encoding='utf-8'), delimiter=",")
for e in reader:
    print(e)    # e es un tupla (,,) con cada linea del archivo


# Doc:
# https://docs.python.org/3/library/csv.html
#https://docs.python.org/3/library/csv.html
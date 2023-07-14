# leer un archivo json para recuperar la estrutura de datos lista

import json

with open("archivos/dicicionario.json", "r") as archivo:
     
     lista= json.load(archivo)

if not archivo.closed:
    print("cerrado archivo")
    archivo.close()

for elem in  lista:
    print(elem,end = )
import json

lista=[10,20,30,40,60]

whit open ("archivos/dicicionario.json","w") as archivo:
    json.dump(lista,archivo)
    print("se ha escrito en disco")

if not archivo.closed:
    print("cerrado archivo")
    archivo.close()

print("se hga cerrado el archivo")
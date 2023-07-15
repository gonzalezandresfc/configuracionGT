import json
def menu()
    
    
def estudiantes():
    pass
def notas ():
    pass
def reportes ():
    pass

def cargarInfo(ruta,dic):
    fd = open(ruta,"a+")
    fd.seek(0)
    # verificar si tiene datos
    try:
        json.load(fd,dic)
    except Exception as e:
        dic = {}
    fd.close()
    print(dic)

# programa principal

ruta = "archivos/institucionacme.json"
dicdata = {}
cargarInfo(ruta,dicdata)
while True:
    op= menu()
    if op == 1:
    estudiantes(ruta)
    elif op == 2:
        notas(ruta)
    elif op== 3
        

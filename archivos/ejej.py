
import json
nominacme = {}
agregarempleado = {}
# PROGRAMA GENERAL


def leerInt(msg):
    while True:
        try:
            n = int(input(msg))
            if n < 1:
                print("Error! El codigo debe ser entero postivo.")
                input("Digite cualquier tecla para continuar...")
                continue
            return n
        except ValueError:
            print("Error! Ingrese un numero valido")


def msgError(msg):
    print("----> ¡ERROR!" + msg)
    input("---> Presione ENTER para continuar")

# MENU ELEGIR PROGRANA


def menu():
    print("\n---------------")
    print(" NOMINA ACME MENU: ")
    print("----------------\n")
    print("1.Agregar empleado ")
    print("2.Modificar empleado ")
    print("3.Buscar empleado ")
    print("4.Eliminar empleado ")
    print("5.Listar empleados ")
    print("6.Listar nomina de un empleado ")
    print("7.Listar nomina de todos los empleados")
    print("8.Salir ")
    print(">> Escoja una opcion (1-8)?")
    elegirop = leerInt("\n>> Opcion (1 a 8)? ")
    if elegirop < 1 or elegirop > 8:
        msgError("Ingrese una opcion valida")
    return elegirop


def leerDatos(ruta):
    Agregar_empleado={}
    with open(ruta, "r")as f:
        datafile= json.load(f)
    print(datafile)
    for x in datafile.keys():
        id = int(datafile[x])
        nombre = datafile[id]["NOMBRE"]
        horas = datafile[id]["HORAS"]
        valorhora = datafile[id]["VALORHORA"]
        agregarempleado [id] ={}
        agregarempleado [id]= ["NOMBRE"]=nombre
        agregarempleado [id]= ["HORAS"]= horas
        agregarempleado [id]= ["VALORHORA"]= valorhora.strip()
    return Agregar_empleado

def actuaizarDatos(agregar_empleado):
    with open(ruta, "w")as f:
        json.dump(agregar_empleado,f)


    id = input("Ingrese el id del empleado: ")
    nominacme[id] = {}
    print(f"Id empleado: {id}")

    nombre = input("Ingrese el nombre de empleado: ")
    nominacme[id]["nombre"] = nombre
    print(f"Nombre empleado: {nombre}")

    horas = int(input("Ingrese horas trabajadas: "))
    nominacme[id]["Horas trabajadas"] = horas
    while True:
        if horas < 1 or horas > 160:
            print("Ingrese una hora valida")
            return horas
        else:
            break
    print(f"Horas trabajadas: {horas}")

    while True:
        valorhora = int(input("Ingrese el valor de la hora trabajada: "))

        if valorhora < 8000 or valorhora > 150000:
            print("Ingrese un valor de hora adecuado")

        else:
            nominacme[id]["Valor hora"] = valorhora
            break
    print(f"Valor horas trabajadas {valorhora}")
    print("LOS VALORES DEL NUEVO EMPLEADO SON: ")
    nominacme.items()
    # print(nominacme)

    # Guardar en el disco
    lstempl = [id, nombre, str(horas), str(valorhora)]
    strempl = "\n" + ";".join(lstempl)
    fd = open(ruta, "a+")
    fd.write(strempl)
    fd.close()

    input("---> Presione ENTER para continuar")


def escribirMemDisco(ruta, dicempl):
    fd = open(ruta, "w")
    fd.write("ID;NOMBRE;HORASTRAB;VALHORA")

    for id in dicempl.keys():
        nombre = dicempl[id]["nombre"]
        horastrab = dicempl[id]["Horas trabajadas"]
        valhora = dicempl[id]["Valor hora"]

        lstempl = [id, nombre, str(horastrab), str(valhora)]
        strempl = "\n" + ";".join(lstempl)
        fd.write(strempl)

    fd.close()



def Modificar_empleado(ruta):
    print("Modificar empleado: ")
    print("----Seleccione el numero de lo que quiere modificar---- ")
    print("\n 1.Modificar nombre \n 2.Modificar horas \n 3.Modicar valor hora")

    while True:
        buscarid = input("Ingrese el id del empleado que desea modificar: ")
        if buscarid in nominacme:
            print("ID ENCONTRADO")
            modificar = int(input("Ingrese un numero: "))
            if modificar == 1:
                nombrenuevo = input("Ingrese el nuevo nombre: ")
                nominacme[buscarid]["nombre"] = nombrenuevo
                break
            elif modificar == 2:
                nuevahora = int(input("Ingrese las nuevas horas trabajadas: "))
                nominacme[buscarid]["Horas trabajadas"] = nuevahora
                break
            elif modificar == 3:
                nuevovalorh = int(input("Ingrese nuevo valor trabajadas: "))
                nominacme[buscarid]["Valor hora"] = nuevovalorh
                break
            else:
                print("Ingrese un numero valido")
        else:
            ("ID NO ENCONTRADO")

    # Modificar el archivo
    escribirMemDisco(ruta, nominacme)
    input("---> Presione ENTER para continuar")


def Buscar_empleado():
    while True:
        buscarid = input("Ingrese el id del empleado que desea modificar: ")
        if buscarid in nominacme:
            print("ID ENCONTRADO")
            nombre = nominacme[buscarid]["nombre"]
            htrabjadas = nominacme[buscarid]["Horas trabajadas"]
            vlhora = nominacme[buscarid]["Valor hora"]

            print("-----EMPLEADO----")
            print("Los datos del empleado son: ")
            print(f"ID empleado: {buscarid}")
            print(f"Nombre empleado: {nombre}")
            print(f"Horas trabajadas: {htrabjadas}")
            print(f"Valor hora: {vlhora}")
            print(nominacme)
            break
        else:
            ("Empleado no encontrado")
    input("---> Presione ENTER para continuar")


def Eliminar_empleado(ruta):

    while True:
        buscarid = input("Ingrese el id del empleado que desea eliminar : ")
        if buscarid in nominacme:
            nominacme.pop(buscarid)
            print(f"ID ELIMINADO,se elimino el id : {buscarid}")
            break
        print("El id ingresado no existe ingrese de nuevo ")

    escribirMemDisco(ruta, nominacme)
    input("---> Presione ENTER para continuar")

def Listar_empleados():

    contador = 4
    indicador = 0
    for empleado in nominacme.keys():
        print("#"*40)
        print("LISTA EMPLEADOS ")
        print("#"*40)

        idencontrado = empleado
        nombre = nominacme[empleado]["nombre"]
        htrabjadas = nominacme[empleado]["Horas trabajadas"]
        vlhora = nominacme[empleado]["Valor hora"]

        print("-----EMPLEADO----")
        print("Los datos del empleado son: ")
        print(f"ID empleado: {idencontrado}")
        print(f"Nombre empleado: {nombre}")
        print(f"Horas trabajadas: {htrabjadas}")
        print(f"Valor hora: {vlhora}")
        print(nominacme)

        if indicador == contador:
            print("Quieres ver otros 5 empleados? ")
            print("Presiona 1 si deseas continuar o Presiona 2 si deseas salir")
            opcion = int(input("OPCION: "))
            if opcion == 1:
                contador += 5
                continue
            elif opcion == 2:
                break
        indicador += 1
    input("---> Presione ENTER para continuar")


def nómina_empleado():

    while True:
        buscarid = input("Ingrese el id del empleado que desea modificar: ")
        if buscarid in nominacme:
            print("ID ENCONTRADO")
            break
        else:
            print("ID NO ENCONTRADO")

    sueldobruto = nominacme[buscarid]["Horas trabajadas"] * \
        nominacme[buscarid]["Valor hora"]
    eps = sueldobruto * 0.04
    pension = sueldobruto * 0.04
    descuento = (eps + pension)
    auxilio = 0
    nombre = nominacme[buscarid]["nombre"]
    if sueldobruto <= 1160000:
        print("Merecedor subsidio de transporte")
        auxilio = 140606
    sueldoneto = (sueldobruto + auxilio) - descuento
    print(f"La nomina del empleado {nombre}")
    print(f"Sueldo bruto: {sueldobruto}")
    print(f"Valor eps: {eps}")
    print(f"Valor pension: {pension}")
    print(f"Valor auxilio: {auxilio}")
    print(f"Sueldo neto: {sueldoneto}")
    input("---> Presione ENTER para continuar")


def nómina_todos():
    contador = 4
    indicador = 0
    for empleado in nominacme.keys():
        print("#"*40)
        print("NOMINAS EMPLEADOS ")
        print("#"*40)

        sueldobruto = nominacme[empleado]["Horas trabajadas"] * \
            nominacme[empleado]["Valor hora"]
        eps = sueldobruto * 0.04
        pension = sueldobruto * 0.04
        descuento = (eps + pension)
        auxilio = 0
        nombre = nominacme[empleado]["nombre"]
        if sueldobruto <= 1160000:
            print("Merecedor subsidio de transporte")
            auxilio = 140606
        sueldoneto = (sueldobruto + auxilio) - descuento
        print(f"La nomina del empleado {nombre}")
        print(f"Sueldo bruto: {sueldobruto}")
        print(f"Valor eps: {eps}")
        print(f"Valor pension: {pension}")
        print(f"Valor auxilio: {auxilio}")
        print(f"Sueldo neto: {sueldoneto}")

        if indicador == contador:
            print("Quieres ver otros 5 empleados? ")
            print("Presiona 1 si deseas continuar o Presiona 2 si deseas salir")
            opcion = int(input("OPCION: "))
            if opcion == 1:
                contador += 5
                continue
            elif opcion == 2:
        agregarempleado [id]= ["NOMBRE


def cargarArch(ruta):
    fd = open(ruta, "a+")

    cont = 0
    dicempl = {}
    fd.seek(0)
    for linea in fd:
        cont += 1
        if cont > 1:
            lin = linea.rstrip()
        agregarempleado [id]= ["NOMBRE
    fd.close()

    if cont < 2:
        dicempl = {}

    return dicempl


# Validacion menu:
ruta = "texto.json"
while True:
    nominacme = cargarArch(ruta)

    elegirop = menu()

    if elegirop == 1:
        Agregar_empleado(ruta)
    elif elegirop == 2:
        Modificar_empleado(ruta)
    elif elegirop == 3:
        Buscar_empleado()
    elif elegirop == 4:
        Eliminar_empleado(ruta)
    elif elegirop == 5:
        Listar_empleados()
    elif elegirop == 6:
        nómina_empleado()
    elif elegirop == 7:
        nómina_todos()
    elif elegirop == 8:
        print("Se ha cerrado el programa")
        break

# print(nominacme)

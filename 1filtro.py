import json

def verifyInt(message, idd, codigoV):
    print("\n","-" *60)
    while True:
        try:
            if codigoV:
                print("Numero valido de  100 a 999")
                number = float(input(message))
                if number < 0 or number > 100.0:
                    print("Digita un numero valido")
                    continue
                return number
            
            if idd:
                number = int(input(message))
                if number < 11 or number > 13:
                    print("Digita una ID valida, maximo 13 diguitos")
                    continue
                return number
            
            
        except ValueError:
            print("Error, no ingreses letras ni caracteres especiales")

def verifyString(message):
    print("\n","-" *60)
    while True:
        letter = input(message)
        if letter.strip() == "" or not(letter.isalpha()):
            print("No ingreses caracteres especiales ni espacios vacios")
            continue
        else:
            return letter
    

def options():
    while True:
        try:
            option = int(input("Opcion: "))
            if option < 1 or option > 6:
                print("Ingresa una opcion valida")
                continue
            break
        except ValueError:
            print("Ingresa un numero valido")
    return option

def informacioCl():
    cliente = int (input("ingrese el nombre de el cliente"))
    id = int(input("Digite la cedula del cliente: "))
    Número = int (input("ingrese un numero de celular"))
    Sexo = input("ingrese su sexo")
    cliente[id] = {}
    cliente[id]["cl"] = cliente
    cliente[id]["id"] = id
    cliente[id]["numero"] = Número
    cliente[id]["sexo"] = Sexo

def añadircliente(clientes):
    print("\n","-" *60)
    print("INGRESAR CLIENTES".center(50,"-"))
    while True:
        id = verifyInt("Ingrese el id del cliente: ", False, False)
        if not(id in clientes):
            clientes[id] = {}
        else:
            print(f"Se han encontrado {len(clientes[id])} el cliente {id}")
        while True:
            unique = True
            while True:
                idd = verifyInt("Ingrese el id del cliente: ", True, False)
                for x in clientes:
                    if idd in clientes[x]:
                        print("Ya existe un usuario con el mismo codigo, verificacion")
                        unique = False
                        break
                if unique:
                    break
            clientes[id][idd] = {}
            name = verifyString("Digite el nombre del cliente: ")
            print("\nSexo del cliente (M = Masculino) (F = Femenino)")
            while True:
                sex = verifyString("Ingresa: ")
                if sex.upper() == "M" or sex.upper() == "F":
                    break
                else:
                    print("Ingresa solamente M o F")
            clientes[id][idd]["Name"] = name.title()
            clientes[id][idd]["Sex"] = sex.upper()
            print(f"La informacion del estudiante {name} se ha guardado")
            print("-" *60)
            print("\nQuieres ingresar otro estudiante? ")
            print("1. Si\n2. No")
            option = options(2)
            if option == 2:
                break
        print("-" *60)
        print("\nQuieres ingresar otro cliente ? ")
        print("1. Si\n2. No")
        option = options(2)
        
def informacioCl(clientes):
    try:
        with open(rute_clientes, "r") as f:
            data_file = json.load(f)
            for x in data_file.keys():
                clientes[int(x)] = {}
                for y in data_file[x].keys():
                    clientes[int(x)][int(y)] = data_file[x][y]
        return clientes
    except:
        with open(rute_clientes, "w") as f:
            json.dump(clientes, f)
            return clientes

def modificar(clientes):
    print("\n","-" *60)
    print("MODIFICAR DATOS DE TARJETA".center(50,"-"))
    while True:
        id = verifyInt("Ingrese el id cliente: ", False, False)
        if not(id in clientes):
            print(f"No existe un grado {id}, verifica")
            continue
        break

    while True:
        idd = verifyInt("Ingrese el codigo del cliente: ", True, False)
        if not(idd in clientes[id]):
            print("No existe un estudiante con ese codigo, verifica")
            continue
        break
    name = (clientes[id][idd]["Name"])
    print(f"\nQue datos quieres modificar del  {name}?")
    print("1. Nombre")
    print("2. id")
    print("3. Sexo")
     

def search_id(clientes):
    found = False
    while True:
        id = verifyInt("Digita el codigo del estudiante: ", True, False, False)
        for x in clientes.keys():
            if id in clientes[x]:
                id = x
                found = True
        if found:
            break
        else:
            print("Codigo no encontrado, valida de nuevo.")
    return id, id


def eliminar ():
    clientes = informacioCl()
    print("\n","-" *60)
    print("ELIMINAR ESTUDIANTE".center(50,"-"))
    (id, id) = search_id(clientes) 
    name = clientes[id][id]["Name"]
    del clientes[id][id]
    print(f"Los datos de {name} fueron eliminados correctamente")
    input("\nPresione cualquier tecla para volver al menu")

def Reportes():
    informacioCl()
    print("Instituto Academico ACME".center(50,"="))
    print("Promedio de notas por grado".center(50,"-"))
    clientes = informacioCl()
##MENU##
while True:
            print("TARJETAS CREDITO ACME".center(50,"="))
            print("Administracion tarjetas".center(50,"-"))
            print("\n1. informacion del cliente")
            print("2.añadir ")
            print("3.modificar")
            print("4.eliminar")
            print("5.hacer reportes")
            print("6.salir")
            opcion = 6
            if opcion == 1:
                informacioCl()
            elif opcion == 2:
                añadircliente()      
            elif opcion == 3:
                modificar()
            elif opcion == 4:
                eliminar()
                pass
            elif opcion == 5:
                Reportes()
            else:
                break

rute_clientes = "PV_MicroAcme/trajetas.json"

import json

def cargar_productos():
    try:
        with open('archivos/micromercado.json', 'rb') as file:
            productos = json.load(file)
    except FileNotFoundError:
        productos = {}
        return productos
    

def guardar_productos(productos):
    with open('archivos/micromercado.json', 'wb') as file:
        json.dump(productos, file)

def cargar_clientes():
    try:
        with open('archivos/micromercado.json', 'rb') as file:
            clientes = json.load(file)
    except FileNotFoundError:
        clientes = {}
    return clientes

def guardar_clientes(clientes):
    with open('clientes.dat', 'wb') as file:
        json.dump(clientes, file)

def agregar_producto(productos, codigo, valor_unitario, tipo_iva):
    productos[codigo] = (valor_unitario, tipo_iva)
    guardar_productos(productos)

def procesar_compra(productos, clientes, cliente):
    compra_iva = 0
    compra_total = 0
    compras_cliente = []

    while True:
        codigo = input("Ingrese el código del producto (0 para terminar la compra): ")
        if codigo == '0':
            break

        if codigo in productos:
            valor_unitario, tipo_iva = productos[codigo]
            cantidad = int(input("Ingrese la cantidad comprada: "))
            valor_producto = valor_unitario * cantidad

            if tipo_iva == 2:
                iva = valor_producto * 0.05
            elif tipo_iva == 3:
                iva = valor_producto * 0.19
            else:
                iva = 0

            compra_iva += iva
            compra_total += valor_producto + iva

            compras_cliente.append((codigo, valor_unitario, cantidad, iva))
        else:
            print("El código del producto no existe. Intente nuevamente.")

    clientes[cliente] = compras_cliente
    guardar_clientes(clientes)

    print("\nTirilla de pago:")
    print("Cliente:", cliente)
    print("")

    for compra in compras_cliente:
        codigo, valor_unitario, cantidad, iva = compra
        valor_producto = valor_unitario * cantidad

        print("Código:", codigo)
        print("Cantidad:", cantidad)
        print("Valor unitario:", valor_unitario)
        print("Valor producto:", valor_producto)
        print("IVA:", iva)
        print("Valor final:", valor_producto + iva)
        print("")

    print("Total venta:", compra_total)
    print("Total IVA:", compra_iva)
    print("\n")

def generar_informe_diario(clientes):
    total_ventas = 0
    total_iva = 0
    total_productos = 0
    total_valor_sin_iva = 0

    for compras_cliente in clientes.values():
        for compra in compras_cliente:
            _, valor_unitario, cantidad, iva = compra
            valor_producto = valor_unitario * cantidad

            total_productos += cantidad
            total_ventas += valor_producto + iva
            total_iva += iva
            total_valor_sin_iva += valor_producto

    print("Informe de ventas diarias:")
    print("Total ventas:", total_ventas)
    print("Total IVA:", total_iva)
    print("Cantidad de productos vendidos:", total_productos)
    print("Valor total sin IVA:", total_valor_sin_iva)
    print("Valor total con IVA:", total_ventas)

def ejecutar():
    productos = cargar_productos()
    clientes = cargar_clientes()

    while True:
        print("----- Menú Principal -----")
        print("1. Agregar producto")
        print("2. Procesar compra")
        print("3. Generar informe diario")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            codigo = input("Ingrese el código del producto: ")
            valor_unitario = float(input("Ingrese el valor unitario del producto: "))
            tipo_iva = int(input("Ingrese el tipo de IVA (1: Exento, 2: Bienes, 3: General): "))
            agregar_producto(productos, codigo, valor_unitario, tipo_iva)
        elif opcion == '2':
            cliente = input("Ingrese el nombre del cliente: ")
            procesar_compra(productos, clientes, cliente)
        elif opcion == '3':
            generar_informe_diario(clientes)
        elif opcion == '4':
            break
        else:
            print("Opción inválida. Intente nuevamente.")

    guardar_productos(productos)
    guardar_clientes(clientes)

if __name__ == '__main__':
    ejecutar()
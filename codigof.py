def menu():
    print("1. Registrarse")
    print("2. Acceder al sistema")
    print("3. Seleccionar proveedor")
    print("4. Asignar petición de proveedor de producto")
    print("5. Verificar si es producto nuevo")
    print("6. Salir")

def registrarse():
    usuario = input("Ingrese el nombre de usuario: ")
    contraseña = input("Ingrese la contraseña: ")

    #validar datos
    if len(usuario) < 5 or len(contraseña) < 5:
        print("Los datos ingresados no son validos. Intentelo de nuevo.")
    else:
        print("Correcto")

def acceder_sistema():
    print("Bienvenido al sistema de acceso.")
    usuario = input("Ingrese su usuario: ")
    codigo = input("Ingrese su codigo: ")

    if usuario == "usuario" and codigo == "1234":
        print("Acceso correcto.")
    else:
        print("Acceso incorrecto. Intente nuevamente.")

def seleccionar_proveedor():
    proveedores = ["A", "B", "C"]

    for i, proveedor in enumerate(proveedores):
        print(f"{i + 1}. {proveedor}")

    opcion = int(input("Seleccione un proveedor: "))
    return proveedores[opcion - 1]

def asignar_peticion_proveedor(proveedor, producto, precio, consciente, aprobado):
    peticion = {
        "proveedor": proveedor,
        "producto": producto,
        "precio": precio,
        "consciente": consciente,
        "aprobado": aprobado
    }

    print("Petición asignada correctamente.")
    print(peticion)

def es_producto_nuevo(producto):
    productos_existentes = ["Producto1", "Producto2", "Producto3"]
    return producto not in productos_existentes

opcion = 0
proveedor = None

while opcion != 6:
    menu()
    opcion = int(input("Ingrese el número de la opción deseada: "))

    if opcion == 1:
        registrarse()

    elif opcion == 2:
        acceder_sistema()

    elif opcion == 3:
        proveedor = seleccionar_proveedor()

    elif opcion == 4:
        producto = "Producto1"
        precio = 100
        consciente = True
        aprobado = False

        if es_producto_nuevo(producto):
            asignar_peticion_proveedor(proveedor, producto, precio, consciente, aprobado)
        else:
            print("El producto ya existe.")

    elif opcion == 5:
        producto = "Producto1"
        es_producto_nuevo(producto)

    elif opcion == 6:
        print("Saliendo del sistema...")
    else:
        print("Opción no válida. Intente de nuevo.")
        
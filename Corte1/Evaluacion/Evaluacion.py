# ==============================
# TUPLA (categorías fijas)
# ==============================

categorias = ("Gloss", "Matte", "Transparente", "Especial", "Industrial", "Seguridad")

# ==============================
# CATÁLOGO COMPLETO
# ==============================

catalogo = {
    "E001": {
        "nombre": "Premium Gloss",
        "material": "Vinilo blanco brillante",
        "beneficio": "Colores vibrantes",
        "caracteristica": "Alimentos y limpieza",
        "precio": 1200,
        "categoria": "Gloss"
    },
    "E002": {
        "nombre": "Elite Matte",
        "material": "Vinilo blanco mate",
        "beneficio": "Elegancia táctil",
        "caracteristica": "Cosméticos",
        "precio": 1400,
        "categoria": "Matte"
    },
    "E003": {
        "nombre": "Crystal Clear",
        "material": "Vinilo transparente",
        "beneficio": "Efecto directo",
        "caracteristica": "Vidrio",
        "precio": 1500,
        "categoria": "Transparente"
    },
    "E004": {
        "nombre": "Special Effects",
        "material": "Vinilo metálico",
        "beneficio": "Brillo llamativo",
        "caracteristica": "Stickers",
        "precio": 1800,
        "categoria": "Especial"
    },
    "E005": {
        "nombre": "Industrial Pro",
        "material": "Alta adherencia",
        "beneficio": "Resistente",
        "caracteristica": "Maquinaria",
        "precio": 2000,
        "categoria": "Industrial"
    },
    "E006": {
        "nombre": "Security Seal",
        "material": "Vinilo destructible",
        "beneficio": "No removible",
        "caracteristica": "Seguridad",
        "precio": 1700,
        "categoria": "Seguridad"
    }
}

inventario = []

# ==============================
# FUNCIONES
# ==============================

def agregar_producto():
    codigo = input("Ingrese código: ").upper()

    if codigo not in catalogo:
        print("Código no existe")
        return

    try:
        cantidad = int(input("Cantidad: "))
    except:
        print("Error en cantidad")
        return

    precio = catalogo[codigo]["precio"]
    total = precio * cantidad

    producto = {
        "codigo": codigo,
        "cantidad": cantidad,
        "total": total
    }

    inventario.append(producto)
    print("Producto agregado")


def mostrar_productos():
    print("\nInventario")

    for item in inventario:
        cod = item["codigo"]
        datos = catalogo[cod]

        print("\n----------------")
        print("Código:", cod)
        print("Nombre:", datos["nombre"])
        print("Categoría:", datos["categoria"])
        print("Material:", datos["material"])
        print("Beneficio:", datos["beneficio"])
        print("Característica:", datos["caracteristica"])
        print("Precio unitario:", datos["precio"])
        print("Cantidad:", item["cantidad"])
        print("TOTAL:", item["total"])


def buscar_producto():
    codigo = input("Código a buscar: ").upper()

    if codigo in catalogo:
        datos = catalogo[codigo]

        print("\nProducto encontrado:")
        print("Código:", codigo)
        print("Nombre:", datos["nombre"])
        print("Categoría:", datos["categoria"])
        print("Material:", datos["material"])
        print("Beneficio:", datos["beneficio"])
        print("Característica:", datos["caracteristica"])
        print("Precio:", datos["precio"])

        # verificar si está en inventario
        encontrado = False
        for item in inventario:
            if item["codigo"] == codigo:
                print("Cantidad en inventario:", item["cantidad"])
                print("Total acumulado:", item["total"])
                encontrado = True
                break

        if not encontrado:
            print("Este producto no ha sido agregado al inventario")

    else:
        print("Código no existe")


def eliminar_producto():
    codigo = input("Código a eliminar: ").upper()

    for item in inventario:
        if item["codigo"] == codigo:
            inventario.remove(item)
            print("Eliminado")
            return

    print("No encontrado en inventario")


def total_inventario():
    suma = 0

    for item in inventario:
        suma += item["total"]

    print("\nTOTAL GENERAL DEL INVENTARIO:", suma)


# ==============================
# MENÚ
# ==============================

while True:
    print("\n===== MENÚ =====")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Total de compra")
    print("6. Ver categorías")
    print("7. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_productos()
    elif opcion == "3":
        buscar_producto()
    elif opcion == "4":
        eliminar_producto()
    elif opcion == "5":
        total_inventario()
    elif opcion == "6":
        print("\nCategorías disponibles:", categorias)
    elif opcion == "7":
        break
    else:
        print("Opción inválida")

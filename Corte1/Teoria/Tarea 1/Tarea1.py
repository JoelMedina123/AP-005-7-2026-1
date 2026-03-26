#-------------------MANEJO DE LISTAS------------------
# Definir una lista inicial de 6 colores
colores = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde']
# Mostrar el contenido de la lista
print(colores)
# Verificar el tipo de dato de la variable
print(type(colores))
# Acceder al tercer elemento (índice 2)
print(colores[2])

# Obtener la cantidad total de elementos
print("Tamaño de la lista: ", len(colores))
# Extraer una sublista desde el índice 0 hasta el 1
print(colores[0:2])
# Atajo para obtener los primeros dos elementos
print(colores[:2])

# Insertar un color nuevo al final de la estructura
colores.append('Blanco')
# Mostrar cambios
print(colores)

# Ubicar el color 'Negro' específicamente en la cuarta posición
colores.insert(3, 'Negro')
# Mostrar cambios
print(colores)

# Unir una lista adicional a la que ya tenemos
colores.extend(['Marron', 'Gris'])
# Visualizar lista extendida
print(colores)

# Buscar en qué índice se encuentra el color 'Azul'
print(colores.index('Azul'))

# Borrar el elemento 'Marron' y ajustar índices automáticamente
colores.remove('Marron')
# Mostrar lista tras borrado
print(colores)

# Reinsertar el color eliminado en su posición original (índice 8)
colores.insert(8, 'Marron')
# Mostrar lista actualizada
print(colores)

# Quitar el último ítem y mostrar cuál fue el eliminado
print(colores.pop())
# Guardar la nueva longitud en una variable
largo = len(colores)
# Mostrar el conteo actual
print("largo = ", largo)
# Eliminar el elemento que quedó al final usando el índice dinámico
print(colores.pop(largo-1))

# Generar una lista repetida tres veces consecutivas
lista_triplicada = colores * 3
# Mostrar el resultado de la triplicación
print("lista_triplicada: ", lista_triplicada)

# Proceso de ordenamiento
print("Ordenando elementos:")
# Crear una copia ordenada alfabéticamente sin alterar la original
lista_ordenada = sorted(colores)
# Mostrar la nueva lista organizada
print(lista_ordenada, "\n")

# Crear lista numérica desordenada del 10 al 1
Numeros = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# Aviso de orden ascendente
print("Lista de menor a mayor: ")
# Aplicar ordenamiento ascendente directo sobre la lista
Numeros.sort()
# Mostrar lista numérica corregida
print(Numeros)

# Aplicar ordenamiento descendente (de mayor a menor)
Numeros.sort(reverse=True)
# Mostrar resultado final de números
print("Mayor a menor: ", Numeros, "\n")


#-------------------MANEJO DE TUPLAS------------------
# Las tuplas son colecciones que, a diferencia de las listas,
# son constantes y no permiten modificaciones tras su definición:

# Transformar la lista de colores en una estructura inmutable
print("############ SECCIÓN TUPLAS #########")
mi_tupla = tuple(colores)
print()
print()
# Visualizar la tupla creada
print("mi_tupla: ", mi_tupla)

# Consultar el primer valor de la tupla
print(mi_tupla[0])
# Consultar el tercer valor de la tupla
print(mi_tupla[2])

# Comprobar si 'Rojo' existe dentro de la tupla (True/False)
print('Rojo' in mi_tupla)
# Contar las ocurrencias del color 'Rojo'
print(mi_tupla.count('Rojo'))

# Declaración de una tupla de un único valor
tupla_simple = ('Blanco')
# Mostrar tupla unitaria
print(tupla_simple)

# Técnica de empaquetado: crear tupla omitiendo paréntesis
datos_persona = 'Gaspar', 5, 8, 1999
# Mostrar datos empaquetados
print(datos_persona)

# Técnica de desempaquetado: asignar valores a variables independientes
nom, d, m, a = datos_persona
# Mostrar cada variable por separado
print(nom)
print(d)
print(m)
print(a)

# Formatear la salida de los datos personales
print("Nombre: ", nom, " - Dia:", d, " - Mes: ", m, "- Año: ", a)

# Revertir la tupla a formato de lista para que sea editable de nuevo
lista_desde_tupla = list(datos_persona)
# Mostrar la lista resultante
print(lista_desde_tupla)

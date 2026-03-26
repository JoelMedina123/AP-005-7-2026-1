############### CREACIÓN DE DICCIONARIOS ###############

# Definimos un diccionario básico: llave:valor (como el sensor y su temperatura)
sensors = {"living room": 21, "kitchen": 23}
print(sensors)

# Un diccionario que sirve como traductor (palabra:traducción)
translations = {"mountain": "orod", "bread": "bass"}
print(translations)

# ¡OJO! Esto tira error: las llaves tienen que ser fijas (inmutables). 
# Las listas [] no sirven como llaves porque pueden cambiar.
# powers = {[1,2,3]: 2}

# Pero los valores sí pueden ser listas sin problema (ej: un apellido, varios hijos)
children = {"Corleone": ["Sonny","Fredo","Michael"]}
print(children)

# Crear un diccionario que nace sin nada (vacío)
my_empty_dictionary = {}
print(my_empty_dictionary)

# Para meter algo nuevo al menú, solo usamos la llave y le asignamos el precio
menu = {"oatmeal": 3, "toast": 6}
menu["cheesecake"] = 8
print(menu)

# Si la llave ya existe, simplemente le "caemos encima" al valor anterior
menu["oatmeal"] = 5
print(menu)

# Con .update() metemos varias cosas de un solo viaje
sensors.update({"pantry":22, "patio":34})
print(sensors)

############### DICT COMPREHENSION ###############

# Tenemos dos listas por separado: nombres y estaturas
names = ['Jenny', 'Alexus', 'Sam']
heights = [61, 70, 67]

# El truco pro: zip los junta como parejas y el 'for' arma el diccionario rápido
students = {k:v for k,v in zip(names, heights)}
print(students)

############### EJEMPLO MÁS COMPLETO ###############

# Lista de temas y cuántas veces los escuchamos
songs = ["Imagine","Respect","Satisfaction"]
playcounts = [44, 89, 29]

# Armamos el diccionario de reproducciones combinando las listas
plays = {k:v for k,v in zip(songs, playcounts)}
print(plays)

# Agregamos una canción nueva y actualizamos las reproducciones de otra
plays.update({"Purple Haze":1})
plays.update({"Respect":94}) 
print(plays)

# Diccionarios anidados: un diccionario que guarda otros diccionarios dentro
library = {
    "Best Songs": plays,
    "Chill": {}
}

print(library)

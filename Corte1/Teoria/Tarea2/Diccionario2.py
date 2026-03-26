############### DICCIONARIOS (OPERACIONES) ################

# Relación clave-valor (como un buscador: pones el nombre y te da el dato)
building_heights = {
    "Burj Khalifa": 828,
    "Shanghai Tower": 632,
    "Abraj Al Bait": 601,
    "Ping An": 599
}

# Accedemos directamente al valor usando su nombre (la clave)
print(building_heights["Burj Khalifa"])

# Las claves pueden guardar listas enteras como valores
zodiac_elements = {
    "water": ["Cancer", "Scorpio", "Pisces"],
    "fire": ["Aries", "Leo", "Sagittarius"]
}

# Me trae la lista completa asociada a "water"
print(zodiac_elements["water"])

# --- VALIDACIONES ---
# Antes de pedir un dato, mejor checar si existe para que no mande error
key_to_check = "Landmark 81"
if key_to_check in building_heights:
    print(building_heights[key_to_check])

# El método .get() es más seguro: si la clave no existe, te devuelve "None" en vez de romper el código
print(building_heights.get("Shanghai Tower"))
print(building_heights.get("My House")) # Aquí imprime None porque no está en el dict

# Ejemplo de uso de .get() para asignar valores por defecto
user_ids = {"teraCoder": 100019, "pythonGuy": 182921}

# Si no existe el usuario, le asignamos el ID 1000 manualmente
if user_ids.get("teraCoder") == None:
    tc_id = 1000
else:
    tc_id = user_ids.get("teraCoder")

print(tc_id)

# --- ELIMINAR ---
# .pop() saca el elemento y te dice qué había ahí. 
# Si no lo encuentra, devuelve el mensaje de "No Prize" (opcional)
raffle = {223842: "Teddy Bear", 872921: "Concert Tickets"}
print(raffle.pop(223842, "No Prize"))
print(raffle) # Ahora solo queda el ticket del concierto

# --- RECORRER (LOOPS) ---
test_scores = {"Grace":[80,72], "Jeffrey":[88,68]}

# Si solo me interesan los nombres (las claves)
for student in test_scores.keys():
    print(student)

# Si solo me interesan las notas (los valores)
for scores in test_scores.values():
    print(scores)

# El más útil: recorrer ambos al mismo tiempo con .items()
biggest_brands = {"Apple": 184, "Google": 141.7}
for company, value in biggest_brands.items():
    print(company, "vale", value, "billones")

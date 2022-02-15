#Ejercicio 1 Creacion de un bucle while
n_planet = ''
planets = []
# Escribe el ciclo while solicitado
while n_planet.lower() != 'hecho':
    if n_planet:
        planets.append(n_planet)
    n_planet = input('ingresa un nuevo pleneta ')

#Ejercicio 2 Creacion de un ciclo for
for planet in planets:
    print(planet)
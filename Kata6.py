#Ejercicio 1 crear y usar listas en python

planetas = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 
'Saturn', 'Uranus', 'Neptune']
print('There are', len(planetas), 'planets')
planetas.append('Pluto')
print(planetas[-1], 'is the last planet')

#Ejercicio 2 Trabajando con datos de una lista

planetas = ['Mercury', 'Venus', 'Earth',
 'Mars', 'Jupiter', 'Saturn', 'Neptun']
user_planet = input('por favor introduce el nombre del planeta (with a capital letter to start)')
planet_index = planetas.index(user_planet)
print('Here are the planets closer than ' + user_planet)
print(planetas[0:planet_index])
print('Here are the planets further than ' + user_planet)
print(planetas[planet_index + 1:])


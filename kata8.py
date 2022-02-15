#Ejercicio 1
# Crea un diccionario llamado planet con los datos propuestos
planet = {
    'name': 'Marte',
    'lunas': 2
}
print(f'{planet["name"]} has {planet["lunas"]} lunas')
planet['circumference (km)'] = {
    'polar': 6752,
    'equatorial': 6792}
print(f'{planet["name"]} tiene una circunferencia polar de {planet["circumference (km)"]["polar"]}')

#Ejercicio 2 realiza un codigo para determinar el numero de lunas
lunas = planet_moons.values()
planets = len(planet_moons.keys())
total_moons = 0
for moon in lunas:
    total_moons = total_moons + moon
    average = total_moons / planets
print(average)
#EJERCICIO 1 Utiliza operadores aritmeticos

# Crear variables para almacenar las dos distancias
# ¡Asegúrate de quitar las comas!
primP = 149597870
segP = 778547200
# Calcular la distancia entre planetas
distance_km = segP - primP
print(distance_km)
distance_mi = distance_km * 0.621
print(distance_mi)

#EJERCICIO 2 
# Almacenar las entradas del usuario
primP = input('Escriba la distancia del sol para el primer planeta en KM')
segP = input('Escriba la distancia desde el sol para el segundo planeta')
 #Convierte las cadenas de ambos planetas a números enteros
primP = int(primP)
segP = int(segP)
# Realizar el cálculo y determinar el valor absoluto
distance_km = segP - primP
print(distance_km)

# Convertir de KM a Millas
distance_mi = distance_km * 0.621
print(abs(distance_mi))

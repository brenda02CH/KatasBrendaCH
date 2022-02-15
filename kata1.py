from datetime import date

date.today()

# program.py
print('Hola desde la consola')


#FECHA DE HOY
print("La fecha de hoy es: " + str(date.today()))

#ENTRADA DE DATOS
print("Bienvenido al programa de bienvenida")
nombre = input("Ibntroduzca su nombre ")
print("Saludos: " + nombre)

#CONVERTIDOR DE UNIDADES
parsec = 11
lyears = 3.26156 * parsec

print(str(parsec) + " parsec, is " + str(lyears) + " lightyears")

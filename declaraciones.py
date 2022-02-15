#EJERCICIO 1

# Añadir el código necesario para crear una variable que guarde la velocidad del asteroide.
# Escribe una expresión de prueba para calcular si necesita una advertencia.
# Agregue las instrucciones que se ejecutarán si la expresión de prueba es true o false.

ast = 49
if ast > 25:
    print('¡El asteroide se acercara muy pronto!')
else:
    print('¡que tengas un día!')

#EJERCICIO 2
# Agrega el código para crear una variable para un asteroide que viaja a 19 km/s
# Escribe varias expresiones de prueba para determinar si puedes ver el rayo de luz desde la tierra
# Agrega las instrucciones que se ejecutarán si las expresiones de prueba son True o False

ast = 19
if ast > 20:
    print('Look up! ¡Hay una luz mágica en el cielo!')
elif ast == 20:
    print('Look up! ¡Hay una luz mágica en el cielo!')
else:
    print('¡Nada que ver aquí!')



#EJERCICIO 3
# Agrega el código para crear nuevas variables para la velocidad y el tamaño del asteroide
# Para probar el código, prueba con varias velocidades y tamaños
# Escribe varias expresiones de prueba o combinaciones de expresiones de prueba para determinar qué mensaje se debe enviar a Tierra.

velocidad_ast = 25
tamano_asteroide = 40
if velocidad_ast > 25 and tamano_asteroide > 25:
    print('¡Cuidado, Un asteroide muy peligroso viene hacia la Tierra!')
elif velocidad_ast >= 20:
    print('Mira! ¡Hay una luz mágica en el cielo!')
elif tamano_asteroide < 25:
    print('No hay nada que ver aquí :)')
else:
    print('No hay nada que ver aquí :)')


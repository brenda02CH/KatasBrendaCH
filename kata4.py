#Ejercicio 1: Transformar cadenas
text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth"""

# Divide el texto
text_parts = text.split('. ')
text_parts
# Palabras clave
key_words = ["average", "temperature", "distance"]
# Ciclo for para recorrer la cadena
for sentence in text_parts:
    for key_word in key_words:
        if key_word in sentence:
            print(sentence)
            break
# Ciclo para cambiar C a Celsius
for sentence in text_parts:
    for key_word in key_words:
        if key_word in sentence:
            print(sentence.replace(' C', ' Celsius'))
            break

#Ejercicio 2 Formateando Cadenas
# Datos con los que vamos a trabajar
# variables

planeta = 'Marte '
gravedad  = 0.00143
nombre = 'Ganímedes'
# Creamos el título
title = f'datos de gravedad de {nombre}'
# Creamos la plantilla
hechos = f"""{'-'*80} 
Nombre del planeta: {planeta} 
Gravedad en {nombre}: {gravedad * 1000} m/s2 
"""
# Unión de las cadenas
template = f"""{title.title()} 
{hechos} 
""" 
print(hechos)
# New datos
planeta = 'Marte '
gravedad  = 0.00143
nombre = 'Ganímedes'
print(hechos)
new_template = """
Datos de Gravedad sobre: {nombre}
-------------------------------------------------------------------------------
Nombre del planeta: {planeta}
Gravedad en {nombre}: {gravedad} m/s2
"""
print(new_template.format(nombre=nombre, planeta=planeta, gravedad=gravedad))
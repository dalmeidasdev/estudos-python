# Pintando parede
# Link do vídeo: https://youtu.be/mzSJpn9ldt4?si=4pFFalp6KqjTkmXq

import math 

a = float(input('Digite a altura da parede: '))
l = float(input('Digite a largura da parede: '))
area = a * l
lt = math.ceil(area / 2)

print(f'Para pintar uma parede de {area} metros quadrados serão necessários {lt} litros de tinta !')
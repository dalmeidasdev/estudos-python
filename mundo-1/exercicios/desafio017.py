# Catetos e hipotenusa
# Link da aula: https://youtu.be/vmPW9iWsYkY?si=4QRU4kPZ1DLCD7Fv
import math

o = float(input('Digite o comprimento do cateto oposto: '))
a = float(input('Digite o comprimento do cateto adajacente: '))
h = math.sqrt((o ** 2) + (a ** 2))
print(f'O valor da hipotenusa é {h}')
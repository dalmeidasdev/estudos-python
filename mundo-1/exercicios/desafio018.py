# Seno, cosseno e tangente
# Link do vídeo: https://youtu.be/9GvsphwW26k?si=pgbUKh82qTwNrqIj

import math

a = float(input('Digite um ângulo: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
tg = math.tan(math.radians(a))

print(f'O valor do seno, cosseno e tangente de {a} respectivamente é: {s:.2f}, {c:.2f}, {tg:.2f}')
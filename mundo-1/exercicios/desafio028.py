# Jogo da adivinhação
# Link do vídeo: https://youtu.be/kchC5KLZSZ4?si=lQNyGIHWazE43v2T

import random

n = random.randint(0, 5)
r = int(input('Digite um número inteiro entre 0 a 5: '))

if r == n:
    print('Parabéns, você acertou !')
else:
    print(f'Não foi dessa vez, o número era {n}')
print('Fim')
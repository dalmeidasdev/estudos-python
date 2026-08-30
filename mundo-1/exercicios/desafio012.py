# Calculando descontos
# Link do vídeo: https://youtu.be/4MAmKOT9FeU?si=0Z_IwqxrTwBKkoCe

pi = float(input('Digite o preço inicial: '))
d = (5/100) * pi
pf = pi - d

print(f'O valor final com 5% de desconto é R${pf:.2f}')

# Esse foi por curiosidade, já que o 5 pode ser variável vou colocar pro usuário escolher o desconto

pi2 = float(input('Digite o preço inicial: '))
d2 = float(input('Digite a porcentagem do desconto: '))
pd = (d2/100) * pi2
pf2 = pi2 - pd
print(f'O valor inicial R${pi2} com {d2}% de desconto da o valor final de R${pf2:.2f}')
# Análise de triângulos
# Link do vídeo: https://youtu.be/NZiNphKkxhg?si=tpElcmYn0-zf6CTa

l1 = float(input('Digite o valor do primeiro cateto: '))
l2 = float(input('Digite o valor do segundo cateto: '))
l3 = float(input('Digite o valor da hipotenusa: '))

if l3 >= l1 + l2:
    print('Isso não forma um triângulo')
else:
    print('Isso forma um triângulo')
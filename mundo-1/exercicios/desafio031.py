# Custo da viagem
# Link do vídeo: https://youtu.be/PGqHyzWoagc?si=PTmnZhaHrmHBFtuG

d = float(input('Digite a distância da viagem em km: '))

if d <= 200:
    s = d * 0.5
    print(f'O custo da viagem é de R${s:.2f}')
else:
    s = d * 0.45
    print(f'O custo da viagem é de R${s:.2f}')
# Radar eletrônico
# Link do vídeo: https://youtu.be/hgJ_ETNGSj8?si=g9s4ZEKuzYpEA3ES

v = int(input('Qual foi a velocidade do veículo (km/h)?: '))
if v > 80:
    vm = v - 80
    m = vm * 7
    print(f'Você estava a {vm}km/h acima do limite de velocidade e recebeu uma multa de R${m:.2f}!')
else:
    print('Você estava abaixo do limite de velocidade, boa viagem !')
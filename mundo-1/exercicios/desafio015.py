# Aluguel de carros
# Link do vídeo: https://youtu.be/I4NYUeetLAc?si=M8h1RAuj-deOGCVp

dias = int(input('Quantos dias o carro ficou alugado?: '))
km = float(input('Quantos KM foram rodados?: '))
pd = dias * 60
pkm = km * 0.15
pt = pd + pkm

print(f'O valor a pagar pelo aluguel de {dias} dias e {km}km rodados é de R${pt:.2f}')
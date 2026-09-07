# Condições (finalmente)
# Link do vídeo: https://youtu.be/K10u3XIf1-Q?si=2KYzjUbrsM9w-aRu

n = input('Digite seu nome: ').strip().upper()
if 'ALMEIDA' in n: # Se
    print('Você tem o mesmo sobrenome que eu !')
else: # Se não
    print('Você não tem meu sobrenome')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2

if m >= 5:
    print('Você passou !')
else:
    print('Você reprovou, estude mais !')
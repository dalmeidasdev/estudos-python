# Conversor de bases
# Link do vídeo: https://youtu.be/B3F0IjH5WAM?si=ORiv0G9sYmQiq1M4

n = int(input('Digite um número inteiro para a conversão: '))
e = int(input('Escolha uma opção para conversão:\n[1] Binário\n[2] Hexadecimal\n[3] Octogonal\nResposta: '))

if e == 1:
    print(bin(n)[2:])
elif e == 2:
    print(hex(n)[2:])
elif e == 3:
    print(oct(n)[2:])
else:
    print('Opção inválida !')
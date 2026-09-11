# Maior e menor valores
# Link do vídeo:https://youtu.be/a_8FbW5oH6I?si=9pQG6jcb7KjQ3tqg

n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
n3 = float(input('Digite o terceiro valor: '))

if n1 > n2 and n1 > n3:
    print(f'O maior número é {n1}')
elif n2 > n1 and n2 > n3:
    print(f'O maior número é {n2}')
else:
    print(f'O maior número é {n3}')

if n1 < n2 and n1 < n3:
    print(f'O menor número é {n1}')
elif n2 < n1 and n2 < n3:
    print(f'O menor número é {n2}')
else:
    print(f'O menor número é {n3}')
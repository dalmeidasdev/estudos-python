# Aula de tipos primitivos
# Link do vídeo: https://youtu.be/hdDHg1p3YVc?si=XDmM0U0YScJVVAZh

# Sem o int()
n1 = input('Digite um valor: ')
print(type(n1))

# Com o int()
n2 = int(input('Digite um valor: '))
print(type(n2))

# Soma sem int()
n3 = input('Digite um número: ')
n4 = input('Digite outro: ')
s1 = n3 + n4
print(f'A soma entre {n3} + {n4} é {s1}')

# Soma com int()
n5 = int(input('Digite um número: '))
n6 = int(input('Digite outro: '))
s2 = n5 + n6
print(f'A soma entre {n5} + {n6} é {s2}')

# Convertendo para float()
n = float(input('Digite um valor: '))
print(n)

# Usando .is
n8 = input('Digite algo: ')
print(n8.isnumeric())
print(n8.isalpha())
print(n8.isalnum())
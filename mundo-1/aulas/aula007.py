# Aula sobre operadores aritiméticos
# Link do vídeo: https://youtu.be/Vw6gLypRKmY?si=LR45LXKkX3n3Ry5o

# Adição (+)
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
soma = n1 + n2
print(f'A soma entre {n1} + {n2} é {soma}')

# Subtração (-)
n3 = int(input('Digite um número: '))
n4 = int(input('Digite outro número: '))
subtracao = n3 - n4
print(f'A subtração entre {n3} e {n4} é {subtracao}')

# Multiplicação (*)
n5 = int(input('Digite um número: '))
n6 = int(input('Digite outro número: '))
multiplicacao = n5 * n6
print(f'A multiplicação entre {n5} e {n6} é {multiplicacao}')

# Divisão (/)
n7 = int(input('Digite um número: '))
n8 = int(input('Digite outro número: '))
divisao = n7 / n8
print(f'A divisão entre {n7} e {n8} é {divisao}')

# Divisão inteira (//)
divisaointeira = n7 // n8
print(f'A divisão inteira entre {n7} e {n8} é {divisaointeira}')

# Resto da divisão (%)
resto = n7 % n8
print(f'O resto da divisão entre {n7} e {n8} é {resto}')

# Potência (**) ou pow(n, n2)
n9 = int(input('Digite um número: '))
n10 = int(input('Digite outro número: '))
potencia = n9 ** n10
print(f'{n9} elevado á {n10} é {potencia}')
print(pow(n9, n10))

# Expressão, sendo a ordem de prioridade (), ** * / // %, + -
n11 = int(input('Digite um número: '))
n12 = int(input('Digite outro: '))
n13 = int(input('Digite outro: '))
expressao = n11 * (n12 + n13)
print(f'O resultado da expressão {n11} x ({n12} + {n13}) é {expressao}')

# Raiz (n1 ** (1/n))
n14 = int(input('Digite um número: '))
raiz = n14 ** (1/2)
print(f'A raiz quadrada de {n14} é {raiz}')

# Trabalhando com string
print('Oi' + 'to')
print('Oi'*5)
print('='*20)

# Alterando 'tamanho' da string
# {msg:n} define quantos caracteres vai ter a string
# {msg:>n} ou {msg:^n} ou {msg:<n} define a posição da string em meio ao número de caracteres
# Usar um caractere após o : define o que fica entre a mensagem {msg:=^n}
msg = input('Digite uma mensagem: ')
print(f'A sua mensagem é: {msg:20} !')
print(f'{msg:>20}')
print(f'{msg:^20}')
print(f'{msg:=^20}')
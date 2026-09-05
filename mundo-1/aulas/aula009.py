# Tratamento de texto
# Link do vídeo: https://youtu.be/a7DH88vk2Sk?si=PsYZAbhiSk6p6GSN

# No python toda string está entre aspas (simples, duplas ou até mesmo triplas, por covenção a maioria é simples)
frase = 'Isso é uma string'

# Cada letra ocupa um espaço e recebe um índice, que começa de 0 e segue até o final
# [I][s][s][o][][é][][u][m][a][][s][t][r][i][n][g]
#  0  1  2  3 4  5 6  7  8  9 10 11 12 13 14 15 16
# A primeira letra começa com 0 e não com 1
# Os espaços também contam como um caractere

# Fatiamento
print(frase[9])
# Vai printar apenas o caractere 9, que é o "a"

# Fatiar uma sequência
print(frase[7:10])
# Aqui ele vai printar do caractere inicial (7) até o caractere anterior ao final (10), portanto serão printados os caracteres 7 a 9
# O ultimo caractere não entra na sequência e o : determina de onde até onde vai a sequência
print(frase[9:17])
# Uma das maneiras de fatiar até o fim da frase, não é a mais recomendada

# Fatiar uma sequência pulando caracteres
print(frase[0:17:2])
# O primeiro número representa o início, o segundo o final +1 e o terceiro de quanto em quanto vai pular

# Fatiar do início até um indicador
print(frase[:10])
# Fatia até o caractere 9

# Fatiar do indicador até o final
print(frase[5:])
# Fatia do 5 até o final

# Fatiar do indicador até o final pulando
print(frase[3::2])
# O segundo número vazio indica até o fim

# Análise de tamanho da strig
print(len(frase))

# Conta quantas vezes algo aparece
print(frase.count("a"))

# Count + fatiamento, count(x, inicio, fim)
print(frase.count("s", 0, 10))

# Econtra algo na frase e mostra onde ele começou
print(frase.find("um"))

# Retorna se exite algo na frase
print('Isso' in frase)

# Substitui algo por outro na frase
print(frase.replace('uma', 'duas'))

# Deixar tudo maiúsculo
print(frase.upper())

# Deixar tudo minúsculo
print(frase.lower())

# Deixa tudo minusculo e coloca apenas o primeiro caractere da frase maiúsculo
print(frase.capitalize())

# Deixa a primeira letra de cada palavra maiúsculo
print(frase.title())

# -----------------------------------------------------

frase2 = "      Isso é uma string 2           "

# Remove os espaços inúteis do inicio e final da frase
print(frase2.strip())

# Remove os espaços inúteis somente de um lado
print(frase2.rstrip()) # Direita
print(frase2.lstrip()) # Esquerda

# Dividir a string
print(frase.split())

# Juntar a string
print('-'.join(frase))
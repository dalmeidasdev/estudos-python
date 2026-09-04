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
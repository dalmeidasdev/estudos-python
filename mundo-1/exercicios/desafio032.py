# Ano bisexto
# Link do vídeo: https://youtu.be/cyGY_83m4Xw?si=fWJiTuyBYI6h1h-W

a = int(input('Digite o ano: '))
d = a % 4

if d == 0 and a % 100 != 0 or a % 400 ==0:
    print('É bissexto !')
else:
    print('Não é bissexto !')
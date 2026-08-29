# Ler algo na tela e mostrar seu tipo primitivo e todas as infos
# Link do vídeo: https://youtu.be/tHYxjJxtJko?si=yGINfWnq6gz_mOAk

msg = input('Digite algo: ')

print(type(msg))
print('É alphanumérico?:', msg.isalnum())
print('Todos são alfabéticos?:', msg.isalpha())
print('É um número?:', msg.isnumeric())
print('É decimal?:', msg.isdecimal())
print('É um dígito?:', msg.isdigit())
print('É minusculo?:', msg.islower())
print('É maiusculo?:', msg.isupper())
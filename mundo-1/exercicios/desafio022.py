# Analisador de texto
# Link do vídeo: https://youtu.be/EQQt-6QqXOs?si=33XWRRWUAKGuB5g6

nome = input('Qual seu nome completo?: ')

nomer = nome.title()
print(nomer.upper())
print(nomer.lower())

nomestrip = nomer.strip()
nomesplit = nomestrip.split()
nomesemespaco = "".join(nomesplit)

print(len(nomesemespaco))
print(len(nomesplit[0]))

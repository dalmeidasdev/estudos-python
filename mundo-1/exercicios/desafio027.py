# Primeiro e último nome
# Link do vídeo: https://youtu.be/SifYYsXhLM8?si=whLtTMRdolC96Qrh

nome = input('Digite seu nome completo: ').strip().upper().split()
print('Seu primeiro nome é', nome[0].capitalize())
print('Seu ultimo nome é', nome[-1].capitalize())


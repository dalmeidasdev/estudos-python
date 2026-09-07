# Analisador de número
# Link do vídeo: https://youtu.be/wD2aerLMBWA?si=Abs_WPNdZqoXdDzp

n = int(input('Digite um número inteiro: ')) 

u = n // 1 % 10
d = n // 10 % 10 
c = n // 100 % 10 
m = n // 1000

print(f'Esse número tem {m} milhar(es), {c} centena(s), {d} dezena(s) e {u} unidade(s)')
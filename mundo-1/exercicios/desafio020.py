# Sorteando nome de alunos e a ordem de apresentação
# Link do vídeo: https://youtu.be/OPh0nngbBSY?si=NDZgydf9u4dxZTKb
import random

n1 = input('Digite o nome do primeiro aluno: ')
n2 = input('Digite o nome do segundo aluno: ')
n3 = input('Digite o nome do terceiro aluno: ')
n4 = input('Digite o nome do quarto aluno: ')

nomes = [n1, n2, n3, n4]
random.shuffle(nomes)

print(nomes)
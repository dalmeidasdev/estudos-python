# Primeira vez
# Link do vídeo: https://youtu.be/23UOVEetNPY?si=QcRn5t074iMIpDXg

f = input('Digite uma frase: ').strip()
fm = f.upper()
print('A letra A aparece', fm.count('A'), 'vezes')
fs = fm.split()
print(fs.find('A')+1)

# Reajuste salarial
# Link do vídeo: https://youtu.be/Sfadj_AzKHw?si=1QFFUO7txZ-HDR-n

s = float(input('Digite o seu salário: '))

if s < 1250:
    r = s + ((15/100) * s)
    print(f'O seu novo salário será de R${r:.2f}') 
else:
    r = s + ((10/100) * s)
    print(f'O seu novo salário será de R${r:.2f}')
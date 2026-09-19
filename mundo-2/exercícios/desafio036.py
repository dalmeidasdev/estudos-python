# Aprovando empréstimos
# Link do vídeo: https://youtu.be/IV13X0QOMU8?si=krFJvr37AljelBSB

vcasa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o seu salário: '))
anos = int(input('Em quantos anos pretende pagar?: '))

meses = anos * 12
prestacao = vcasa / meses
limite = (30/100) * salario

if prestacao > limite:
    print('Empréstimo negado !')
else:
    print('Empréstimo aprovado !')
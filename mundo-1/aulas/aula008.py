# Usando módulos
# Link da aula: https://youtu.be/oOUyhGNib2Q?si=aCKV2l1BrWHd3VQM

import math
import random

n = float(input('Digite um número: '))

print(math.ceil(n)) # Arredonda pra cima com ceil()
print(math.floor(n)) # Arredonda para baixo com floor()
print(math.sqrt(n)) # Raiz quadrada com sqrt()
print(math.factorial(int(n))) # Fatorial com factorial()
print(math.log(n)) # Logaritimo com log()

n2 = random.randint(0, 10)
print(n2)
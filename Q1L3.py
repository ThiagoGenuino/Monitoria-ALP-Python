
import re
n=input('Digite um número:')

if re.match(r'^[-+]?\d*\.?\d+$',n):
    n = float(n)
    if n < 0 :
        print('o numero é negativo')
    elif n > 0 :
        print('o numero é positivo')
    else:
        print('o numero é nulo')

else:
    print('Digite um número válido')

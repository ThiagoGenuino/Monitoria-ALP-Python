import re
n1 = input('digite o numero 1:\n')
n2 = input('digite o numero 2:\n')
n3 = input('digite o numero 2:\n')
if re.match(r'^[-+]?\d*\.?\d+$',n1) and re.match(r'^[-+]?\d*\.?\d+$',n2) and re.match(r'^[-+]?\d*\.?\d+$',n2):
    n1 = float(n1)
    n2 = float(n2)
    n3 = float(n3)
    teste = 1
else:
    teste =0

if teste == 1:
    if n1 == n2 or n1 == n3 or n2 == n3:
        print('digite numeros validos')
    else:
        maior = max(n1,n2,n3)
        print('o numero maior digitado é {}'.format(maior))
      
else:
    print('digite numeros validos')
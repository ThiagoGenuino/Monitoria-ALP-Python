import re
import math
n = input('digite um numero inteiro:\n')
if re.match(r'^\d+$',n):
    n = int(n)
    teste = 1 
else:
    teste = 0

if teste == 1:
    raiz_inteira = math.isqrt(n)
    raiz_quadrada = raiz_inteira * 2
    if raiz_quadrada == n:
        print('o numero é um quadrado perfeito')    
    else:
        print('o numero não é um quadrado perfeito')    

else:
    print('digite um numero valido')     

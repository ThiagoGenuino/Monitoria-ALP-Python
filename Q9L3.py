import math
import re 
folhas = input('digite a quantidade de folhas\n')
preco = 0.25
if re.match(r'^\d+$',folhas):
    folhas = int(folhas)
    teste = 1
else:
    teste = 0


if teste == 1:
    if folhas >= 20:
        valor = (folhas*preco)*0.9
        print('o valor a ser pago é {} R$'.format(valor))
    else:
        valor = folhas*preco
        print('o valor a ser pago é {} R$'.format(valor))

else:
    print('digite um numero inteiro valido')
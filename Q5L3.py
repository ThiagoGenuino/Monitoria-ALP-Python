import math
import re 
import datetime

ano_de_nascimento = input('digite ano de nascimento\n')
if re.match(r'^\d+$',ano_de_nascimento):
    ano_de_nascimento = int(ano_de_nascimento)
    teste = 1
else:
    teste = 0

if teste == 1:
    ano_atual  = datetime.datetime.now()
    ano_atual = int(ano_atual.year)
    idade = ano_atual - ano_de_nascimento
    if idade >= 18: 
        print('voce tem {}'.format(idade))
        print('voce pode tirar habilitação e votar')
    elif idade >=16:
        print('voce tem {} anos'.format(idade))
        print('voce pode votar')
    elif ano_de_nascimento > ano_atual :
        print('digite um numero abaixo de {}'.format(ano_atual))
    else:
        print(' voce tem {} anos'.format(idade))
        print('voce não pode nem dirigir nem votar')

else:
    print('digite um numero valido')
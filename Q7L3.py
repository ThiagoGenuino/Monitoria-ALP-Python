import re 

numero1 = input('digite o primeiro numero inteiro\n')
numero2 = input('digite o segundo numero inteiro\n')

if re.match(r'^\d+$',numero1) and (r'^\d+$'):
    numero1, numero2 = int(numero1), int(numero2)
    teste = 1
else:
    teste = 0

if teste == 1:
    div = numero1 % numero2
    if div == 0 :
        print('o numero {} é divisivel por {}'.format(numero1,numero2))
    else:
        print('o numero {} não é divisivel por {}'.format(numero1,numero2))

    


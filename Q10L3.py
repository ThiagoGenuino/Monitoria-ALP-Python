import re
nota1 = input('digite a nota 1:\n')
nota2 = input('digite a nota 2:\n')
if re.match(r'^[-+]?\d*\.?\d+$',nota1) and re.match(r'^[-+]?\d*\.?\d+$',nota2):
    nota1 = float(nota1)
    nota2 = float(nota2)
    teste = 1
else:
    teste =0

if teste == 1:
    nota_final = (nota1 + nota2)/2
    if nota_final >= 7:
        print('sua nota é {} e voce passou'.format(nota_final))
    else:
        print('sua nota é {} e voce reprovou'.format(nota_final))    

else:
    print('digite numeros validos')
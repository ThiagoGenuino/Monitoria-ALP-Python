import re
r1 = input('Digite a resistencia 1:')
r2 = input('Digite a resistencia 2:')

if re.match(r'^[-+]?\d*\.?\d+$',r1) and re.match(r'^[-+]?\d*\.?\d+$',r2) :
    r1, r2 = float(r1), float(r2)
    if r1 > 0 and r2 > 0:
        calculo = (input('digite se quer "serie" ou "paralelo" \n'))
        if calculo == 'serie':
            serie = r1 + r2
            print('valor em serie:{}'.format(serie))
        elif calculo == 'paralelo':
            paralelo = (r1*r2)/(r1+r2)
        else:
            print('digite a opção serie ou paralelo')  
    else:
        print('digite numeros positivos')

else:
    print('Digite somente numeros e positivos')
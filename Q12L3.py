import re
altura = input('digite a altura:\n')
peso = input('digite o peso:\n')
if re.match(r'^\d*\.?\d+$',altura) and re.match(r'^\d*\.?\d+$',peso):
    altura = float(altura)
    peso = float(peso)
    teste = 1
else:
    teste =0

if teste == 1:
    imc = peso/(altura**2)
    if imc > 30:
        print('o seu IMC é {:.2f}'.format(imc))
        print('voce está obeso')
    elif  25 <= imc <= 30:
         print('o seu IMC é {:.2f}'.format(imc))
         print('voce está acima do peso')
    elif 18.5 <= imc < 25:  
        print('o seu IMC é {:.2f}'.format(imc))
        print('voce está no peso normal')    
    else:
        print('o seu IMC é {:.2f}'.format(imc))
        print('voce está abaixo do peso')
      
else:
    print('digite numeros validos')
import re
altura = input('Digite a altura(m²)\n')
peso = input('Digite o peso(kg)\n')

if re.match(r'^[-+]?\d*\.?\d+$',altura) and re.match(r'^[-+]?\d*\.?\d+$',peso):
    altura, peso = float(altura), float(peso)
    sexo = input('digite se é "homem" ou "mulher" ')
    if sexo == 'homem':
        peso_ideal = (altura * 72.7) - 58
        if peso_ideal >= (peso - 5) and peso_ideal <= (peso + 5) :
                print('voce está no peso ideal')
        else: 
            print('voce nao esta no peso ideal')     
    elif sexo == 'mulher':
        peso_ideal = (altura * 62.1) - 44.7
        if peso_ideal >= (peso - 5) and peso_ideal <= (peso + 5) :
                print('voce está no peso ideal')
        else: 
            print('voce nao esta no peso ideal')      
    else: 
         print('digite se é homem ou mulher')
else:
    print('Digite um número válido')

    
    
    

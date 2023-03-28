import re
altura = input('Digite a altura(m²)')
peso = input('Digite o peso(kg)')

if re.match(r'^[-+]?\d*\.?\d+$',altura) and re.match(r'^[-+]?\d*\.?\d+$',peso):
    altura, peso = float(altura), float(peso)
    peso_ideal = (altura * 72.7) - 58 
    if peso_ideal >= (peso - 5) and peso_ideal <= (peso + 5) :
        print('voce está no peso ideal')
    else: 
        print('voce nao esta no peso ideal')
else:
    print('Digite um número válido')
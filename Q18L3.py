import re
x=input('Digite o valor de um lado do triângulo: ')
y=input('Digite o valor do segundo lado: ')
z=input('Digite o valor do outro lado: ')
if re.match(r'^[-+]?\d*\.?\d+$',x) and re.match(r'^[-+]?\d*\.?\d+$',y) and re.match(r'^[-+]?\d*\.?\d+$',z):
    x=float(x)
    y=float(y)
    z=float(z)
    teste = 1 
     
else:
    teste = 0

if teste == 1:
    if x < y+z and y < x+z and z < x+y:
        print('Os valores podem ser comprimentos dos lados de um triângulo.')
        
        if x != y != z != x:
            print('O triângulo é escaleno')
        elif x == y == z:
            print('O triângulo é equilátero')
        elif x == y != z or x == z != y or y == z != x:
            print('O triângulo é isóceles')     
        
        if x**2 == y**2 + z**2 or y**2 == x**2 + z**2 or z**2 == x**2 + y**2:
            print('Triângulo RETÂNGULO')
            if x**2 == y**2 + z**2:
                area1 = (y*z)/2
                print('o valor da area é:{}'.format(area1))
            elif y**2 == x**2 + z**2:
                area2 = (x*z)/2
                print('o valor da area é:{}'.format(area2))
            else:
                area3 = (x*y)/2
                print('o valor da area é:{}'.format(area3))
        else :
            lado_max = max(x,y,z)
            if lado_max == max(x,y,z):
                if x**2 > y**2 + z**2:
                    print('Triângulo Obtusângulo')
                else:
                    print('Triângulo acutangulo')
            elif lado_max == y:
                if y**2 > x**2 + z**2:
                    print('Triângulo Obtusângulo')
                else:
                    print('Triângulo Acutângulo')
            else:
                if z**2 > x**2 + y**2:
                    print('Triângulo Obtusângulo')
                else:
                    print('Triângulo Acutângulo')
    else: 
        print('os valores não podem ser comprimentos dos lados de triangulo')                
else:
    print('digite valores validos.')
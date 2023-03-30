import math
import re

umcentavo = (input("Digite a quantidade de moedas de 1 centavo: "))
cincocentavos = (input("Digite a quantidade de moedas de 5 centavos: "))
dezcentavos = (input("Digite a quantidade de moedas de 10 centavos: "))
vinteecincocentavos = (input("Digite a quantidade de moedas de 25 centavos: "))
cinquentacentavos = (input("Digite a quantidade de moedas de 50 centavos: "))
umreal = (input("Digite a quantidade de moedas de 1 real: "))


notas = [200, 100, 50, 20, 10, 5, 2, 1]

if re.match(r'^\d+$', umcentavo) and re.match(r'^\d+$', cincocentavos) and re.match(r'^\d+$', dezcentavos) and re.match(r'^\d+$', vinteecincocentavos) and re.match(r'^\d+$', cinquentacentavos) and re.match(r'^\d+$', umreal):
    umcentavo = int(umcentavo)
    cincocentavos = int(cincocentavos)
    dezcentavos = int(dezcentavos)
    vinteecincocentavos = int(vinteecincocentavos)
    cinquentacentavos = int(cinquentacentavos)
    umreal = int(umreal)
    teste = 1
    
else:
    teste = 0

if teste == 1:
   
    Tcentavos = (umcentavo * 1) + (cincocentavos * 5) + (dezcentavos * 10) + (vinteecincocentavos * 25) + (cinquentacentavos * 50) + (umreal * 100)
    economia = Tcentavos / 100
    saque = economia
    
    notas200 = saque//notas[0]
    saque -= notas200 * notas[0]
    notas100 = saque//notas[1]
    saque -= notas100 * notas[1]
    notas50 = saque//notas[2]
    saque -= notas50 * notas[2]
    notas20 = saque//notas[3]
    saque -= notas20 * notas[3]
    notas10 = saque//notas[4]
    saque -= notas10 * notas[4]
    notas5 = saque//notas[5]
    saque -= notas5 * notas[5]
    notas2 = saque//notas[6]
    saque -= notas2 * notas[6]
    moeda1 = saque//notas[7]
    saque -= moeda1 * notas[7]

    print('notas de 200:{}, notas de 100:{}, notas de 50:{}, notas de 20:{}, notas de 10:{}, notas de 5:{}, notas de 2:{}, moeda de 1:{} '.format(notas200,notas100,notas50,notas20,notas10,notas5,notas2, moeda1))
    print('total economizado {:.2f}'.format(economia))
else:
    print('digite valores validos')
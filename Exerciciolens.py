

nome = str(input('digite o nome\n'))
idade = int(input('digite a idade\n'))

if nome and idade:
    print('seu nome é {}'.format(nome))
    print('seu nome é invertido é {}'.format(nome))
    if ' ' in nome:
        print('seu nome contem espaços')
    else:
        print('seu nome nao contem espaço')
    print('seu nome tem {} letras'.format(len(nome)))
    print('')
else:
    print('voce deixou campos vazios')
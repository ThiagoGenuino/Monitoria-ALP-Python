import re
import PySimpleGUI as sg
sg.theme('Reddit')
lista=['Brigadeiro','Coxinha','lasanha','Bolo']
layout=[[sg.Text('Qual o seu nome?'), sg.Input(size=(12,1))],
        [sg.Text('Quantos anos você tem?'), sg.Input(size=(7,1))],
        [sg.Text('Você está com fome?'), sg.Checkbox('Sim'), sg.Checkbox('Não')],
        [sg.Text('Escolha uma comida:'), sg.Listbox(lista,size=(9,4))],
        [sg.Button('OK',size=(4,5)), sg.Button('Cancelar',size=(8,5))]]
window=sg.Window('Teste Brigadeiro',layout,font=('Any 25'))
event,values=window.read()
window.close()
if event=='OK':
    if re.match(r'^[a-zA-Záéíãõêô]+$',values[0]) and re.match(r'^\d+$',values[1]):
       
        if values[2] == True :
            layout = [[sg.Text('Olá {}! você tem {} anos, está com fome e escolheu a comida {}'.format(values[0],values[1],values[4]))],
                      [sg.Button('Ok', size=(3, 1))]]
            window = sg.Window('Fome', layout, font=('Any 20'))
            event, values = window.read()
        elif values[2] == False:
            layout = [[sg.Text('Olá {}! você tem {} anos e não está com fome'.format(values[0],values[1],))],
                      [sg.Button('Ok', size=(3, 1))]]
            window = sg.Window('Sem Fome', layout, font=('Any 20'))
            event, values = window.read()

    else:
        layout = [[sg.Text('Preencha todos os dados corretamente')],
                  [sg.Button('OK')]]
        window = sg.Window('Sem número', layout, font=('Any 25'))
        event, values = window.read()
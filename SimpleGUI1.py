'''Lista3, 2º: A altura vezes 72.7 menos 58 é igual ao seu peso ideal. Escreva um programa que posso realizar esse cálculo,
solicitando a altura e o peso e, informe se o paciente se encontra no seu peso ideal ou não'''
import PySimpleGUI as sg
import re
sg.theme('Reddit')
layout = [[sg.Text('Digite a altura: '), sg.Input(size=(5, 1))],
          [sg.Text('Digite o peso: '), sg.Input(size=(5,1))],
          [sg.Button('Ok', size=(3, 1)), sg.Button('Cancelar', size=(8, 1))]]
window = sg.Window('Peso ideal?', layout, font=('Any 20'))
event, values = window.read()
window.close()
if event == 'Ok':
    if re.match(r'^[-+]?\d*\.?\d+$',values[0]) and re.match(r'^[-+]?\d*\.?\d+$',values[1]):
        altura = float(values[0])
        peso = float(values[1])
        ideal=(altura*72.7)-58
        
        if peso == ideal:
            layout = [[sg.Text('Está no peso ideal.')], 
                      [[sg.Text(peso)]], 
                      [[sg.Text(ideal)]],
                      [sg.Button('Ok', size=(3, 1))]]
            window = sg.Window('Peso ideal', layout, font=('Any 20'))
            event, values = window.read()
        elif peso != ideal:
            layout = [[sg.Text('Não está no peso ideal.')],
                      [[sg.Text(peso)]],
                      [[sg.Text(ideal)]],
                      [sg.Button('Ok', size=(3, 1))]]
            window = sg.Window('Não é o ideal', layout, font=('Any 20'))
            event, values = window.read()
    else:
        layout = [[sg.Text('Digite números válidos.')],
                  [sg.Button('Ok', size=(3, 1))]]
        window = sg.Window('Não foi digitado números válidos', layout, font=('Any 30'))
        event, values = window.read()


import PySimpleGUI as sg

layout = [[sg.Text('press Button 1'),sg.Button(' Button 1')],
          [sg.Text('press Button 4'), sg.Button('Button 4')],
          [sg.Text('press Button 2'),sg.Button('Button 2')],
          [sg.Text('press Button 3'),sg.Button('Button 3')]
          ]
window = sg.Window('Janela teste', layout= layout )
print(window.read())
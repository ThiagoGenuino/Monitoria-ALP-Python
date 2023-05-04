import PySimpleGUI as sg

layout_direita = [
    [sg.Image(filename='ifpesimbolo.png')]
]

layout_esquerda = [
    [sg.Text('E-mail:'), sg.Input()],
    [sg.Text('Senha:'), sg.Input(password_char='*')],
    [
        sg.Push(),
        sg.Button('Login!'),
        sg.Push(),
        sg.Button('Esqueci a senha'),
        sg.Push(),
    ],
]

layout = [
    [sg.Column(layout_direita), sg.VSeparator(), sg.Column(layout_esquerda)]
]

window = sg.Window(
    'Janela teste 3',
    layout=layout,
)

print(window.read())
window.close()
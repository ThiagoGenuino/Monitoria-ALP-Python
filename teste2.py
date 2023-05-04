import PySimpleGUI as sg

layout = [
    [sg.Image(filename= 'ifpesimbolo.png')],
    [sg.Text('Digite login do IFPE:')],
    [sg.Text('E-mail institucional:'), sg.Input()],
    [sg.Text('Senha:'), sg.Input(password_char='*')],
    [sg.Button('entrar'), sg.Button('Esqueci a senha')]]
window= sg.Window('Janelateste2',layout, font=('Any 25'))
event,values=window.read()
window.close()

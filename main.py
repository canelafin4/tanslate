import PySimpleGUI as sg
from googletrans import Translator


layout = [
    [sg.Text ('Digitar texto'), sg.Input(key='palavra')],
    [sg.Text ('Idioma'), sg.Input(key='idioma')],
    [sg.Button('Traduzir')]
]

window = sg.Window("Tela de tradução", layout)

while True:
    event, values = window.read()
    translator = Translator()

    if event == sg.WIN_CLOSED:
        break
    
    elif event == 'Traduzir':
        text = values['palavra']
        idioma = values['idioma']

        detected_lang = translator.detect(text).lang
        traducao = translator.translate(text, src=detected_lang, dest= idioma)
        print("Texto original:", text)
        print("Idioma detectado:", detected_lang)
        print(f'Texto traduzido para o {idioma}: ', traducao.text)
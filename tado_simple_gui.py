import PySimpleGUI as sg

# import tado as be
import time


layout1 = [
    [
        sg.Button(
            "Start new game",
            size=(16, 0),
            key="-new game-",
            border_width=(10),
            button_color="#ff1155",
        ),
        sg.Text("", size=(5, 0)),
    ],
    [
        sg.Button(
            "Highscores", size=(16, 0), border_width=(10), button_color="#ff1155"
        ),
        sg.Text("", size=(5, 0)),
    ],
    [
        sg.Button("Load game", size=(16, 0), border_width=(10), button_color="#ff1155"),
        sg.Text("", size=(5, 0)),
    ],
    [
        sg.Button(
            "Difficulty", size=(16, 0), border_width=(10), button_color="#ff1155"
        ),
        sg.Text("", size=(5, 0)),
    ],
    [
        sg.Output(s=(19, 20)),
    ],
    [
        sg.Button(
            "Exit",
            size=(16, 0),
            key="-EXIT-",
            border_width=(10),
            button_color="#ff1155",
        ),
        sg.Text("", size=(5, 0)),
    ],
]
layout2 = [
    [
        sg.Button(
            size=(15, 7),
            button_color=("white"),
        )
        for a in range(4)
    ]
    for col in range(4)
]
layout = [[sg.Col(layout1, p=0), sg.Col(layout2, p=0, visible=False, key="-COL2-")]]
# Sukuriamas langas
window = sg.Window("Tile Memory Game", layout, size=(800, 600))
# Atvaizduojame ir bendraujame su langu, naudodami įvykių kilpą
while True:
    event, values = window.read()
    # Žiūrime, ar vartotojas nori išeiti, ar langas buvo uždarytas
    if event == sg.WINDOW_CLOSED or event == "-EXIT-":
        break
    # Išvedame pranešimą į langą
    if event == "-new game-":
        window["-COL2-"].update(visible=True)
    # window["-Output-"].update("Game starting...")

window.close()

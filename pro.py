import matplotlib.pyplot as plt
import numpy as py
import PySimpleGUI as sg

sg.theme('Black')   
layout = [  [sg.Text('KATEGOORIA NUMBRID')],
            [sg.Text('ÜÜR - 1')],
            [sg.Text('KOMMUNAALID - 2')],
            [sg.Text('TELEFONI OPERAATOR - 3')],
            [sg.Text('RIIDED - 3')],
            [sg.Text('PEOD - 4')],
            [sg.Text('SPORT - 5')],
            [sg.Text('MEELELAHUTUS(kino, teater, jne) - 6')],
            [sg.Text('TRANSPORT - 7')],
            [sg.Text('ILUTEENUSED - 8')],
            [sg.Text('SÖÖK - 8')],
            [sg.Text("Sisesta kategooria number"), sg.InputText(key="kategooria")],
            [sg.Text("Sisesta selles kategoorias kulunud summa"), sg.InputText(key="kategooria_summa")],
            [sg.Button('OK')], [sg.Button('Koosta kuu eelarve fail')], [sg.Button("Lõpeta")]]

window = sg.Window('Kuu eelarve', layout)
event, values = window.read()

kategooria = (values["kategooria"])
kategooria_summa = float(values["kategooria_summa"])
summa = 0
üür_kommud_telefon_transport_summa = 0
meelelahutus_sport = 0
toit = 0
söök = 0
peod = 0
muu = 0

while True:
    def kategooria_summad(kategooria, summa):
        if kategooria == 1 and event == "OK":
            üür_kommud_telefon_transport_summa += kategooria_summa
        if kategooria == 2:
            üür_kommud_telefon_transport_summa += kategooria_summa
        if kategooria == 3 and event == "OK":
            üür_kommud_telefon_transport_summa += kategooria_summa
        if kategooria == 4 and event == "OK":
            peod += kategooria_summa
        if kategooria == 5 and event == "OK":
            meelelahutus_sport += kategooria_summa
        if kategooria == 6 and event == "OK":
            meelelahutus_sport += kategooria_summa
        if kategooria == 7 and event == "OK":
            üür_kommud_telefon_transport_summa += kategooria_summa
        if kategooria == 8 and event == "OK":
            peod += kategooria_summa
        if kategooria == 8 and event == "OK":
            söök += kategooria_summa
    if event == "Lõpeta":
        break


summad = kategooria_summad(kategooria, kategooria_summa)


window.close()
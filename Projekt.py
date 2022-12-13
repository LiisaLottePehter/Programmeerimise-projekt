#programmi tuleb veel lisada see, et need kaks diagrammi oleksid kõrvuti.
#Samuti tuleb lisada programmi soovitused, mis sõltuvad kasutaja sisestusest.
#Näiteks, kui pidutsemiseks ja vabaaja tegevustele kulus liiga palju raha siis programm soovitab järgmine kuu rohkem tähelepanu pöörata säästmisele.
#Veel tuleb muuta sisestused selliseks, et kui kasutaja ei sisesta midagi, küsib programm seda uuesti.
#Programm võiks ka lõpuks inpute küsida kasutajaliideses, et see oleks komplekssem.

#Kõige olulisem, millele raha kulutada:
#Üür, toit, kommunaalid, telefon
#Teise järguline = riided, joomine, meelelahutus
#Võtame arvesse = sissetulek
#sissetulekust lahutame kõige olulisemad
#kui sissetulekust jääb vähe alles peaks programm soovitama sisestajal
#kulutada vähem raha teise järgulistele kulutustele
#samuti võiks programm arvutada iga kuu mingi summa, mille võiks sisestaja
#lisada kuskile hoiufondi, arvutaks protsendi abil

# kokku_üld=100
# majutus_üld=27.3
# vabaaeg_üld=9.1
# söök_üld=18.2
# transport_üld=1.5
# riided_jalanõud_üld=5.5
# alkohol=5.5
# muu=32.9

import matplotlib.pyplot as plt
import numpy as py
import PySimpleGUI as sg

sg.theme('DarkAmber')   
layout = [  [sg.Text('Sisesta oma kuu kulutused')],
            [sg.Text('Palju kulub raha üürile'), sg.InputText()],
            [sg.Text('Palju kulub raha kommunaalideks'), sg.InputText()],
            [sg.Text('Palju kulub raha telefonioperaatoritele maksmiseks'), sg.InputText()],
            [sg.Text('Palju kulub raha riietele'), sg.InputText()],
            [sg.Text('Palju kulub raha pidutsemiseks'), sg.InputText()],
            [sg.Text('Palju kulub raha sportimiseks'), sg.InputText()],
            [sg.Text('Palju kulub raha meelelahutus asutustes käimisele(kino, teater, jne)'), sg.InputText()],
            [sg.Text('Palju kulub raha transpordile'), sg.InputText()],
            [sg.Text('Palju kulub iluteenustele'), sg.InputText()],
            [sg.Text('Palju kulub söögile raha'), sg.InputText()],
            [sg.Button('Sinu kuu eelarve')], [sg.Button('Keskmine üliõpilase kuueelarve')], [sg.Button("Lõpeta")]]

# Create the Window
window = sg.Window('Kuu eelarve', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == "Lõpeta" or event == sg.WIN_CLOSED: # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()

sissetulek = int(input("Sisesta kuu sissetulek: "))
üür = int(input("Palju kulub raha üürile: "))
kommunaalid = int(input("Palju kulub raha kommunaalideks: "))
telefon = int(input("Palju kulub raha telefonioperaatoritele maksmiseks: "))
riided = int(input("Palju kulub raha riietele: "))
peod = int(input("Palju kulub raha pidutsemiseks: "))
sport = int(input("Palju kulub raha sportimiseks: "))
meelelahutus = int(input("Palju kulub raha meelelahutus asutustes käimisele(kino, teater, jne): "))
transport = int(input("Palju kulub raha transpordile: "))
iluteenused = int(input("Palju kulub iluteenustele: "))
söök = int(input("Palju kulub söögile raha: "))

üür_ja_kommunaalid = int(üür + kommunaalid)
vabaaja_tegevused = int(meelelahutus + sport)
muu = int(iluteenused + riided)


p_üür_ja_kommunaalid = (üür_ja_kommunaalid * 100) / sissetulek
p_vabaaja_tegevused = (vabaaja_tegevused * 100)/ sissetulek
p_muu = (muu * 100) / sissetulek
p_söök = (söök * 100)/sissetulek
p_peod = (peod * 100)/sissetulek

Kategooriad = ["Üür ja kommunaalid", "Vabaaja tegevused", "Söök", "Peod", "Muu"]
Osakaal = [p_üür_ja_kommunaalid, p_vabaaja_tegevused, p_söök, p_peod, p_muu]

olulised = üür_ja_kommunaalid + söök + telefon + transport
teise_järgulised = vabaaja_tegevused + muu + peod 

p_olulised = int((olulised * 100) / sissetulek)
print("Olulised kulutused moodustavad sissetulekust " + str(p_olulised) + " protsenti.")

p_teise_järgulised = teise_järgulised * 100 / sissetulek
print("Teise järgulised kulutused moodustavad sissetulekust " + str(p_teise_järgulised) + " protsenti")

plt.bar(Kategooriad, Osakaal)
plt.title("Kuu eelarve")
plt.xlabel("Kategooriad")
plt.ylabel("Osakaal")

plt.show()

andmed={"Majutus":27.3,"Vabaaeg":9.1, "Söök":18.2, "Transport":1.5, "Riided/jalanõud":5.5,"Alkohol":5.5, "Muu":32.9}
valdkonnad=list(andmed.keys())
protsendid=list(andmed.values())
#moodustan tabeli
plt.bar(valdkonnad, protsendid)
plt.title("Tartu tudengite keskmised kulud kuus")
plt.xlabel("Valdkonnad")
plt.ylabel("Kulud protsentides( keskmine sissetulek: 550 eurot")

plt.show()
import matplotlib.pyplot as plt
import numpy as py
import PySimpleGUI as sg

sg.theme('Black')   
layout = [  [sg.Text('Sisesta oma kuu kulutused')],
            [sg.Text('Kui suur on sissetulek'), sg.InputText(key="sissetulek")],
            [sg.Text('Palju kulub raha üürile'), sg.InputText(key="üür")],
            [sg.Text('Palju kulub raha kommunaalideks'), sg.InputText(key="kommunaalid")],
            [sg.Text('Palju kulub raha telefonioperaatoritele maksmiseks'), sg.InputText(key="telefon")],
            [sg.Text('Palju kulub raha riietele'), sg.InputText(key="riided")],
            [sg.Text('Palju kulub raha pidutsemiseks'), sg.InputText(key="peod")],
            [sg.Text('Palju kulub raha sportimiseks'), sg.InputText(key="sport")],
            [sg.Text('Palju kulub raha meelelahutus asutustes käimisele(kino, teater, jne)'), sg.InputText(key="meelelahutus")],
            [sg.Text('Palju kulub raha transpordile'), sg.InputText(key="transport")],
            [sg.Text('Palju kulub iluteenustele'), sg.InputText(key="iluteenused")],
            [sg.Text('Palju kulub söögile raha'), sg.InputText(key="söök")],
            [sg.Button('Sinu kuu eelarve')], [sg.Button('Keskmine üliõpilase kuueelarve')], [sg.Button("Lõpeta")]]


window = sg.Window('Kuu eelarve', layout)
event, values = window.read()

sissetulek = float(values["sissetulek"])
üür = float(values["üür"])
kommunaalid = float(values["kommunaalid"])
telefon = float(values["telefon"])
riided = float(values["riided"])
peod = float(values["peod"])
sport = float(values["sport"])
meelelahutus = float(values["meelelahutus"])
transport = float(values["transport"])
iluteenused = float(values["iluteenused"])
söök = float(values["söök"])

fail = open("Kuu eelarve.txt", "w") 

def kahe_arg_protsent(ü_arg, t_arg):
    summa1 = ü_arg + t_arg
    p_üür_ja_kommunaalid = (summa1 * 100) / sissetulek
    return round(p_üür_ja_kommunaalid, 2)

p_üür_ja_kommunaalid = kahe_arg_protsent(üür, kommunaalid)

p_vabaaja_tegevused = kahe_arg_protsent(meelelahutus, sport)

p_muu = kahe_arg_protsent(iluteenused, riided)

def ühe_arg_protsent(ü_arg):
    p_söök = (ü_arg * 100)/sissetulek
    return round(p_söök, 2)

p_söök = ühe_arg_protsent(söök)

p_peod = ühe_arg_protsent(peod)

p_transport = ühe_arg_protsent(transport)

p_riided = ühe_arg_protsent(riided)

#Tingimuslaused
def soovitused(majutus, vabaaeg, söök, transport, riided, peod, muu):
    #argumendid peab olema võtetud protsentide arvutamise funktsioonidest
    if majutus <= 27.3: #majutuse protsent
        fail.write("Majutuse kulud on alla või võrdne keskmise protsendiga, 27.3% sissetulekust. Tubli!" + "\n")
    if majutus > 27.3:
        fail.write("Kulud majutusele on suuremad keskmisest, 27.3%. Eeldades, et majutuse kulutusi ei saa muuta, proovi hoida raha kokku kusagilt mujalt." + "\n")

    if vabaaeg<= 9.1:
        fail.write("Spordi, meelelahutuse ja muud vabaaja kulud on alla või võrdne keskmisest, 9.1% sissetulekust. Oled oma sissetulekut hästi kasutanud!" + "\n")
    if vabaaeg > 9.1:
        fail.write("Kulutused vabale ajale nagu sport, meelelahutus ja muu on üle keskmise. Proovi hoida kusagilt kokku, nt käi kinos ainult kaks korda kuus ja vaata ilme kodust, või käi väljas jooksmas sporisaali membershipi ostmise asemel." + "\n")

    if söök <= 18.2:
        fail.write("Söögi peale läheb täpselt nii palju, kui vaja on." + "\n")
    if söök > 18.2:
        fail.write("Võib-olla sa tellid liiga palju toitu koju võid sööd palju väljas. Katseta rohkem kodus kokkamist ning valmista sööki suures koguses, et saaks süüa sama einet ka nt lõunaks." + "\n")

    if transport <= 1.5:
        fail.write("Transpordilt oled säästnud hästi" + "\n")
    if transport > 1.5:
        fail.write("Oma autoga sõites võivad kõrged transpordi kulutused olla põhjustatud bensiini hindadest. Taksod on ka kallid-taksosõidud jäta olukordadeks, kus muu transport pole võimalik. Lisaks, käi palju jala kui võimalik on. See on ka tervisele hea :D" + "\n")
 
    if riided <= 5.5:
        fail.write("Riietele ja jalanõudele ei kulu kuus palju. Tavaliselt ostetakse kalleid tooteid nagu saapad kord aastas. Väiksemad tooted nagu sokid ja t-särgid on suhteliselt odavad." + "\n")
    if riided > 5.5:
        fail.write("Hoidu impulsiivsetest ostudest. Kaltsukad ning teiseringi poed on ka mitmetes linnades saadaval. Isegi äpid nagu Yaga aitavad leida kvaliteetseid riideid odavamate hindadega." + "\n")
 
    if peod <= 5.5:
        fail.write("Tubli oled. Alkohol on kallis, eriti baarides ning klubides. Ühe õhtuga võib kaduda üle 20 euro." + "\n")
    if peod > 5.5:
        fail.write("Ole ettevaatlik. Liigne alkoholi tarbimine ei mõju tervisele ega rahakotile hästi. Sea endale alkoholi tarbimiseks piirangud, nii rahalised kui ka enda tervise jaoks." + "\n")
      
    if muu <= 32.9:
        fail.write("Säästad hästi raha muude asjade jaoks-olgu need kõrvale pandud hädavara säästud või kogud raha suure ostu jaoks : D" + "\n")
    if muu > 32.9:
        fail.write("Väldi impulsiivseid oste ja koosta iga kuu endale korralik eelarve. Raha peaks olema ka tagavara kontol rasketeks olukordadeks." + "\n")

soovitused2 = soovitused(p_üür_ja_kommunaalid, p_vabaaja_tegevused, p_söök, p_transport, p_riided, p_peod, p_muu) 

#diagrammi funktsioon

fail = open("Kuu eelarve.txt", "w")

def tudengi_eelarve(p_üür_ja_kommunaalid, p_vabaaja_tegevused, p_muu, p_söök, p_peod):
    Kategooriad = ["Üür ja kommunaalid", "Vabaaja tegevused", "Söök", "Peod", "Muu"]
    Osakaal = [p_üür_ja_kommunaalid, p_vabaaja_tegevused, p_söök, p_peod, p_muu]
    plt.bar(Kategooriad, Osakaal)
    plt.title("Kuu eelarve")
    plt.xlabel("Kategooriad")
    plt.ylabel("Osakaal")
    return plt.savefig("fail")

def keskmine_tudengi_eelarve(andmed):
    valdkonnad=list(andmed.keys())
    protsendid=list(andmed.values())
    #moodustan tabeli
    plt.bar(valdkonnad, protsendid)
    plt.title("Tartu tudengite keskmised kulud kuus")
    plt.xlabel("Valdkonnad")
    plt.ylabel("Kulud protsentides( keskmine sissetulek: 550 eurot")
    return plt.savefig("fail")

tudengi_eelarve_diagramm = tudengi_eelarve(p_üür_ja_kommunaalid, p_vabaaja_tegevused, p_muu, p_söök, p_peod)
andmed={"Üür ja kommunaalid":27.3,"Vabaaeg":9.1, "Söök":18.2, "Transport":1.5, "Riided/jalanõud":5.5,"Alkohol":5.5, "Muu":32.9}
keskmise_tudengi_eelarve_diagramm = keskmine_tudengi_eelarve(andmed)

fail.write(soovitused2)
fail.write(tudengi_eelarve_diagramm)
fail.write(keskmise_tudengi_eelarve_diagramm)

while True:
    if event == "Lõpeta":
        break
    elif event == "Sinu kuu eelarve":
        sg.popup(fail)
        
    elif event == "Keskmine üliõpilase kuueelarve":
        sg.popup(keskmise_tudengi_eelarve_diagramm)

fail.close()
window.close()


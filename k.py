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
            [sg.Button("Sinu kuu eelarve graafik")], 
            [sg.Button("Keskmise tudengi eelarve graafik")], 
            [sg.Button("Näita soovitusi")], 
            [sg.Button("Lõpeta")]]


window = sg.Window('Kuu eelarve', layout)

def kahe_arg_protsent(ü_arg, t_arg):
    summa1 = ü_arg + t_arg
    p_üür_ja_kommunaalid = (summa1 * 100) / sissetulek
    return round(p_üür_ja_kommunaalid, 2)

def ühe_arg_protsent(ü_arg):
    p_söök = (ü_arg * 100)/sissetulek
    return round(p_söök, 2)

def keskmine_tudengi_eelarve():
    andmed={"Üür ja kom":27.3,"Vabaaeg":9.1, "Söök":18.2, "Trans":1.5, "Riided":5.5,"Peod":5.5, "Muu":32.9}
    valdkonnad=list(andmed.keys())
    protsendid=list(andmed.values())
    #moodustan tabeli
    plt.bar(valdkonnad, protsendid)
    plt.title("Tartu tudengite keskmised kulud kuus")
    plt.xlabel("Valdkonnad")
    plt.ylabel("Kulud protsentides( keskmine sissetulek: 550 eurot")
    return plt.show(block=False)

def tudengi_eelarve(ü, t, k, n, v):
    Kategooriad = ["Üür ja kom", "Vabaaeg", "Söök", "Peod", "Muu"]
    Osakaal = [ü, t, k, n, v]
    plt.bar(Kategooriad, Osakaal)
    plt.title("Kuu eelarve")
    plt.xlabel("Kategooriad")
    plt.ylabel("Osakaal")
    return plt.show(block=False)

soovituste_järjend = []

#Tingimuslaused
def soovitused(majutus, vabaaeg, söök, transport, riided, peod, muu):
    #argumendid peab olema võtetud protsentide arvutamise funktsioonidest
    if majutus <= 27.3: #majutuse protsent
        soovituste_järjend.append("\n" + "Majutuse kulud on alla või võrdne keskmise protsendiga, 27.3% sissetulekust. Tubli!")
    if majutus > 27.3:
        soovituste_järjend.append("Kulud majutusele on suuremad keskmisest, 27.3%. Eeldades, et majutuse kulutusi ei saa muuta, proovi hoida raha kokku kusagilt mujalt.")

    if vabaaeg<= 9.1:
        soovituste_järjend.append("Spordi, meelelahutuse ja muud vabaaja kulud on alla või võrdne keskmisest, 9.1% sissetulekust. Oled oma sissetulekut hästi kasutanud!")
    if vabaaeg > 9.1:
        soovituste_järjend.append("Kulutused vabale ajale nagu sport, meelelahutus ja muu on üle keskmise. Proovi hoida kusagilt kokku, nt käi kinos ainult kaks korda kuus ja vaata ilme kodust, või käi väljas jooksmas sporisaali membershipi ostmise asemel.")

    if söök <= 18.2:
        soovituste_järjend.append("Söögi peale läheb täpselt nii palju, kui vaja on.")
    if söök > 18.2:
        soovituste_järjend.append("Võib-olla sa tellid liiga palju toitu koju võid sööd palju väljas. Katseta rohkem kodus kokkamist ning valmista sööki suures koguses, et saaks süüa sama einet ka nt lõunaks.")

    if transport <= 1.5:
        soovituste_järjend.append("Transpordilt oled säästnud hästi")
    if transport > 1.5:
        soovituste_järjend.append("Oma autoga sõites võivad kõrged transpordi kulutused olla põhjustatud bensiini hindadest. Taksod on ka kallid-taksosõidud jäta olukordadeks, kus muu transport pole võimalik. Lisaks, käi palju jala kui võimalik on. See on ka tervisele hea :D")
 
    if riided <= 5.5:
        soovituste_järjend.append("Riietele ja jalanõudele ei kulu kuus palju. Tavaliselt ostetakse kalleid tooteid nagu saapad kord aastas. Väiksemad tooted nagu sokid ja t-särgid on suhteliselt odavad.")
    if riided > 5.5:
        soovituste_järjend.append("Hoidu impulsiivsetest ostudest. Kaltsukad ning teiseringi poed on ka mitmetes linnades saadaval. Isegi äpid nagu Yaga aitavad leida kvaliteetseid riideid odavamate hindadega.")
 
    if peod <= 5.5:
        soovituste_järjend.append("Tubli oled. Alkohol on kallis, eriti baarides ning klubides. Ühe õhtuga võib kaduda üle 20 euro.")
    if peod > 5.5:
        soovituste_järjend.append("Ole ettevaatlik. Liigne alkoholi tarbimine ei mõju tervisele ega rahakotile hästi. Sea endale alkoholi tarbimiseks piirangud, nii rahalised kui ka enda tervise jaoks.")
      
    if muu <= 32.9:
        soovituste_järjend.append("Säästad hästi raha muude asjade jaoks-olgu need kõrvale pandud hädavara säästud või kogud raha suure ostu jaoks : D")
    if muu > 32.9:
        soovituste_järjend.append("Väldi impulsiivseid oste ja koosta iga kuu endale korralik eelarve. Raha peaks olema ka tagavara kontol rasketeks olukordadeks.")
    return soovituste_järjend

while True: 
    event, values = window.Read()
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

    p_söök = ühe_arg_protsent(söök)
    p_peod = ühe_arg_protsent(peod)
    p_transport = ühe_arg_protsent(transport)
    p_riided = ühe_arg_protsent(riided)

    p_üür_ja_kommunaalid = kahe_arg_protsent(üür, kommunaalid)
    p_vabaaja_tegevused = kahe_arg_protsent(meelelahutus, sport)
    p_muu = kahe_arg_protsent(iluteenused, riided)

    olulised = üür + kommunaalid + söök + telefon + transport
    teise_järgulised = meelelahutus + sport + peod + iluteenused + riided

    p_olulised = ühe_arg_protsent(olulised)
    p_teise_järgulised = ühe_arg_protsent(teise_järgulised)

    soovituste_järjend.append("Oluliste kulutuste(üür, kommunaalid, söök, telefon ja transport) kulutuste summa on "+ str(olulised) + " ja protsent kogu kulutustest on " + str(p_olulised) +"%.")
    soovituste_järjend.append("Teise järguliste(meelelahutus, sport, peod, riided, jne.) kulutuste summa on "+ str(teise_järgulised) + " ja protsent kogu kulutustest on " + str(p_teise_järgulised) +"%.")

    soovitused2 = soovitused(p_üür_ja_kommunaalid, p_vabaaja_tegevused, p_söök, p_transport, p_riided, p_peod, p_muu) 
    if p_olulised > p_teise_järgulised:
        soovituste_järjend.append("Tubli, olulistele kulutustele kulus rohkem kui teise järgulistele")
    else:
        soovituste_järjend.append("Proovi järgmine kuu jälgida teisejärguliste kulutuste suurust")
    if event == "Lõpeta":
        break
    elif event == "Sinu kuu eelarve graafik":
        tudengi_eelarve(p_üür_ja_kommunaalid, p_vabaaja_tegevused, p_söök, p_peod, p_muu)
    elif event == "Keskmise tudengi eelarve graafik":
        keskmine_tudengi_eelarve()
    elif event == "Näita soovitusi":
        sg.popup(*soovitused2)

window.close()



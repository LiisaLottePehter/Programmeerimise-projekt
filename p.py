import matplotlib.pyplot as plt
import numpy as py

def keskmine_tudengi_eelarve(andmed):
    valdkonnad=list(andmed.keys())
    protsendid=list(andmed.values())
    #moodustan tabeli
    plt.bar(valdkonnad, protsendid)
    plt.title("Tartu tudengite keskmised kulud kuus")
    plt.xlabel("Valdkonnad")
    plt.ylabel("Kulud protsentides( keskmine sissetulek: 550 eurot")
    return plt.show()

andmed={"Üür ja kom":27.3,"Vabaaeg":9.1, "Söök":18.2, "Trans":1.5, "Riided":5.5,"Peod":5.5, "Muu":32.9}
keskmise_tudengi_eelarve_diagramm = keskmine_tudengi_eelarve(andmed)
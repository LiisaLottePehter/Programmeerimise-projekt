import matplotlib.pyplot as plt
import numpy as py

def tudengi_eelarve(p_üür_ja_kommunaalid, p_vabaaja_tegevused, p_muu, p_söök, p_peod):
    Kategooriad = ["Üür ja kom", "Vabaaeg", "Söök", "Peod", "Muu"]
    Osakaal = [p_üür_ja_kommunaalid, p_vabaaja_tegevused, p_söök, p_peod, p_muu]
    plt.bar(Kategooriad, Osakaal)
    plt.title("Kuu eelarve")
    plt.xlabel("Kategooriad")
    plt.ylabel("Osakaal")
    return plt.show()

tudengi_eelarve_diagramm = tudengi_eelarve(30, 29, 40, 30, 20)

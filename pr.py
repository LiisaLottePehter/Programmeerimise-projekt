import tkinter as tk

aken = tk.Tk()
aken.title("Kasutaja sisestused")

tk.Label(aken, text='ÜÜR').grid(row=0)
tk.Label(aken, text='KOMMUNAALID').grid(row=1)
tk.Label(aken, text='TELEFONI OPERAATOR').grid(row=2)
tk.Label(aken, text='RIIDED').grid(row=3)
tk.Label(aken, text='PEOD').grid(row=4)
tk.Label(aken, text='SPORT').grid(row=5)
tk.Label(aken, text='MEELELAHUTUS(kino, teater, jne)').grid(row=6)
tk.Label(aken, text='ILUTEENUSED').grid(row=7)
tk.Label(aken, text='SÖÖK').grid(row=8)
tk.Label(aken, text='MUU').grid(row=9)
tk.Label(aken, text='SISSETULEK').grid(row=10)



aken.mainloop()
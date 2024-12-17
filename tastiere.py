import tkinter as tk
import tasti as t


class TastieraNumeri:
    def __init__(self):
        self.frame = tk.Frame()
        self.tastiNumeri = []
        for i in range(10):
            riga = int(i/3)
            colonna = i % 3
            valore = (i+1) % 10
            tastoNum = t.TastoNumerico(self.frame, valore, riga, colonna)
            self.tastiNumeri.append(tastoNum)

        # aggiusto tasto 0 e spazi
        self.tastiNumeri[9].y = 1
        tastoVuotoSx = tk.Button(self.frame, command="", background="black", width=1, wraplength=1, state=tk.DISABLED)
        tastoVuotoSx.grid(row=3, column=0)
        tastoVuotoDx = tk.Button(self.frame, command="", background="black", width=1, wraplength=1, state=tk.DISABLED)
        tastoVuotoDx.grid(row=3, column=2)

        # posiziono tasti sul frame
        for i in range(10):
            self.tastiNumeri[i].grid(row=self.tastiNumeri[i].x, column=self.tastiNumeri[i].y)

    def getElem(self, i):
        if 0 <= i < len(self.tastiNumeri):
            return self.tastiNumeri[i]


class TastieraOperazioni:
    def __init__(self):
        self.frame = tk.Frame()
        self.tastiOper = []
        riga = 0

        # tastiera standard
        for simbolo in ["+", "-", "*", "/", "="]:
            tastoOper = t.TastoOperazione(self.frame, simbolo, riga, 0)
            self.tastiOper.append(tastoOper)
            riga = riga + 1

    def aggiungi(self, tastoOperazione):
        self.tastiOper.append(tastoOperazione)

    # posiziono tasti sul frame
    def posiziona(self):
        for tasto in self.tastiOper:
            # tasto.stampa()
            tasto.grid(row=tasto.x, column=tasto.y)
            # tasto.pack()

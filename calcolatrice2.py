import tkinter as tk
import tasti as t
import tastiere as tt

clicccato = ""

class Calcolatrice:
    def __init__(self):
        self.fin = tk.Tk()
        self.fin.configure(background="grey")
        self.fin.title("Calcolatrice")
        self.fin.geometry("250x500+500+500")
        self.cliccato = ""

        # replica tasti
        empty = ""
        self.lettura = tk.StringVar(self.fin)
        self.etichetta = tk.Label(self.fin, text=empty, background="black", font="Helvetica 30", fg="white", textvariable=self.lettura)
        self.etichetta.grid(row=0, column=0, columnspan=4, sticky="SW")

        # tastiera numeri
        # self.frameNumeri = tk.Frame(self.fin)
        self.tastiNumeri = []
        for i in range(10):
            riga = int(i / 3)
            colonna = i % 3
            valore = (i + 1) % 10
            tasto = t.Tasto(self.fin, valore, riga, colonna)
            tasto.grid(row=riga+1, column=colonna)
            tasto.bind("<Button-1>", lambda e, a = valore: self.mostra(a))
            self.tastiNumeri.append(tasto)

        self.tastiNumeri[9].grid(row=4, column=1)
        # self.frameNumeri.grid(row=1, column=0)

        # tastiera operazioni
        i = 1
        self.tastiOperazione = []
        for simbolo in ["+", "-", "*", "/"]:
            tastoOp = t.TastoOperazione(self.fin, simbolo, i, 4)
            self.tastiOperazione.append(tastoOp)
            tastoOp.grid(row=i, column=4)
            i = i + 1

    def mostra(self, v):
        cliccato = v
        testoNuovo=""
        visualizzatore =  self.lettura.get()
        maxLenght = 7
        if len(visualizzatore) >= maxLenght:
            for i in range(maxLenght):
                testoNuovo = testoNuovo + visualizzatore[i]

            visualizzatore = testoNuovo

        else:
            visualizzatore = visualizzatore + str(cliccato)

        self.lettura.set(visualizzatore)

    '''
    def aggOperazione(self, tastoOperazione):
        self.tastieraOperazioni.aggiungi(tastoOperazione)
    '''
    def vai(self):
        self.fin.mainloop()

c = Calcolatrice()
c.vai()

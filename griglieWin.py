import tkinter as tk

class Griglia (tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Griglia")
        self.geometry("300x180+1200+600")
        self.resizable(False, False)

        self.setup()

        # definisco griglia di caselle di testo
        frmCaselle = tk.Frame(self)
        caselle =[]

        for i in range(3):
            riga = []
            for j in range(3):
                casella = tk.Entry(frmCaselle, width=3, textvariable=self.valori[i][j])
                casella.configure(font=("verdana",20, "bold"))
                riga.append(casella)
                casella.grid(row = i, column = j)
            caselle.append(riga)

        pulsante = tk.Button(self, fg="yellow", text = "Invia", background="black", font=("white", 12, "bold"), width=10, height=1, command=self.controllo)
        frmCaselle.pack()
        pulsante.pack(pady=10)

    def setup(self):
            # definisco matrice variabili
            self.valori = []
            for i in range(3):
                riga = []
                for j in range(3):
                    v = tk.IntVar()
                    riga.append(v)
                self.valori.append(riga)

            # self.valori default
            self.valori[0][2].set(43)
            self.valori[1][0].set(73)
            self.valori[2][1].set(13)


    def sommaRiga(self, riga):
        sommaRiga = 0
        for j in range(3):
            sommaRiga += self.valori[riga][j].get()

        if sommaRiga == 111:
            return True
        else:
            return False


    def sommaColonna(self, col):
        sommaCol = 0
        for i in range(3):
            sommaCol += self.valori[i][col].get()

        if sommaCol == 111:
            return True
        else:
            return False

    def sommaDiagSx(self):
        sommaDiagSx = 0
        for i in range(3):
            sommaDiagSx += self.valori[i][i].get()

        if sommaDiagSx == 111:
            return True
        else:
            return False

    def sommaDiagDx(self):
        sommaDiagDx = 0
        for i in range(3):
            sommaDiagDx += self.valori[i][2-i].get()

        if sommaDiagDx == 111:
            return True
        else:
            return False


    def controllo(self):
        if self.sommaRiga(0) and self.sommaRiga(1) and self.sommaRiga(2) and self.sommaColonna(0) and self.sommaColonna(1) and self.sommaColonna(2) and self.sommaDiagSx() and self.sommaDiagDx():
            print("vittoria")
        else:
            print("correggi")

        self.stampa()


    def stampa(self):
        for i in range (3):
            print()
            for j in range(3):
                print(self.valori[i][j].get(), end = " ")

g = Griglia()
g.mainloop()

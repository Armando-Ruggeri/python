import tkinter as tk
import tastiere as tt
class Calcolatrice:
    def __init__(self):
        self.fin = tk.Tk()
        self.fin.configure(background="grey")
        self.fin.title("Calcolatrice")
        self.fin.geometry("250x500+500+500")

        # replica tasti
        empty = "               "
        self.etichetta = tk.Label(self.fin, text=empty, background="orange", font="Helvetica 30")
        self.etichetta.grid(row=0, column=0, columnspan=4, sticky="SW")

        # tastiera numeri
        self.tastieraNumeri = tt.TastieraNumeri()
        self.tastieraNumeri.frame.grid(row=1, column=0, columnspan=1,rowspan=1,sticky="N")

        # tastiera operazioni
        self.tastieraOperazioni = tt.TastieraOperazioni()
        self.tastieraOperazioni.frame.grid(row=1, column=1, sticky="W")

        # parte bassa
        self.etichetta2 = tk.Label(self.fin, text=empty, background="green", font="Helvetica 30")
        self.etichetta2.grid(row=3, column=0, columnspan=4, sticky="N")

    def mostra(self):
        print("cliccato")

    '''
    def aggOperazione(self, tastoOperazione):
        self.tastieraOperazioni.aggiungi(tastoOperazione)
    '''
    def vai(self):
        self.tastieraOperazioni.posiziona()
        self.fin.mainloop()

c = Calcolatrice()
c.vai()

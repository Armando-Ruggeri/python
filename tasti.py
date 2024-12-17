import tkinter as tk

class Tasto(tk.Button):
    def __init__(self, finestra, valore, posX, posY):
        tk.Button.__init__(self, finestra, text= valore, font="Helvetica 30")
        self.valore = valore
        self.x = posX
        self.y = posY
        self.cliccato =""

    def stampa(self):
        print(f"{self.valore} {self.x} {self.y}")


class TastoNumerico(Tasto):
    def __init__(self, finestra, valore, posX, posY):
        if 0<= valore<=9:
            Tasto.__init__(self, finestra, valore, posX, posY)
        else:
            print("Tasto numerico non corretto")


class TastoOperazione(Tasto):
    def __init__(self, finestra, valore, posX, posY):
        Tasto.__init__(self, finestra, valore, posX, posY)
        self.config(background="black", fg="white", width=1, wraplength=1)
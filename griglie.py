import tkinter as tk

def stampa():
    print (valori[0][0].get())

fin = tk.Tk()
fin.title = "GRIGLIA"
fin.geometry("280x180+1200+600")
fin.resizable(False, False)

# definisco griglia variabili
valori = []
for i in range(3):
    riga = []
    for j in range(3):
        v = tk.IntVar()
        riga.append(v)
    valori.append(riga)

valori[0][2].set(43)
valori[1][0].set(73)
valori[2][1].set(13)
# definisco griglia di caselle di testo
frmCaselle = tk.Frame()
caselle =[]

for i in range(3):
    for j in range(3):
        casella = tk.Entry(frmCaselle, width=3, textvariable=valori[i][j])
        casella.configure(font=("verdana",20, "bold"))
        riga.append(casella)
        casella.grid(row = i, column = j)
    caselle.append(riga)

pulsante = tk.Button(text = "Invia", width=10, command=stampa)
frmCaselle.pack()
pulsante.pack()
fin.mainloop()

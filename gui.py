import tkinter as t
from tkinter import ttk as tt
'''
La gerarchia dei widget 
I widget sono disposti in una gerarchia. L'etichetta e il pulsante erano contenuti in un contenitore, 
che a sua volta è contenuto nella finestra principale. 
Quando si crea un widget figlio, il suo widget padre viene passato come primo parametro al costruttore del widget. 

Opzioni di configurazione 
I widget hanno opzioni di configurazione che ne modificano l'aspetto e il comportamento, come il testo da visualizzare 
in un'etichetta o in un pulsante. Le diverse classi di widget avranno diversi set di opzioni. 
La gestione della geometria 
I widget non vengono aggiunti automaticamente all'interfaccia utente quando vengono creati. Un gestore di geometrie 
come la griglia controlla la posizione dei widget nell'interfaccia utente. 

Il ciclo di eventi 
Tkinter reagisce agli input dell'utente, alle modifiche del programma e aggiorna il display solo quando è in 
esecuzione un ciclo di eventi. Se il programma non esegue il ciclo di eventi, l'interfaccia utente non si 
aggiorna.
'''

class MyWindow:
    def __init__(self):
        # crea la finestra
        self.finestra = t.Tk()
        
        # definisce dimensioni e posizione
        self.finestra.geometry("430x250+1000+500")
        
        # configura la finestra
        self.finestra.configure(bg="grey")
        
        # imposta il titolo della finestra
        self.finestra.title("Finestra 1")
        
        # crea i widget e li configura
        etichetta = t.Label(text="Nome", background="#ff1144")
        nome = t.Entry(text="Scrivi il nome")
        pulsante = t.Button(text="Invia")
        
        # listbox
        indirizzi = t.Listbox(height = 5)
        indirizzi.insert(1, "Informatica")
        indirizzi.insert(3, "Biotecnologie")
        indirizzi.insert(2, "Economico")
        
        # combobox
        scelta = t.StringVar()
        sezioni= tt.Combobox(self.finestra, textvariable = scelta, width=3)
        sezioni["values"] = ["A", "B", "C", "D"]
        
        # pulsanti di controllo
        prom = t.StringVar()
        bocc = t.StringVar()
        promosso = t.Checkbutton(text="promosso", variable=prom)
        bocciato = t.Checkbutton(text="bocciato", variable= bocc)
        
        # posiziona i widget attacca alla finestra
        etichetta.grid(row=0,column=0, sticky="E")
        nome.grid(row=0,column=1)
        indirizzi.grid(row=1,column=0, pady=15, padx=15)
        sezioni.grid(row=1,column=1, pady=15, padx=5, sticky="NW")
        promosso.grid(row=3,column=0)
        bocciato.grid(row=3,column=1)
        bocciato.deselect()

        pulsante.grid(row=3,column=2, sticky="S", padx=20)
        
        # avvia il ciclo
        self.finestra.mainloop()

win = MyWindow()
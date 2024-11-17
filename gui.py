import tkinter as t
from tkinter import ttk as tt
'''
La gerarchia dei widget 
I widget sono disposti in una gerarchia. L'Nome e il pulsante erano contenuti in un contenitore, 
che a sua volta è contenuto nella finestra principale. 
Quando si crea un widget figlio, il suo widget padre viene passato come primo parametro al costruttore del widget. 

Opzioni di configurazione 
I widget hanno opzioni di configurazione che ne modificano l'aspetto e il comportamento, come il testo da visualizzare 
in un'Nome o in un pulsante. Le diverse classi di widget avranno diversi set di opzioni. 
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
        distanzaX = 10
        distanzaY = 10
        
        # crea la finestra
        self.finestra = t.Tk()
        
        # definisce dimensioni e posizione
        self.finestra.geometry("450x300+1000+500")
        
        # configura la finestra
        self.finestra.configure(bg="grey")
        
        # imposta il titolo della finestra
        self.finestra.title("Finestra 1")
        
        # crea i widget e li configura
        frame = t.Frame(self.finestra)
        
        etichettaNome = t.Label(frame, text="Nome", background="#ff1144", width=5)
        nome = t.Entry(frame, text="Scrivi il nome", background="#77ffaa", width=25)
        
        # creazione pulsante e definizione azione evento (callback)
        pulsante = t.Button(text="Stampa Sezione", command=self.stampaSezione)
        pulsante2 = t.Button(text="Stampa Indirizzo", command=self.stampaIndirizzo)
        pulsante3 = t.Button(text="Entrambi", command=self.stampaIndirizzo)
        pulsante3.bind( '<Button-3>', self.click)
        
        # listbox
        self.indirizzi = t.Listbox(height = 5)
        self.indirizzi.insert(1, "Informatica")
        self.indirizzi.insert(3, "Biotecnologie")
        self.indirizzi.insert(2, "Economico")
        
        # combobox e variabili associate
        self.scelta = t.StringVar()
        self.sezioni= tt.Combobox(self.finestra, textvariable = self.scelta, width=3)
        self.sezioni["values"] = ["A", "B", "C", "D"]
        
        # pulsanti di controllo e variabili associate
        self.prom = t.StringVar()
        self.bocc = t.StringVar()
        promosso = t.Checkbutton(text="promosso", variable=self.prom)
        bocciato = t.Checkbutton(text="bocciato", variable= self.bocc)
        
        # posiziona i widget e li attacca alla finestra
        etichettaNome.grid(row=0,column=0, sticky="E", padx=5)
        nome.grid(row=0,column=1, sticky="W")
       
        frame.grid(row=0,column=0, padx=distanzaX, pady=distanzaY, columnspan=2)        
        self.indirizzi.grid(row=1,column=0, pady=distanzaY, padx=distanzaX, sticky="NW")
        self.sezioni.grid(row=1,column=1, pady=distanzaY, padx=distanzaX, sticky="NW")
        promosso.grid(row=3,column=0, sticky="W", padx=distanzaX)
        bocciato.grid(row=3,column=1, sticky="W")
        
        bocciato.deselect()

        pulsante.grid(row=3,column=2, sticky="S", padx=20)
        pulsante2.grid(row=4,column=2, sticky="S", padx=20)
        pulsante3.grid(row=5,column=2, sticky="S", padx=20)
         
        # avvia il ciclo
        self.finestra.mainloop()
        
    def stampaSezione(self):
        print(self.scelta.get())
        
    def stampaIndirizzo(self):
        selezione = self.indirizzi.curselection()
        for s in selezione:
            print(self.indirizzi.get(s))
            
    def click(self, event):
        print("click destro del mouse")


win = MyWindow()
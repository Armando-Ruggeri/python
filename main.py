import tkinter as tk


class MyWindow (tk.Tk):
    def __init__(self):
        super().__init__()
        self.resizable(False, False)
        w = self.winfo_screenwidth()
        h = self.winfo_screenheight()
        print(f"{w} {h}")
        w = int(w/2) - 140
        h = int(h/2) - 75
        self.title = "Login utente"
        dim = "280x150+" + str(w) + "+" + str(h)
        self.geometry(dim)

        # creazione frames
        self.usr = tk.Frame()
        self.pwd = tk.Frame()
        self.login = tk.Frame(pady=25)

        # creazione etichette
        self.etUser = tk.Label(self.usr, text="Username", width=9, anchor=tk.W)
        self.etPwd = tk.Label(self.pwd, text="Password", width=9, anchor=tk.W)

        # creazione caselle testo
        self.txtUsr = tk.Entry(self.usr, width=12)
        self.txtPwd = tk.Entry(self.pwd, width=12)

        # creazione pulsante
        self.butLogin = tk.Button(self.login, text="Login", width=15, command=self.go)

        # posizionamento widget in frames
        self.etUser.grid(row=0, column=0)
        self.txtUsr.grid(row=0, column=1)

        self.etPwd.grid(row=0, column=0)
        self.txtPwd.grid(row=0, column=1)
        self.butLogin.pack()

        # posizionamento frames
        self.usr.pack()
        self.pwd.pack()
        self.login.pack()

    def go(self):
        print("ok")

# avvio finestra
fin = MyWindow()
fin.mainloop()

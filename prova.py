import tkinter as tk

def stampa(*args):
    print(c.get())

f = tk.Tk()
c = tk.IntVar()
c.set(6)
c.trace("w", stampa)
e = tk.Entry( textvariable=c)
p = tk.Button(text="stampa")
e.pack()
p.pack()
f.mainloop()



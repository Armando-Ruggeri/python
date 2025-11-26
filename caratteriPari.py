parola = input("inserisci parola")

lungParola = len(parola)
caratteriPari = ""

for posizionePari in range(0, lungParola, 2):
    caratteriPari = caratteriPari + parola[posizionePari]
    
print("Caratteri pari: ", caratteriPari)
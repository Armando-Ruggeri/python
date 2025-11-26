parola = input("inserisci parola: ")
lungParola = len(parola)

palindroma = True
i = 0

while (palindroma == True) and (i < lungParola/2):
    if parola[i] != parola[lungParola - 1 - i]:
        palindroma = False
    else: 
        i = i + 1
        
print(palindroma)
        
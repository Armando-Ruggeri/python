num = int(input("Inserisci quantità di numeri "))
numPari = 0
numDispari = 0

for i in range (0, num):
    numero = num = int(input("Inserisci numero "))
    
    if numero % 2 == 0:
        numPari = numPari + 1
    else:
        numDispari = numDispari + 1
        
print (f"Ci sono {numPari} numeri pari e {numDispari} numeri dispari")
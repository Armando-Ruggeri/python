'''
restituisce il dizionario che rappresenta il social network
'''
def setup():
    socNetwork = dict()
    return socNetwork


'''
aggiunge un utente al social network

Parametri:
nomeUtente = nome dell'utente
socNet = dizionario che rappresenta il social netowork

'''
def aggiungiUtente (nomeUtente: str, socNet:dict):
    socNet[nomeUtente] = set()
    
'''
aggiunge un follower ad un utente

Parametri:
nomeUtente = nome dell'utente che concede l'amicizia
nomeFollower = nome dell'utente che chiede l'amicizia
socNet = dizionario che rappresenta tutti gli utenti del social network
'''
def aggiungiFollower(nomeUtente: str, nomeFollower: str, socNet: dict):
    listaUtenti = socNet.keys()
    if nomeFollower not in listaUtenti:
        aggiungiUtente(nomeFollower, socNet)
        
    # utente e follower si scambiano l'amicizia
    socNet[nomeUtente].add(nomeFollower)
    socNet[nomeFollower].add(nomeUtente)
    
   
'''
restituisce tutti gli amici diretti dei follower di un utente

Parametri:
nomeUtente = utente a cui suggerire nuovi amici
network = social netowork in cui cercarli
''' 
def suggerisciAmici (nomeUtente: str, network: dict)-> set:
    amiciDiretti = network[nomeUtente]
    
    amiciIndiretti = set()
    for amico in amiciDiretti:
        amiciIndiretti = amiciIndiretti. union(network[amico])
        
    return amiciIndiretti
    
'''
restituisce la lista degli amici comuni a due utenti su un social network

Parametri:
nomeUtente1 = primo utente
nomeUtente2 = secondo utente
socNet = il social network
'''
def getAmiciComuni(nomeUtente1: str, nomeUtente2: str, socNet: dict)-> list:
    # ottengo la lista delel chiavi (gli utenti)
    listaUtenti = socNet.keys()
    
    # verifico se gli utenti appartengono al social network
    if nomeUtente1 not in listaUtenti:
        print(f"{nomeUtente1} non è un utente del network")
        return []
    if nomeUtente2 not in listaUtenti:
        print(f"{nomeUtente2} non è un utente del network")
        return []
    
    # ottengo l'insieme degli amici comuni
    amiciComuni = socNet[nomeUtente1].intersection(socNet[nomeUtente2])
    
    # trasformo l'insieme in lista
    listaAmiciComuni = list(amiciComuni)
    return listaAmiciComuni
    
'''
banna un utente cancellandolo dal social ed eliminandolo dai follower di tutti gli utenti

Parametri:
nomeUtente = nome dell'utente da eliminare
social = social da cui eliminarlo
'''
def bannaUtente (nomeUtente: str, social: dict) -> None:
    # rimuove l'utente dal social
    social.pop(nomeUtente)
    
    # lo elimina dall'insieme dei follower di tutti gli utenti di cui lo è
    tuttiUtenti = social.keys()
    for utente in tuttiUtenti:
        if nomeUtente in social[nomeUtente]:
            social[nomeUtente].remove(nomeUtente)

    
"""
trova l'utente con più follower nel social network

Parametro:
social = network
"""
def calcolaUtenteMaxFollower(social)-> tuple[str, int]:
    maxFollower = 0
    nomeUtente = ""
    tuttiUtenti = social.keys()
    
    if social!= []:
        for utente in tuttiUtenti:
            numFollower = social[utente]
            if numFollower > maxFollower:
                maxFollower = numFollower
                nomeUtente = utente
    
    return nomeUtente, maxFollower
    
    
'''
visualizza tutti gli utenti del social network

Parametri:
socNetwork = il socialnetwork
'''
def visualizzaElencoUtenti(socNetwork: dict):
    # ottengo l'insieme degli amici comuni
    listaUtenti = socNetwork.keys()
    
    print("Il social ha i seguenti utenti: ")
    for utente in listaUtenti:
        print(utente, end=" ")
    
    print("\n-------------------------------")
    
    
def main():
    # creo il social
    social = setup()
    
    # iscrivo Andrea al social
    aggiungiUtente("Andrea", social)
    
    # aggiungo Pietro come follower di Andrea
    aggiungiFollower("Andrea", "Pietro", social)
    
    # aggiungo Hermann come follower di Andrea
    aggiungiFollower("Andrea", "Hermann", social)
    
    # aggiungo Filippo come follower di Andrea
    aggiungiFollower("Andrea", "Filippo", social)
    
    # aggiungo Filippo come follower di Pietro
    aggiungiFollower("Pietro", "Filippo", social)
    
    # visualizzo tutti i membri del social
    visualizzaElencoUtenti(social)
    
    # ottengo gli amici comuni di Andrea e Pietro
    amici = getAmiciComuni("Andrea", "Pietro", social)
    print(amici)
    
# programma effettivo
main()
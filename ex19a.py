#prova a fare tu una funzione
def calcolo_secondi (giorni, ore, secondi):
    print giorni, "corrispondono esattamente a", ore, "ore e", secondi, "secondi"

giorni= raw_input("Quanti giorni?")
ore= int(giorni)*24
secondi=int(ore)*60.0  

calcolo_secondi (giorni, ore, secondi)     
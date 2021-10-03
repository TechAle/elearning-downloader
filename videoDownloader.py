"""
    @Author TechAle
    @Since 03/10/21
"""
import os
import requests
import time


# Funzione principale
def download(link = "", timeSleep=1, inizio=1, retrySleep=10, tentativi=5):
    # Compongo il link
    temp = link.split("seg-")
    nTent = 0
    linkComposto = [temp[0] + "seg-", temp[1][temp[1].find("-"):]]

    # Se non esiste la cartella temp, creiala
    if not os.path.exists("temp"):
        os.makedirs("temp")

    # Iniziamo a scaricare
    while True:
        # Creiamo l'url e facciamo una richiesta
        url = linkComposto[0] + str(inizio) + linkComposto[1]
        r = requests.get(url)

        # Se successo
        if r.status_code == 200:
            # Scriviamo il risultato su file
            print("Scaricato " + str(inizio))
            open('temp/' + str(inizio) + '.ts', 'wb').write(r.content)
            inizio += 1
            time.sleep(timeSleep)
        else:
            # Se c'è stato un problema
            nTent += 1
            # 404 = file non trovato = abbiamo raggiunto la fine
            if r.status_code == 404:
                print("Probabilmente finito di scaricare")
                break

            # Se abbiamo fatti troppi tentativi, esci
            elif nTent > tentativi:
                print("Troppe richieste fallite")
                break
            else:
                # Aspetta prima di fare un altra richiesta
                print("Richiesta fallita, tentativo" + str(nTent) + "/" + str(tentativi))
                time.sleep(retrySleep)

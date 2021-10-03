"""
    @Author TechAle
    @Since 03/10/21
"""
from videoDownloader import *
from videoConcatenatore import *
import sys, getopt

'''
    -h -help
    -d -download [link]
    -c -concatena [input] [output]
    -f -frazioni [valore]
    -r -rimuovi si/no
    -s -start [valore]
    -t -tempo [valore]
'''
def help():
    print("Utilizzo: main.py [-h] [-d <link>] [-c <output>]\n"
          "[-f <numero>] [-r <si/no>] [-s <numero>] [-t <secondi>] [-i <nome>]\n\n"
          "Dettagli:\n"
          "\thelp\t\tGuida utilizzo dei parametri\n"
          "\tdownload\tLink del download\n"
          "\ttempo\t\tIn secondi quant'è l'attesa (potete usare .5) [default:1]\n"
          "\tstart\t\tPer il download, da quale file si inizia\n"
          "\tconcatena\tNome dell'output per la concatenazione\n"
          "\tinput\t\tNome input per la concatenazione"
          "\trimuovi\t\tSe lasciare o no i file usati per il concatenamento si/no [default: si]\n"
          "\tfrazioni\tIn quanti file sarà diviso il file finale. Warning: Più il numero è basso e più memoria si "
          "utilizzerà [10 default]")

# Voglio che venga eseguito solamente da main
if __name__ == "__main__":
    # Valori di default
    downloadLink = ""
    inizio = timeSleep = 1
    output = ""
    split = 10
    cancella = "si"
    inputDir = "temp/"
    # Esecuzione normale
    if len(sys.argv) == 1:
        while True:
            # Prendo la scelta
            scelta = int(input("1) Download e concatena\n"
                               "2) Download\n"
                               "3) Concatena\n"
                               "4) Quit\n"
                               "Choose: "))

            # Se stiamo facendo il download
            if scelta == 1 or scelta == 2:
                downloadLink = input("Nome: ")
                inizio = int(input("Inizio (1 se è la prima volta): "))
                timeSleep = float(input("Pausa (consigliato 1): "))

            # Se stiamo concatenando
            if scelta == 1 or scelta == 3:
                output = input("Nome output: ")
                split = int(input("Numero divisioni del video (meno memoria hai, più divisioni, consigliato 10): "))
                if scelta == 3:
                    inputDir = input("Directory Input: ")
                    cancella = input("Cancella: ")
                    cancella.lower()

            # Download + concatena
            if scelta == 1:
                download(downloadLink, timeSleep, inizio)
                concatena(output, split=split)
            # Download
            elif scelta == 2:
                download(downloadLink, timeSleep, inizio)
            # Concatena
            elif scelta == 3:
                concatena(output, inputDir, split, cancella)
                # Resetto
                inputDir = "temp/"
            # Esci
            elif scelta == 4:
                break
    else:
        # https://docs.python.org/3/library/getopt.html
        try:
            # Setup dei vari comandi
            opts, args = getopt.getopt(sys.argv[1:],
                                       "h:d:c:f:r:s:t:i:",
                                       [])
        except getopt.GetoptError as err:
            print(err)
            help()
            sys.exit(2)

        # Inizio
        startDownload = startConcatenazione = False
        for o, a in opts:
            if len(a) > 0 and a[0] == '=':
                a = a[1:]
            if o in ("-h", "--help"):
                help()
                sys.exit()
            elif o in ("-d", "--download"):
                downloadLink = a
                startDownload = True
            elif o in ("-c", "--concatena"):
                output = a
                startConcatenazione = True
            elif o in ("-i", "--input"):
                inputDir = a
            elif o in ("-f", "--frazioni"):
                split = int(a)
            elif o in ("-r", "--rimuovi"):
                if a.lower() == "no":
                    a = "no"
            elif o in ("-s", "--start"):
                inizio = int(a)
            elif o in ("-t", "--tempo"):
                timeSleep = float(a)

        # Iniziamo il download
        if startDownload:
            download(downloadLink, timeSleep, inizio)

        # Iniziamo la concatenazione
        if startConcatenazione:
            concatena(output, inputDir, split, cancella)


#Elearning downloader
Questa applicazione scritta in python permette di scaricare i video che sono stati caricati sulla piattaforma elearning.<br>
## Perchè?
Trovo più comodo potere visualizzare in locale/offline le lezioni e, siccome elearning non ha un opzione per scaricare le varie lezioni, me lo sono dovuto creare da solo.<br>
## Come utilizzarlo
1) Installare python 3.9
2) Scaricare la repository
3) pip install requirements.txt
4) Andare sul link della lezione che vuoi scaricare, tasto destro ispeziona elemento, in alto a destra cliccare "Rete" (Firefox) avviate il video e cercate un pacchetto che contiene, come file, il nome "seg". Cliccatelo, copiate il link

Qui, o avviate il file main.py normalmente con python main.py (in talcaso, tutto sarà guidato), oppure potete eseguire "python main.py -h".<br>
<br>Esempi comandi cli:
- python main.py -c=prova -f=15 -r=si -i=temp/
- python main.py -d=LINK -t=.7 -s=1
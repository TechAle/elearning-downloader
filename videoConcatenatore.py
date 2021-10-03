"""
    @Author TechAle
    @Since 03/10/21
"""
import os
from moviepy.editor import VideoFileClip, concatenate_videoclips, CompositeVideoClip
import re

## Funzione per l'ordinamento dei file
# https://stackoverflow.com/questions/5997006/sort-a-list-of-files-using-python
digits = re.compile(r'(\d+)')
def tokenize(filename):
    return tuple(int(token) if match else token
                 for token, match in
                 ((fragment, digits.search(fragment))
                  for fragment in digits.split(filename)))

# Funzione per la divisione di una lista
def split_list(alist, wanted_parts=1):
    length = len(alist)
    return [alist[i * length // wanted_parts: (i + 1) * length // wanted_parts]
            for i in range(wanted_parts)]


# Funzione principale
def concatena(nomeOutput, directoryInput="temp/", split=10, cancella="si"):
    # Aggiungiamo / alla fine di directoryInput se non c'è
    directoryInput += '' if directoryInput[-1] == '/' else '/'

    # Se l'input non esiste, esci
    if not os.path.exists(directoryInput):
        print("Directory input non trovata")
        return

    # Se output non esiste, esci
    if not os.path.exists("output"):
        os.makedirs("output")

    # Prendi tutti i file e ordinali
    files = [directoryInput + x for x in os.listdir(directoryInput) if x.endswith(".ts")]
    files.sort(key=tokenize)

    # Dividili
    groups = split_list(files, split)

    # per ogni gruppo di file
    for i in range(split):
        # Inizia l'elaborazione
        print("Elaborazione " + str(i) + "/" + str(split))
        # Crea mini file per poi metterli insieme
        clips = [VideoFileClip(x) for x in groups[i]]
        final_cip = concatenate_videoclips(clips)

        # Output
        final_cip.write_videofile("output/" + nomeOutput + str(i) + ".mp4")

    # Se dobbiamo cancellare i mini file
    if cancella == "si":
        for group in groups:
            for file in group:
                os.remove(directoryInput + file)

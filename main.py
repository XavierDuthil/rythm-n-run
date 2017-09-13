from record import recordImpulses
from parseRecord import parseRecord
from evaluateLibrary import evaluateLibrary
import subprocess
import random
import os
import re

if __name__ == '__main__':
    LIBRARY = "/home/pi/music/"
    ANALYSE_FILE = "{0}Analyse.mp3".format(LIBRARY)
    firstPlay = True
    lastSelectedBpm = 0

    # Analyse the unevaluated audio files
    evaluateLibrary()

    # Play "analyse en cours"
    if os.path.isfile(ANALYSE_FILE):
        command = "cmus-remote -q {0}".format(ANALYSE_FILE)
        subprocess.call(command.split(), shell=False)
        subprocess.call(["cmus-remote", "-n"])
        subprocess.call(["cmus-remote", "-p"])
        firstPlay = False

    # Main progam loop
    while True:
        # Record impulses
        record = recordImpulses()
        bpm = parseRecord(record)
        print("bpm : {0}".format(bpm))
        if bpm < 60 or bpm > 250:
            print("Bad value")
            continue

        # Execute until a playable file is found
        musicFound = False
        availableMusics = []
        selectedFolder = ""
        while not musicFound:
            # Scan the music folders as bpm values
            library = []
            folders = os.listdir(LIBRARY)
            for folder in folders:
                if re.match("^\d+$", folder):
                    library.append(float(folder))

            # If library is empty
            if not library:
                print("Library is empty !\nProgram exiting")
                exit()

            # Select the closest bpm value
            closestBpmInLibrary = int(min(library, key=lambda x:abs(x-bpm)))
            selectedFolder = "{0}{1}/".format(LIBRARY, closestBpmInLibrary)

            # Remove the folder if empty
            availableMusics = os.listdir(selectedFolder)
            if not availableMusics:
                os.remove(selectedFolder)
                continue

            # If same rythm, don't interrupt music
            if closestBpmInLibrary == lastSelectedBpm:
                print("Keeping current title")
                continue

            musicFound = True

        # Select a random audio file in the folder
        music = random.choice(availableMusics)

        # Send the file to the player
        command = "cmus-remote -q {0}{1}".format(selectedFolder, music)
        subprocess.call(command.split(), shell=False)
        subprocess.call(["cmus-remote", "-n"])

        # Send command "play"
        #if firstPlay:
        #   subprocess.call(["cmus-remote", "-p"])
        #   firstPlay = False

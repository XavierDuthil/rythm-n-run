import subprocess
import os
import re

LIBRARY = "/home/pi/music/"
UNEVALUATED_FOLDER = LIBRARY + "unevaluated/"
audioFiles = [
    re.compile(".+\.mp3$"),
    re.compile(".+\.ogg$"),
    re.compile(".+\.m4a$"),
    re.compile(".+\.flac$")
]


def evaluateLibrary():
    unevaluatedFiles = os.listdir(UNEVALUATED_FOLDER)
    for fileName in unevaluatedFiles:
        # Only process if known audio file
        knownFile = False
        for audioFile in audioFiles:
            if audioFile.match(fileName):
                knownFile = True
                break
        if not knownFile:
            continue

        fileFullPath = UNEVALUATED_FOLDER + fileName
        print("Evaluating {0}...".format(fileName))
        fileBpm = subprocess.Popen(["bpm-tag", "-n", fileFullPath], stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()[0]

        # Create the folder associated to this bpm value if it doesn't exist (rounded to 5)
        scaledBpm = int(3 * round(float(fileBpm) / 3))

        destinationFolder = "{0}{1}/".format(LIBRARY, scaledBpm)
        if not os.path.exists(destinationFolder):
            os.makedirs(destinationFolder)

        os.rename(UNEVALUATED_FOLDER + fileName, destinationFolder + fileName)
        print("Placed in folder {0}".format(destinationFolder))


if __name__ == '__main__':
    evaluateLibrary()

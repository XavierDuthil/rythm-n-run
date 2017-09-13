import adxl345
from time import sleep, time


def recordImpulses():
    accel = adxl345.ADXL345()
    accel.setRange(adxl345.RANGE_8G)

    # xFile = open('result/xRecording', 'w')
    # yFile = open('result/yRecording', 'w')
    # zFile = open('result/zRecording', 'w')
    recordingFile = open('result/recording', 'w')

    # lastTime = time()
    # startTime = int(lastTime*1000)

    startTime = time()

    records = []
    correspondingTimes = []
    print("Recording...")

    for i in range(2000):
        axes = accel.getAxes(True)
        x = axes['x']
        y = axes['y']
        z = axes['z']

        currentTime = time()
        # timePassed = currentTime - lastTime
        # lastTime = currentTime
        timePassed = currentTime - startTime

        addedPerturbation = abs(x) + abs(y) + abs(z)
        records.append(addedPerturbation)
        correspondingTimes.append(timePassed)

        recordingFile.write("{0}\n".format(addedPerturbation))

        sleep(0.003)

    return records, correspondingTimes

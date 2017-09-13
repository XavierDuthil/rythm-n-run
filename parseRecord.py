def parseRecord(recordsWithTimesTuple):
    filterSize = 3
    passNext = 0
    records = recordsWithTimesTuple[0]
    correspondingTimes = recordsWithTimesTuple[1]
    peaks = []

    for i in range(filterSize, len(records) - filterSize):
        if passNext > 0:
            passNext -= 1
            continue

        val = records[i]
        consideredValues = []
        for j in range(i - filterSize, i + filterSize + 1):
            consideredValues.append(records[j])

        average = sum(consideredValues) / float(len(consideredValues))

        # Get median value
        # middleIndex = int(filterSize / 2 + 0.5)
        # consideredValues.sort()
        # median = consideredValues[middleIndex]
        # print("value :{0}".format(val))
        # print("median :{0}".format(median))

        if val > average * 2:
            passNext = filterSize
            peaks.append(correspondingTimes[i])

    if len(peaks) < 3:
        return 0
    return getBpm(peaks)


def getBpm(peaks):
    intervals = []
    for i in range(1, len(peaks)):
        intervals.append(peaks[i] - peaks[i - 1])

    intervals.sort()
    extremValues = len(intervals) / 4
    startValue = extremValues
    endValue = len(intervals) - extremValues

    keptIntervals = intervals[startValue:endValue]
    average = sum(keptIntervals) / float(len(keptIntervals))
    bpm = (1 / average) * 60
    return bpm

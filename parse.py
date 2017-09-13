data = []
recordFile = open('recording', 'r')

for line in recordFile:
    data.append(float(line))

totalRecords = len(data)
for index, val in enumerate(data):
    if index < 5 | index > totalRecords - 5:
        continue

    max = 0
    maxIndex = 0
    for subIndex, subVal in enumerate(data[index - 5:index + 5]):
        if subVal > max:
            max = subVal
            maxIndex = subIndex

    data[index] = 0
    data[index + (maxIndex - 5)] += val

for line in data:
    print(line)

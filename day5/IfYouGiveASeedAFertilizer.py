import sys

def mapSourceToDestination(sources, destStart, sourceStart, span, map):
    for source in sources:
        if source >= sourceStart and source < sourceStart + span:
            map[source] = source + (destStart - sourceStart)
        elif source not in map.keys():
            map[source] = source

def partOne(lines, seeds):
    seedToSoil = {}
    soilToFertilizer = {}
    fertilizerToWater = {}
    waterToLight = {}
    lightToTemperature = {}
    temperatureToHumidity = {}
    humidityToLocation = {}
    lineNbr = 0
    while lines[lineNbr] != '':
        soilStart, seedStart, span = [int(val) for val in lines[lineNbr].split()]
        mapSourceToDestination(seeds, soilStart, seedStart, span, seedToSoil)
        lineNbr += 1
    lineNbr += 2

    while lines[lineNbr] != '':
        fertStart, soilStart, span = [int(val) for val in lines[lineNbr].split()]
        mapSourceToDestination(seedToSoil.values(), fertStart, soilStart, span, soilToFertilizer)
        lineNbr += 1
    lineNbr += 2

    while lines[lineNbr] != '':
        waterStart, fertStart, span = [int(val) for val in lines[lineNbr].split()]
        mapSourceToDestination(soilToFertilizer.values(), waterStart, fertStart, span, fertilizerToWater)
        lineNbr += 1
    lineNbr += 2

    while lines[lineNbr] != '':
        lightStart, waterStart, span = [int(val) for val in lines[lineNbr].split()]
        mapSourceToDestination(fertilizerToWater.values(), lightStart, waterStart, span, waterToLight)
        lineNbr += 1
    lineNbr += 2

    while lines[lineNbr] != '':
        tempStart, lightStart, span = [int(val) for val in lines[lineNbr].split()]
        mapSourceToDestination(waterToLight.values(), tempStart, lightStart, span, lightToTemperature)
        lineNbr += 1
    lineNbr += 2

    while lines[lineNbr] != '':
        humidityStart, tempStart, span = [int(val) for val in lines[lineNbr].split()]
        mapSourceToDestination(lightToTemperature.values(), humidityStart, tempStart, span, temperatureToHumidity)
        lineNbr += 1
    lineNbr += 2

    while lineNbr < len(lines) and lines[lineNbr] != '':
        locationStart, humidityStart, span = [int(val) for val in lines[lineNbr].split()]
        mapSourceToDestination(temperatureToHumidity.values(), locationStart, humidityStart, span, humidityToLocation)
        lineNbr += 1

    print('Lowest location number corresponding to starting seeds: ' + str(min(humidityToLocation.values())))


def updateSpans(spans, lineNbr, lines):
    newSpans = []
    while lineNbr < len(lines) and lines[lineNbr] != '':
        unusedSpans = []
        nextStart, oldStart, chunk = [int(val) for val in lines[lineNbr].split()]
        oldStop = oldStart + chunk - 1
        offset = nextStart - oldStart
        while (len(spans)):
            span = spans.pop(0)
            if oldStart <= min(span) and oldStop >= max(span):                              # whole span
                newSpans.append((min(span) + offset, max(span) + offset))
            elif oldStart <= min(span) and oldStop >= min(span) and oldStop <= max(span):   # beginning of span
                newSpans.append((min(span) + offset, oldStop + offset))
                unusedSpans.append((oldStop + 1, max(span)))
            elif oldStart >= min(span) and oldStart <= max(span) and oldStop >= max(span):  # end of span
                newSpans.append((oldStart + offset, max(span) + offset))
                unusedSpans.append((min(span), oldStart - 1))
            elif oldStart >= min(span) and oldStop <= max(span):                            # middle of span
                newSpans.append((oldStart + offset, oldStop + offset))
                unusedSpans.append((min(span), oldStart - 1))
                unusedSpans.append((oldStop + 1, max(span)))
            else:                                                                           #  no match    
                unusedSpans.append(span)
        spans = unusedSpans
        lineNbr += 1
    lineNbr += 2
    for span in unusedSpans:
        newSpans.append(span)
    return newSpans, lineNbr


def partTwo(lines, seedsInput):
    spans = []
    totalMin = sys.maxsize
    for i in range(0, len(seedsInput), 2):
        spans.append((seedsInput[i], seedsInput[i] + seedsInput[i + 1] - 1))

    lineNbr = 0

    print('SeedToSoil')
    spans, lineNbr = updateSpans(spans, lineNbr, lines)

    print('SoilToFert')
    spans, lineNbr = updateSpans(spans, lineNbr, lines)

    print('fertToWater')
    spans, lineNbr = updateSpans(spans, lineNbr, lines)

    print('waterToLight')
    spans, lineNbr = updateSpans(spans, lineNbr, lines)

    print('lightToTemp')
    spans, lineNbr = updateSpans(spans, lineNbr, lines)

    print('tempToHumidity')
    spans, lineNbr = updateSpans(spans, lineNbr, lines)

    print('humidityToLoc')
    spans, lineNbr = updateSpans(spans, lineNbr, lines)

    minVal = sys.maxsize
    for span in spans:
        val = min(span)
        if val < minVal:
            minVal = val

    print('Lowest location number corresponding to starting seed spans: ' + str(minVal))

if __name__ == '__main__':
    with open('day5/input.txt') as f:
        lines = [line.strip() for line in f]
    
    seeds = [int(val) for val in lines[0].split()[1:]]
    lines = lines[3:]

    partOne(lines, seeds)
    partTwo(lines, seeds)





def mapSourceToDestination(sources, destStart, sourceStart, span, map):
    for source in sources:
        if source >= sourceStart and source <= sourceStart + span:
            map[source] = source + (destStart - sourceStart)
        elif source not in map.keys():
            map[source] = source

if __name__ == '__main__':
    with open('day5/input.txt') as f:
        lines = [line.strip() for line in f]
    
    seeds = [int(val) for val in lines[0].split()[1:]]
    lines = lines[3:]

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


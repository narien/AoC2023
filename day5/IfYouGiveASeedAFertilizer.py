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

def partTwo(lines, seedsInput):
    seeds = []
    totalMin = sys.maxsize
    for i in range(0, len(seedsInput), 2):
        seeds = list(range(seedsInput[i], seedsInput[i] + seedsInput[i + 1], 1))

        seedToSoil = {}
        soilToFertilizer = {}
        fertilizerToWater = {}
        waterToLight = {}
        lightToTemperature = {}
        temperatureToHumidity = {}
        humidityToLocation = {}
        lineNbr = 0
        print('mapping to soil')
        while lines[lineNbr] != '':
            soilStart, seedStart, span = [int(val) for val in lines[lineNbr].split()]
            mapSourceToDestination(seeds, soilStart, seedStart, span, seedToSoil)
            lineNbr += 1
        lineNbr += 2

        print('mapping to fert')
        while lines[lineNbr] != '':
            fertStart, soilStart, span = [int(val) for val in lines[lineNbr].split()]
            mapSourceToDestination(seedToSoil.values(), fertStart, soilStart, span, soilToFertilizer)
            lineNbr += 1
        lineNbr += 2

        print('mapping to water')
        while lines[lineNbr] != '':
            waterStart, fertStart, span = [int(val) for val in lines[lineNbr].split()]
            mapSourceToDestination(soilToFertilizer.values(), waterStart, fertStart, span, fertilizerToWater)
            lineNbr += 1
        lineNbr += 2

        print('mapping to light')
        while lines[lineNbr] != '':
            lightStart, waterStart, span = [int(val) for val in lines[lineNbr].split()]
            mapSourceToDestination(fertilizerToWater.values(), lightStart, waterStart, span, waterToLight)
            lineNbr += 1
        lineNbr += 2

        print('mapping to temp')
        while lines[lineNbr] != '':
            tempStart, lightStart, span = [int(val) for val in lines[lineNbr].split()]
            mapSourceToDestination(waterToLight.values(), tempStart, lightStart, span, lightToTemperature)
            lineNbr += 1
        lineNbr += 2

        print('mapping to humidity')
        while lines[lineNbr] != '':
            humidityStart, tempStart, span = [int(val) for val in lines[lineNbr].split()]
            mapSourceToDestination(lightToTemperature.values(), humidityStart, tempStart, span, temperatureToHumidity)
            lineNbr += 1
        lineNbr += 2

        print('mapping to location')
        while lineNbr < len(lines) and lines[lineNbr] != '':
            locationStart, humidityStart, span = [int(val) for val in lines[lineNbr].split()]
            mapSourceToDestination(temperatureToHumidity.values(), locationStart, humidityStart, span, humidityToLocation)
            lineNbr += 1
        currentMin = min(humidityToLocation.values())
        totalMin = min(currentMin, totalMin)

        print('Lowest location number corresponding to starting seed spans: ' + str(totalMin))

if __name__ == '__main__':
    with open('day5/input.txt') as f:
        lines = [line.strip() for line in f]
    
    seeds = [int(val) for val in lines[0].split()[1:]]
    lines = lines[3:]

    partOne(lines, seeds)
    partTwo(lines, seeds)




import re

def sumVals(lines):
    total = 0
    for line in lines:
        l = [s for s in line if s.isdigit()]
        total += int(l[0] + l.pop())
    return total

def sumTextAndDigits(lines):
    converter = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    total = 0

    for line in lines:
        matches = re.finditer(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
        results = [str(match.group(1)) for match in matches]
        first = converter[results[0]] if results[0] in converter.keys() else results[0]
        last = converter[results[-1]] if results[-1] in converter.keys() else results[-1]
        total += int(first + last)
    return total

if __name__ == '__main__':
    with open('day1/input.txt') as f:
        lines = [val.strip() for val in f]
    print('P1 calibration value: ' + str(sumVals(lines)))
    print('P2 calibration value: ' + str(sumTextAndDigits(lines)))
from itertools import cycle

output = 0
listOfFrequencies = []

with open('..//input.txt', 'r') as f:
    lineList = f.readlines()
    
# need to look into how to optimize

running = True
lineListCycle = cycle(lineList)
# Prime the pump
nextelem = next(lineListCycle)
while running:
    thiselem, nextelem = nextelem, next(lineListCycle)
    output += int(thiselem)

    if output in listOfFrequencies:
        break

    listOfFrequencies.append(output)

print(output)
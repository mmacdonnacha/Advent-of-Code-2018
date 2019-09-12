output = 0

with open('..//input.txt', 'r') as input:
    for line in input.readlines():
        # print(line)

        output += int(line)

print(output)

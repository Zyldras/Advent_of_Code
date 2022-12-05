##### DAY 1 #####

def part1 (lineTab):
    count = 0
    max = 0

    for line in lineTab:
        if line == '':
            if count > max:
                max = count
            count = 0
        else:
            count += int(line)
        
    print(max)

def part2 (lineTab):
    count = 0
    max = 0

    for line in lineTab:
        if line == '':
            if count > max:
                max = count
            count = 0
        else:
            count += int(line)
        
    print(max)


##### MAIN #####

file = open("input.txt", "r")

lineTab = file.read().splitlines()

# part1(lineTab)
part2(lineTab)

file.close()

##### MAIN #####
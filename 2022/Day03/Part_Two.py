f = open("input.txt", "r")
line = f.readline()
total = 0
while line :
    uno = line[:len(line)]
    line = f.readline()
    dos = line[:len(line)]
    line = f.readline()
    tres = line[:len(line)]
    item = ""
    '''
    for j in line :
        uno += j
    line = f.readline()
    for j in line :
        dos += j
    line = f.readline()
    for j in line :
        tres += j
    '''
    for j in uno :
        if j in dos :
            if j in tres and j not in item :
                item += j
                if ord(j) > 64 and ord(j) < 91 :
                    total += ord(j) - 38
                elif ord(j) > 96 and ord(j) < 123 :
                    total += ord(j) - 96
    line = f.readline()
print("Total =", total)
f.close

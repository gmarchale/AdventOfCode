f = open("input.txt", "r")
total = 0
line = f.readline()
while line:
    j = 0
    premierSac = line[:len(line)//2]
    secondSac = line[len(line)//2:]
    item = ""
    for j in premierSac :
        for k in secondSac :
            if j == k and j not in item :
                if ord(j) > 64 and ord(j) < 91 :
                    total += ord(j) - 38
                elif ord(j) > 96 and ord(j) < 123 :
                    total += ord(j) - 96
                item += j
    line = f.readline()
print("Total =", total)
f.close()

f = open("input.txt", "r")
rock = 1
paper = 2
scissors = 3
somme = 0

i = f.readline()
while i:
    if i[0] == "A":
        if i[2] == "X":
            somme += 3
        elif i[2] == "Y":
            somme += 4
        elif i[2] == "Z":
            somme += 8
    elif i[0] == "B":
        if i[2] == "X":
            somme += 1
        elif i[2] == "Y":
            somme += 5
        elif i[2] == "Z":
            somme += 9
    elif i[0] == "C":
        if i[2] == "X":
            somme += 2
        elif i[2] == "Y":
            somme += 6
        elif i[2] == "Z":
            somme += 7
    i = f.readline()
f.close()
print("Part Two :", somme)

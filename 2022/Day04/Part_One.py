import re

f = open("input.txt", "r")
total = 0
line = f.readlines()
for i in line:
    liste = re.findall(r'\d+', i)
    if int(liste[0]) <= int(liste[2]) and int(liste[1]) >= int(liste[3]) :
        total += 1
    elif int(liste[0]) >= int(liste[2]) and int(liste[1]) <= int(liste[3]) :
        total += 1
print("Total =", total)

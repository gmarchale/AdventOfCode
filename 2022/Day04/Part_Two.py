import re

f = open("input.txt", "r")
total = 0
line = f.readlines()
for i in line:
    liste = re.findall(r'\d+', i)
    liste1 = [x for x in range(int(liste[0]), int(liste[1]) + 1)]
    liste2 = [x for x in range(int(liste[2]), int(liste[3]) + 1)]
    stop = 0
    #for x in range(int(liste[0]), int(liste[1]) + 1) :
     #   liste1.append(x)
    #for x in range(int(liste[2]), int(liste[3]) + 1) :
     #   liste2.append(x)
    for y in liste1 :
        if y in liste2 and stop == 0:
            total += 1
            stop = 1
print("Total =", total)

f = open("input.txt", "r")
max1 = 0
max2 = 0
max3= 0
sum = 0

i = f.readline()
while i:
    if i != "\n":
        sum += int(i)
    else :
        if sum > max3:
            if sum > max2:
                if sum > max1:
                    max3= max2
                    max2 = max1
                    max1 = sum
                else:
                    max3 = max2
                    max2 = sum
            else:
                max3 = sum
        sum = 0
    i = f.readline()
f.close()
print("1er = ",max1)
print("2eme = ",max2)
print("3eme = ",max3)

total = max1 + max2 + max3
print("Total des 3 premiers = ",total)

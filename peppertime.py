n = int(input())
totalHeat = 0
for i in range(n):
    pepper = input() #not int, just word
    if(pepper == "Poblano"):
        totalheat = totalHeat + 1500
    elif(pepper == "Mirasol"):
        totalHeat = totalHeat + 6000
    elif(pepper == "Serrano"):
        totalHeat = totalHeat + 15500
    elif(pepper == "Cayenne"):
        totalHeat = totalHeat + 40000
    elif(pepper == "Thai"):
        totalHeat = totalHeat + 75000
    else:
        totalHeat = totalHeat + 125000

print(totalHeat)
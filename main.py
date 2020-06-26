import random

a = "Welkom bij galgje"
print(a)
b = 'De regels:'
print(b)

lijst = ["-maximaal vijf keer raden","-een letter per beurt"]
for item in lijst:
 print(item)
 
counter = 0
compwoordenlist = ["informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk"]                        
hetwoord = random.choice(compwoordenlist)
lengtewoord = len(hetwoord)
temp = "." * lengtewoord

print("het woord heeft " + str(lengtewoord) + " letters")







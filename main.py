aimport random
import re

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
i = input()
print(i)


while True:
  userguess = (input(": "))
  match = re.search(userguess, hetwoord)
  if userguess == hetwoord: #als je het woord heb geraden
    print('je heb het woord ' + '"' + hetwoord + '"' + " geraden")
    break
  




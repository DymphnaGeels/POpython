import random
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

  elif match: #goed geraden letter
    print("Goed geraden")
    for i in range(0, lengtewoord):
      if userguess == hetwoord[i]:
        temp = temp[:i] + userguess +temp[i+1:]
    print(temp)
        
  else: # fout gereaden
    print("nee geen match")
    counter = counter + 1
    if counter == 1:
      print("""  
     |
     |
     |
     |
     |
_____|""")
    elif counter == 2:
           print("""  ____
     |
     |
     |
     |
     |
_____|""")
    elif counter == 3:
            print("""  ____
    \|
     |
     |
     |
     |
_____|""")
    elif counter == 4:
      print("""  ____
  | \|
     |
     |
     |
     |
_____|""")
    elif counter == 5:
      print("""  ____
  | \|
  0  |
     |
     |
     |
_____|""")
    elif counter == 6:
      print("""  ____
  | \|
  0  |
  |  |
     |
     |
_____|""")
    elif counter == 7:
      print("""  ____
  | \|
  0  |
 /|  |
     |
     |
_____|""")
    elif counter == 8:
      print("""  ____
  | \|
  0  |
 /|\ |
     |
     |
_____|""")
    elif counter == 9:
      print("""  ____
  | \|
  0  |
 -|- |
 /   |
     |
_____|""")
    elif counter ==10:
      print("Helaas, je bent dood")
      print("""  ____
  | \|
  0  |
 -|- |
 / \ |
     |
_____|""")
      print('het woord was ' + '"' + hetwoord + '"')
      break
    else:
     pass






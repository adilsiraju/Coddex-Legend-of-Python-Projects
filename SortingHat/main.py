# The Sorting Hat game

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0


q1 = ''' Do you like Dawn or Dusk?:\n(1) Dawn | (2) Dusk\n'''
q2 = '''When I’m dead, I want people to remember me as:\n(1) The Good | (2) The Great\n(3) The Wise | (4) The Bold\n'''
q3 = '''Which kind of instrument most pleases your ear?\n(1) The violin | (2) The trumpet\n(3) The piano | (4) The drum\n'''

s1 = int(input(q1))

if s1 > 2:
  print("Wrong input.")
if s1 == 1:
   Gryffindor +=1
   Ravenclaw +=1

s2 = int(input(q2))
if s2 == 1:
   Hufflepuff +=2
elif s2 == 2:
   Slytherin +=2
elif s2 == 3:
   Ravenclaw +=2
elif s2 == 4:
   Gryffindor +=2
else:
  print("Wrong input.")

s3 = int(input(q3))
if s3 == 1:
   Hufflepuff +=4
elif s3 == 2:
   Slytherin +=4
elif s3 == 3:
   Ravenclaw +=4
elif s3 == 4:
   Gryffindor +=4
else:
  print("Wrong input.")

print('Total Score:\n🐍 Slytherin :' + str(Slytherin)+ '\t🦡 Hufflepuff : ' + str(Hufflepuff) + '\n🦅 Ravenclaw : ' + str(Ravenclaw) + '\t🦁 Gryffindor : ' + str(Gryffindor))
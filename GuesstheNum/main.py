guess = 0
tries = 0

while guess != 6:
  guess = int(input("Guess the number:  "))
  tries +=1
  if tries == 6:
    print("You've exhausted your tries")

print("You got it!")
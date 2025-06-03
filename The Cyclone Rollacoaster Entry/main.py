# height requirement is 137 cm and the cost is 10 credits)

height = int(input('Enter height: '))
credits = int(input('Enter credits: '))

if height >= 137 and credits >= 10:
  print("Enjoy the ride!")
elif height < 137 and credits >= 10:
  print("You are not tall enough to ride.")
elif height >= 137 and credits < 10:
  print("You don't have enough credits.")
else:
  print("You haven't met either requirement.")
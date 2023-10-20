def movie_tickets():
  # P3
  age = int(input("What is your age? "))
  if age > 60:
    print("Your ticket is $10")
  elif age >= 13 and age < 60:
    print("Your ticket is $12")
  elif age >= 5 and age < 13:
    print("Your ticket is $8")
  elif age < 5:
    print("Your ticket is free!")
  else:
    print("Please enter a valid age.")
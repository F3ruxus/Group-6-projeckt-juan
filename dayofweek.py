def p6():
  #P6
  day=input("what day is it today?").lower()
  if day=="saturday" or day=="sunday":
    print("It's the weekend.")
  elif day=="monday" or day=="tuesday" or day=="wednesday" or day=="thursday" or day=="friday":
    print("It's a weekday.")
  else:
    print("invalid input")
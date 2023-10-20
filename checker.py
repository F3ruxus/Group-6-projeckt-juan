def password_checker():
  #P9 
  password = input("Enter a password: ").lower()
  length = len(password)
  # data_type = str(type(password))
  # print(data_type == "<class 'str'>")
  # print(data_type)
  if length < 6:
    print("Password too short")
  elif password.isalpha():
    print("Moderate password")
  elif password.isdigit():
    print("Weak password")
  else:
    print("Your password is strong!")
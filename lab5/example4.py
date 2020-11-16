password = "abc123"
i = 0

while True:
  userPass = input("Enter password: ")

  if userPass == password:
    print("Welcome")
    break
  
  elif userPass == "help":
    print(password[i])
    i += 1
  
  else:
    print("Wrong")
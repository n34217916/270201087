mail_adress = input("Enter the email adress: ")
mailA = mail_adress.lower()

before = mailA.split("@")[0]
after = mailA.split("@")[1]
before = before.lower()
after = after.lower()

if after == "example.com":
  before = before.replace(".", "")
  if before == "ceng113":
    print("Mail adress is correct.")
  else:
    print("Mail adress is not correct.")
else:
  print("Mail adress is not correct.")
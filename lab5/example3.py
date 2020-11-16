num1 = int(input("Enter an integer: "))
num2 = int(input("Enter an integer: "))

match = 0
while True:
  if num1 % 10 == num2 % 10:
    match += 1
  num1 = num1 // 10
  num2 = num2 // 10
  
  if num1 == 0 or num2 == 0:
    break

print(match)
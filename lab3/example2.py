print("You will enter three numbers.. Let's begin..")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1 <= num2 and num1 <= num3 :
  minimum = num1
elif num2 <= num3 :
  minimum = num2
else :
  minimum = num3

print("Minimum of the entered numbers is ", minimum)


n = int(input("Enter an integer: "))

factorial = 1

for i in range(1, n+1):
  factorial *= i
print("Factorial of the integer is", factorial)
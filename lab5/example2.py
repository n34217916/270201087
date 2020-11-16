n = int(input("Enter how many integers you would like to enter: "))
evens = 0
for i in range (n):
  num = int(input("Enter an integer: "))
  if num % 2 == 0:
    evens += 1

result = (evens / n) * 100
print(result)
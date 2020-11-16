num = int(input("Please enter an integer: "))
if num > 10:
  d1 = num % 10
  d2 = (num % 100) // 10
  sum_of_digits = (d1+d2) / 2
else:
  sum_of_digits = num
print("Sum of the last two digits of entered integer is ", sum_of_digits)
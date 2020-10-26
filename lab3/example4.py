age = int(input("Enter your age: "))

if age > 60 or age < 6 :
  t_price = "free!"

elif age <= 18 and age >= 6 :
  t_price = "1.5 tl"

else :
  t_price = "3 tl"

print("Your ticket is", t_price)
  
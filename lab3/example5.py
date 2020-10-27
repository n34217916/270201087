month = int(input("Please enter the number of the month: "))
day = int(input("Please enter the day: "))

if month == 3 :
  if day >= 20 :
      season = "spring"
  else :
    season = "winter"
elif month == 4 or month == 5 :
  season = "spring"
elif month == 6 :
  if day >= 21 :
    season = "summer"
  else :
    season = "spring"
elif month == 7 or month == 8 :
  season = "summer"
elif month == 9 :
  if day >= 22 :
    season = "fall"
  else :
    season = "summer"
elif month == 10 or month == 11 :
  season = "fall"
elif month == 12 :
  if day >= 21 :
    season = "winter"
  else :
    season = "fall"
elif month == 1 or month == 2 :
  season = "winter"
else :
  print("Invalid date or month")

print("The season of the entered date is", season, ".")
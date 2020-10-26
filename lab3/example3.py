numLectures = int(input("Enter the number of lectures: "))
gpa = float(input("Enter the GPA: "))

if numLectures < 47 and gpa < 2 :
  ans = "Not enough number of lectures and GPA!"
  
elif numLectures < 47 and gpa >= 2 :
  ans = "Not enough number of lectures!"

elif numLectures >= 47 and gpa < 2 :
  ans = "Not enough GPA!"

else:
  ans = "Graduated!"

print(ans)
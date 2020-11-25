range__ = int(input("How many students' grades would you like to calculate? "))
all_grades = []
for i in range(0,range__):
  one_s_grades = input("Enter the grades separated by space: ")
  grade_list = one_s_grades.split(" ")
  m1 = int(grade_list[0])
  m2 = int(grade_list[1])
  final = int(grade_list[2])
  grade = (m1/100*30) + (m2/100*30) + (final/100*40)
  all_grades.append(grade)

print(all_grades)
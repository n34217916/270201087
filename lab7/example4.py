e_dict = {}
for i in range(5):
  e_name = input("Enter the name of employee: ")
  e_salary = int(input("Enter the salary of the employee: "))
  e_dict[e_name] = e_salary
salaries = list(e_dict.values())
names = list(e_dict.keys())
for i in range(3):
  s = salaries.index(max(salaries))
  name = names[s]
  salaries.pop(s)
  print(name)
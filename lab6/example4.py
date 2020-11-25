lst_input = input("Enter the list separated by space: ")
lst = lst_input.split(" ")
unique_lst = []
for i in lst:
  if i not in unique_lst:
    unique_lst.append(i)
  else:
    pass
print(unique_lst)
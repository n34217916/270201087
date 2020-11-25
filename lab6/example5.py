n = int(input("Enter the dimension of the identity matrix: "))
i_matrix = []
for k in range(0,n):
  for l in range(0,n):
    if k == l:
      i_matrix.append(1)
    else:
      i_matrix.append(0)

print(i_matrix)
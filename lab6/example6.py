n = int(input("Enter number of rows and cloumns (n) in the square matrix: "))
matrix = []
print("Enter the %s x %s matrix: "% (n, n))
for i in range(n):
  matrix.append(list(map(int, input().rstrip().split())))
sum = 0
for i in range(n):
  sum += matrix[i][i]

print (sum)
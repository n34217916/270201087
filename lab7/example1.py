n_a = [("Jon", 15), ("Ned", 45), ("Arya", 9), ("Catelyn", 44), ("Bran", 10)]
for i in range(len(n_a)):
  p = n_a[i]
  name = p[0]
  age = p[1]
  if age > 18:
    print(name)
  else:
    pass
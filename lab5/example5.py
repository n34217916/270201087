n = int(input("How many Fibonacci numbers you would like to generate?"))
a = 1
b = 1
if n == 2 :
  print(a, b)

elif n == 1:
  print(a)

elif n > 2 :
  all_list = [a, b]
  for i in range(n):
    nxt = a + b
    all_list.append(nxt)
    a = b
    b = nxt
  print(all_list)
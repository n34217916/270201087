print("Enter the a, b, c of the quadratic equation ax^2 + bx + c that you want the roots of")
a = float(input("Enter the a: "))
b = float(input("Enter the b: "))
c = float(input("Enter the c: "))

delta = b ** 2 - 4*a*c

if delta > 0 :
  root1 = ( -b + delta**0.5 ) / (2*a)
  root2 = ( -b - delta**0.5 ) / (2*a)
  print ("The roots are", root1, ",", root2)
elif delta == 0 :
  root = - b / (2*a)
  print ("The root is", root)
else :
   root1 = str(( -b + (-delta)**0.5 ) / (2*a))
   root1 = root1 + "i"
   root2 = str(( -b - (-delta)**0.5 ) / (2*a))
   root2 = root2 + "i"
   print ("The roots are", root1, ",", root2)
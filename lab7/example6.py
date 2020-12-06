numbers1 = [2,3,4,20,5,5,15]
numbers2 = [10,20,20,15,30,40]
s1 = set(numbers1)
s2 = set(numbers2)
intersection = []
if s in s1 and s in s2:
  intersection.append(s)
  s1.remove(s)
  s2.remove(s)
else:
  pass
print(intersection)
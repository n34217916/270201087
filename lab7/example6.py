numbers1 = [2,3,4,20,5,5,15]
numbers2 = [10,20,20,15,30,40]
s1 = set(numbers1)
s2 = set(numbers2)
intersection = []
for s in s1:
  if s in s1 and s in s2:
    intersection.append(s)
  else:
    pass
print("Intersection of the two sets is: ", intersection)
union = []
for i in s1:
  union.append(i)
for s in s2:
  if s not in union:
    union.append(s)
  else:
    pass
print("Union of the two sets is: ", union)
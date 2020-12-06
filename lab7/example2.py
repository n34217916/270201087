books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
book_dict = {}
for i in range(len(books)):
  book = books[i]
  v1 = len(book)
  a = book
  v2 = len(list(set(a)))
  v = []
  v.append(v1)
  v.append(v2)
  v = tuple(v)
  book_dict[book] = v
for i in book_dict:
    print (i, book_dict[i])
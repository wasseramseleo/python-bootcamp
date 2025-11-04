numbers = [1, 2, 3, 4]

# map
doubled = list(map(lambda x: x * 2, numbers))

# List Comprehension
doubled_comp = [x * 2 for x in numbers]

# filter
even = list(filter(lambda x: x % 2 == 0, numbers))

# List Comprehension
even_comp = [x for x in numbers if x % 2 == 0]














def add(a, b):
  c = a + 1
  d = b + 1
  return c + d


summe = lambda x, y: add(x, y) + 1


# Das Ergebnis ist der Rückgabewert des Funktionsaufrufs
print(summe(10, 5))





















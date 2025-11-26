from functools import reduce
total = reduce(lambda acc, el: acc + el, numbers)

# GUT (klar, schnell, built-in)
total = sum(numbers)
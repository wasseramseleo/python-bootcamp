from functools import reduce

numbers = [1, 2, 3, 4]

# 1. (acc=1, el=2) -> 3
# 2. (acc=3, el=3) -> 6
# 3. (acc=6, el=4) -> 10
total = reduce(lambda acc, el: acc + el, numbers)

print(total)
# Output: 10
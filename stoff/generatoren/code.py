class FibonacciIterator:
  def __init__(self, max_count):
    self.max_count = max_count
    self.current_count = 0
    self.a, self.b = 0, 1

  def __iter__(self):
    return self

  def __next__(self):
    if self.current_count >= self.max_count:
      raise StopIteration
    # ... (Logik) ...










def fibonacci_generator(max_count):
  """
  Ein Generator, der Fibonacci-Zahlen 'yielded' (ergibt).
  """
  print("Generator wird gestartet...")
  count = 0
  a, b = 0, 1
  while count < max_count:
    yield a  # 3. Hier pausiert die Funktion
    a, b = b, a + b
    count += 1
  print("Generator ist am Ende.")


# 1. Aufruf erzeugt nur das Generator-Objekt.
# (Der print()-Befehl oben wird NICHT ausgeführt)
fib_gen = fibonacci_generator(5)

print(type(fib_gen))
# Output: <class 'generator'>



fib_gen = fibonacci_generator(3) # 'fib_gen' ist jetzt ein Iterator

# 2. next() startet den Code bis zum ersten 'yield'
print(f"Ergebnis 1: {next(fib_gen)}")
# Output:
# Generator wird gestartet...
# Ergebnis 1: 0

# 4. next() setzt den Code nach 'yield a' fort
print(f"Ergebnis 2: {next(fib_gen)}")
# Output:
# Ergebnis 2: 1

print(f"Ergebnis 3: {next(fib_gen)}")
# Output:
# Ergebnis 3: 1

# 5. Die Schleife endet, die Funktion terminiert.
# next() löst automatisch StopIteration aus.
print(next(fib_gen))
# Output:
# Generator ist am Ende.
# Traceback (most recent call last):
#   ...
# StopIteration





# Klasse
class FibonacciIterator:
    def __init__(self, max_count):
        self.max_count = max_count
        self.current_count = 0
        self.a, self.b = 0, 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.current_count >= self.max_count:
            raise StopIteration
        self.current_count += 1
        val = self.a
        self.a, self.b = self.b, self.a + self.b
        return val


# Generator
def fibonacci_generator(max_count):
    count = 0
    a, b = 0, 1
    while count < max_count:
        yield a
        a, b = b, a + b
        count += 1
def test(a: int, b: int) -> int:
  retrun a + b

def test2(a: int) -> int:
  return a ** 2

def test3(a: int, b: int) -> int:
  return a - b
print(test(5, 5))
print(test(0, 0))
print(test(1, 1))
print(test(2, 2) == test2(2))
print(test(3, 5))
print(test(-1, 1))

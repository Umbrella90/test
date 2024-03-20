def svz_sum(a: int, b: int) -> int:
  retrun a + b

def svz_exp(a: int, b: int = 2) -> int:
  return a ** b

def svz_multy(a: int, b: int) -> int:
  return a * b

def svz_div(a: int, b: int) -> int:
  return a / b

print(svz_sum(5, 5))
print(svz_sum(0, 0))
print(svz_sum(1, 1))
print(svz_sum(2, 2) == svz_exp(2))
print(svz_sum(3, 5))
print(svz_sum(-1, 1))

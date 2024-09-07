def max2(i, j):
  if i < j:
      return j
  else:
      return i

def max3(i, j, k):
  return max2(max2(i,j),k)

from cvc5.pythonic import *

j11,j12,j21,j22,j31,j32 = Ints("j11 j12 j21 j22 j31 j32")

s = SolverFor('QF_IDL')
s.add(And([x >= 0 for x in [j11, j12, j21, j22, j31, j32]]))
s.add(And(j12 - j11 >= 10, j22 - j21 >= 15, j32 - j31 >= 5))
s.add(And(Or(j22 - j11 >= 10, j11 - j22 >= 5), 
          Or(j31 - j11 >= 10, j11 - j31 >= 5), 
          Or(j31 - j22 >= 5, j22 - j31 >= 5)))
s.add(And(Or(j21 - j12 >= 5, j12 - j21 >= 15), 
          Or(j32 - j12 >= 5, j12 - j32 >= 5), 
          Or(j32 - j21 >= 15, j21 - j32 >= 5)))
s.add(And(j12 <= 25, j22 <= 25, j32 <= 25))

s.push()
result = s.check()
while result == sat:
  m = s.model()
  a = m.eval(j12).as_long()
  b = m.eval(j22).as_long()
  c = m.eval(j32).as_long()
  s.pop()
  best = max3(a, b, c) + 5
  print("Best solution so far:", best, "minutes")
  new_threshold = best - 5
  s.push()
  s.add(And(j12 < new_threshold, j22 < new_threshold, j32 < new_threshold))
  result = s.check()

s.pop()
print(best, "is the best solution")

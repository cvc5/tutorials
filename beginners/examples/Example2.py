from cvc5.pythonic import *

x, y, z = BitVecs('x y z', 32)
s = SolverFor('QF_BV')

s.add(x == z * 2)
s.add(x * y == 1)

result = s.check()
print("result: ", result)
if result == sat:
  m = s.model()
  print("\n".join([str(k) + " : " + str(m[k]) for k in m]))

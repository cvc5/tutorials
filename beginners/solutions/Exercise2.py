from cvc5.pythonic import *

x = BitVec('x', 8)
s = SolverFor('QF_BV')

s.add(x * 5 == 1)

result = s.check()
print("result: ", result)
if result == sat:
  m = s.model()
  print("\n".join([str(k) + " : " + str(m[k]) for k in m]))

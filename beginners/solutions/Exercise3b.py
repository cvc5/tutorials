from cvc5.pythonic import *
U = DeclareSort("U")
b = Const("b", BoolSort())
x, y, z, w = Consts("x y z w", U)

s = SolverFor('QF_UF')
s.add(x == (If(b, y, z)))
s.add(Or((w == y), (w == z)))
s.add(y == z)
s.add(x != w)

if s.check() == sat:
  m = s.model()
  print("\n".join([str(k) + " : " + str(m[k]) for k in m]))
else:
  print("no solution")

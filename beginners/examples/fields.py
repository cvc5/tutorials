from cvc5.pythonic import *
F = FiniteFieldSort(13)
x, y = FiniteFieldElems("x y", F)
s = SolverFor("QF_FF")
s.add(x + y == 1)
s.add(x * y == 1)
print(s.model() if s.check() == sat else "unsat")


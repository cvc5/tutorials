from cvc5.pythonic import *
x, y = FiniteFieldElems("x y", 13)
s = SolverFor("QF_FF")
s.add(x * x == y)
s.add(y * y == 1)
print(s.model() if s.check() == sat else "unsat")

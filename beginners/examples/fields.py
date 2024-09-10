from cvc5.pythonic import *
x, y = FiniteFieldElems("x y", 13)
s = SolverFor("QF_FF")
s.add(x + y == 1)
s.add(x * y == 1)
print(s.model() if s.check() == sat else "unsat")


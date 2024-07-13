from cvc5.pythonic import *
x, y, z = Reals("x y z")
s = SolverFor('QF_NRA')
s.add(x*x*y + y*z + 2*x*y*z + 4*x*y + 8*x*z + 16 == 0)
print(s.model() if s.check() == sat else "unsat")


from cvc5.pythonic import *
x = Const("x", BitVecSort(32))
xrs = x >> 31
s = SolverFor('QF_BV')
s.add(If(x < 0, -x, x) != (x ^ xrs) - xrs)      # prove abs() == abs1()
print(s.model() if s.check() == sat else "unsat")

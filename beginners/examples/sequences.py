from cvc5.pythonic import *
x, y, z = Consts("x y z", SeqSort(IntSort()))

s = SolverFor('QF_SLIA')

s.add(Length(x) > 0)
s.add(x[0] + x[Length(x) - 1] == 9)
s.add(y == Concat(x,x))
s.add(z == Concat(Unit(IntVal(3)), Unit(IntVal(4)), Unit(IntVal(5))))
s.add(Contains(y, z))

print(s.model() if s.check() == sat else "unsat")


from cvc5.pythonic import *
x, y, z = Consts("x y z", SeqSort(IntSort()))

s = SolverFor('QF_SLIA')

s.add(And(PrefixOf(x, y),  x != y))
s.add(And(PrefixOf(y, z),  y != z))
s.add(And(PrefixOf(z, x),  z != x))


print(s.model() if s.check() == sat else "unsat")


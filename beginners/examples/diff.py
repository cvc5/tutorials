from cvc5.pythonic import *

j11,j12,j21,j22,j31,j32 = Ints("j11 j12 j21 j22 j31 j32")

s = SolverFor('QF_IDL')
s.add(And([x >= 0 for x in [j11, j12, j21, j22, j31, j32]]))
s.add(And(j12 - j11 >= 10, j22 - j21 >= 20, j32 - j31 >= 5))
s.add(And(Or(j22 - j11 >= 10, j11 - j22 >= 5), 
          Or(j31 - j11 >= 10, j11 - j31 >= 5), 
          Or(j31 - j22 >= 5, j22 - j31 >= 5)))
s.add(And(Or(j21 - j12 >= 5, j12 - j21 >= 5), 
          Or(j32 - j12 >= 5, j12 - j32 >= 5), 
          Or(j32 - j21 >= 5, j21 - j32 >= 5)))
s.add(And(j12 <= 25, j22 <= 25, j32 <= 25))

print(s.model() if s.check() == sat else "unsat")

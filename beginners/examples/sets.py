from cvc5.pythonic import *
S = DeclareSort("S")
A, B, C = [Set(i, S) for i in ["A","B","C"]]
s = SolverFor('QF_FS')
s.add(Not((A | (B & C)) == ((A | B) & (A | C))))
print(s.check())


from cvc5.pythonic import *
S = DeclareSort("S")
A, B, C = [Set(i, S) for i in ["A","B","C"]]
s = SolverFor('QF_FS')
s.add(Not(SetMinus(A, (B & C)) == ((SetMinus(A, B)) & (SetMinus(A, C)))))
print(s.check())
print(s.model())


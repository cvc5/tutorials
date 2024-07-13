from cvc5.pythonic import *
I = DeclareSort("I")
E = DeclareSort("E")
i, j = Consts("i j", I)
tmp = Const("tmp", E)
array = ArraySort(I, E)
a_in, a_out = Consts("a_in, a_out", array)

s = SolverFor('QF_AX')

s.add(tmp == (Select(a_in, i)))
s.add(a_out == (Store(Store(a_in, i, Select(a_in, j)), 
    j, tmp)))
s.add((Select(a_in, i)) == (Select(a_in, j)))
s.add(a_in != a_out)

print(s.check())


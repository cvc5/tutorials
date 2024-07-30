from cvc5.pythonic import *

a, b, c = FPs("a b c", Float32())
rm = Const("rm", RNE().sort())

s = SolverFor('QF_FP')
s.add(Distinct(fpAdd(rm, a, fpAdd(rm, b, c)), fpAdd(rm, fpAdd(rm, a, b), c)))
result = s.check()
m = s.model()
print(m)
print(f'fpAdd(rm, a, fpAdd(rm, b, c)) = {m.eval(fpAdd(rm, a, fpAdd(rm, b, c)))}')
print(f'fpAdd(rm, fpAdd(rm, a, b), c) = {m.eval(fpAdd(rm, fpAdd(rm, a, b), c))}')

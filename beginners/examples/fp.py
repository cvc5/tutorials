from cvc5.pythonic import *

a, b, c = FPs("a b c", Float32())
rm = Const("rm", RNE().sort())
s = SolverFor('QF_FP')
s.add(Distinct(fpFMA(rm, a, b, c), fpAdd(rm, fpMul(rm, a, b),c)))
result = s.check()
m = s.model()
print(m)
print(f'fpFMA(rm, a, b, c) = {m.eval(fpFMA(rm, a, b, c))}')
print(f'fpAdd(rm, fpMul(rm, a, b),c) = {m.eval(fpAdd(rm, fpMul(rm, a, b),c))}')

from cvc5.pythonic import *
p, x, i = {}, {}, {}
for k in range(1, 13): p[k] = Bool("p" + str(k))
for k in range(1, 6): x[k] = String("x" + str(k))
for k in range(1,7): i[k] = String("i" + str(k))

result = StringVal("abbaabb")

s = SolverFor('QF_SLIA')
s.add(And(Length(x[1]) <= 2, Length(x[2]) <= 2))

s.add(i[1] == If(p[1], x[1], x[2]))
s.add(i[2] == If(p[2], x[1], x[2]))
s.add(x[3] == Concat(i[1], i[2]))

s.add(i[3] == If(p[3], x[1], If(p[4], x[2], x[3])))
s.add(i[4] == If(p[5], x[1], If(p[6], x[2], x[3])))
s.add(x[4] == Concat(i[3], i[4]))

s.add(i[5] == If(p[7], x[1], If(p[8], x[2], If(p[9], x[3], x[4]))))
s.add(i[6] == If(p[10], x[1], If(p[11], x[2], If(p[12], x[3], x[4]))))
s.add(x[5] == Concat(i[5], i[6]))

s.add(x[5] == result)

print(s.model() if s.check() == sat else "unsat")

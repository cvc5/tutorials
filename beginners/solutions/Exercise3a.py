from cvc5.pythonic import *
U = DeclareSort("U")
f = Function("f", U, U)
x = Const("x", U)

s = SolverFor('QF_UF')
s.add(And((f(f(x)) == x), (f(f(f(f(x))))) == x))
s.add(Distinct(f(x), x))  # negation of f(x) = x

result = s.check()
print(result)
if result == sat:
  m = s.model()
  print("\n".join([str(k) + " : " + str(m[k]) for k in m]))


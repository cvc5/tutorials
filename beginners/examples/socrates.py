from cvc5.pythonic import *
S = DeclareSort("S")
Bool = BoolSort()
Human = Function("Human", S, Bool)
Mortal = Function("Mortal", S, Bool)
Socrates = Const("Socrates", S)

s = SolverFor('UF')

x = Const("x", S)
s.add(ForAll([x], Implies(Human(x), Mortal(x))))
s.add(Human(Socrates))
s.add(Not(Mortal(Socrates)))

print(s.check())


from cvc5.pythonic import *
decl = Datatype("tree")
decl.declare("node", ("data", IntSort()), ("left", decl), ("right", decl))
decl.declare("nil")
Tree = decl.create()

x = Const("x", Tree)

s = SolverFor('ALL')
s.add(Tree.is_node(x))
s.add(Tree.left(x) == x)

print(s.model() if s.check() == sat else "unsat")
    

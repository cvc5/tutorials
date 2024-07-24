from cvc5.pythonic import *
a, b = Reals('a b')
solve(a + 10.0 == 2.0 * b, b + 20.0 == 2.0 * a)

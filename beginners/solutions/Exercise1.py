from cvc5.pythonic import *
a, b = Ints('a b')
solve(a + 10 == 2 * b, b + 20 == 2 * a)

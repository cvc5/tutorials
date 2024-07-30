from cvc5.pythonic import *
x = Const("x", BitVecSort(32))
xrs = x >> 31
abs_ref = If(x < 0, -x, x)   # abs() reference implementation
abs1 = (x ^ xrs) - xrs
abs2 = (x + xrs) ^ xrs
abs3 = x - ((x << 1) & xrs)

prove(abs_ref == abs1)
prove(abs_ref == abs2)
prove(abs_ref == abs3)

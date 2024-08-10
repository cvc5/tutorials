sat
(
(define-fun a () (_ FloatingPoint 8 24) (fp #b1 #b01111110 #b01010101010101010101011))
(define-fun b () (_ FloatingPoint 8 24) (fp #b1 #b01111110 #b11111111111111111111111))
(define-fun c () (_ FloatingPoint 8 24) (fp #b1 #b01111110 #b11111111111111111111111))
(define-fun rm () RoundingMode roundTowardPositive)
)
(((fp.fma rm a b c) (fp #b1 #b01111101 #b01010101010101010101001)))
(((fp.add rm (fp.mul rm a b) c) (fp #b1 #b01111101 #b01010101010101010101000)))

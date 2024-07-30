sat
(
(define-fun a () (_ FloatingPoint 8 24) (fp #b1 #b11000111 #b00011111111111111111111))
(define-fun b () (_ FloatingPoint 8 24) (fp #b0 #b11000111 #b00000000000000000000000))
(define-fun c () (_ FloatingPoint 8 24) (fp #b1 #b10001101 #b11111111000000000000000))
(define-fun rm () RoundingMode roundTowardNegative)
)
(((fp.add rm a (fp.add rm b c)) (fp #b1 #b11000011 #b11111111111111111111000)))
(((fp.add rm (fp.add rm a b) c) (fp #b1 #b11000011 #b11111111111111111110001)))

(set-logic QF_FF)
(set-option :produce-models true)

(define-sort F () (_ FiniteField 13))

(declare-const x F)
(declare-const y F)

(assert (= y (ff.mul x x)))
(assert (= (ff.mul y y) (as ff1 F)))

(check-sat)
(get-model)

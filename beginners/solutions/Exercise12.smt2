(set-logic QF_FF)
(set-option :produce-models true)

(define-sort F () (_ FiniteField 13))  ; F is an alias of sort (_ FiniteField 13)

(declare-const x F)
(declare-const y F)

(assert (= (ff.mul x x) y))
(assert (= (ff.mul y y) (as ff1 F)))

(check-sat)
(get-model)

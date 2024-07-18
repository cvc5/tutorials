(set-logic QF_UF)
(set-option :produce-models true)

(declare-sort U 0)

(declare-fun f (U) U)
(declare-const x U) 

(assert (and (= (f (f x)) x) (= (f (f (f (f x)))) x)))
(assert (distinct (f x) x))

(check-sat)
(get-model)

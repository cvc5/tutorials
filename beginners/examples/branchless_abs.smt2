(set-logic QF_BV)

(declare-const x (_ BitVec 32))

; orignal abs(x) version
(define-fun abs ((x (_ BitVec 32))) (_ BitVec 32) (ite (bvslt x (_ bv0 32)) (bvneg x) x))

; encode branchless abs(x)
(define-fun xrs () (_ BitVec 32) (bvashr x (_ bv31 32)))
(define-fun abs1 ((x (_ BitVec 32))) (_ BitVec 32) (bvsub (bvxor x xrs) xrs))

(assert (distinct (abs x) (abs1 x)))  ; check if abs() and abs1() are equivalent

(check-sat)

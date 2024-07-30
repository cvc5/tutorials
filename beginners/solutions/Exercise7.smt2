(set-logic QF_BV)
(set-option :incremental true)

(declare-const x (_ BitVec 32))

; orignal abs(x) version
(define-fun abs ((x (_ BitVec 32))) (_ BitVec 32) (ite (bvslt x (_ bv0 32)) (bvneg x) x))

; encode branchless abs(x) alternatives
(define-fun xrs () (_ BitVec 32) (bvashr x (_ bv31 32)))
(define-fun abs1 ((x (_ BitVec 32))) (_ BitVec 32) (bvsub (bvxor x xrs) xrs))
(define-fun abs2 ((x (_ BitVec 32))) (_ BitVec 32) (bvxor (bvadd x xrs) xrs))
(define-fun abs3 ((x (_ BitVec 32))) (_ BitVec 32) (bvsub x (bvand (bvshl x (_ bv1 32)) xrs)))

; check if abs() and abs1() are equivalent
(push 1)
(assert (distinct (abs x) (abs1 x)))
(check-sat)
(pop 1)

; check if abs() and abs2() are equivalent
(push 1)
(assert (distinct (abs x) (abs2 x)))
(check-sat)
(pop 1)

; check if abs() and abs3() are equivalent
(push 1)
(assert (distinct (abs x) (abs3 x)))
(check-sat)
(pop 1)

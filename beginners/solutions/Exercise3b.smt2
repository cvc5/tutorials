(set-logic QF_UF)

(declare-sort U 0)

(declare-const b Bool)
(declare-const x U) 
(declare-const y U) 
(declare-const z U) 
(declare-const w U) 

(assert (= x (ite b y z)))
(assert (or (= w y) (= w z)))
(assert (= y z))
(assert (distinct x w))
  
(check-sat)

(set-logic QF_FS)

(declare-sort U 0)

(declare-const A (Set U))
(declare-const B (Set U))
(declare-const C (Set U))

(assert (not (= (set.union A (set.inter B C)) (set.inter (set.union A B) (set.union A C)))))

(check-sat)

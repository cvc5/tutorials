(set-logic QF_FS)
(set-option :produce-models true)

(declare-sort U 0)

(declare-const A (Set U))
(declare-const B (Set U))
(declare-const C (Set U))

(assert (not (= (set.minus A (set.inter B C)) (set.inter (set.minus A B) (set.minus A C)))))

(check-sat)
(get-model)

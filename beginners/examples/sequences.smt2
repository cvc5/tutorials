(set-logic QF_SLIA)
(set-option :produce-models true)

(declare-const x (Seq Int))
(declare-const y (Seq Int))
(declare-const z (Seq Int))

(assert (> (seq.len x) 0))
(assert (= (+ (seq.nth x 0) (seq.nth x (- (seq.len x) 1))) 9))

(assert (= y (seq.++ x x)))
(assert (= z (seq.++ (seq.unit 3) (seq.unit 4) (seq.unit 5))))
(assert (seq.contains y z))

(check-sat)
(get-model)

(set-logic QF_SLIA)

(declare-const x (Seq Int))
(declare-const y (Seq Int))
(declare-const z (Seq Int))

(assert (and (seq.prefixof x y) (distinct x y)))
(assert (and (seq.prefixof y z) (distinct y z)))
(assert (and (seq.prefixof z x) (distinct z x)))

(check-sat)

(set-logic QF_DTLIA)
(set-option :produce-models true)

(declare-datatypes ((Tree 0)) (((node (data Int) (left Tree) (right Tree)) (nil))))

(declare-fun x () Tree)

(assert ((_ is node) x))
(assert (= (left x) x))

(check-sat)

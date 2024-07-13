.. include:: macros.rst

.. _smt-theories:

SMT Theories
============

A key feature of SMT is that the entire problem is parameterized by the choice
of a theory |T|. This is important because it means that SMT is an algorithmic
*framework*, rather than a fixed algorithm. Thus, if a particular problem cannot
easily be encoded in any existing theory supported by SMT solvers, one option
is to add support for a new theory which is better suited to the problem. In
fact, this is exactly the process by which many of the theories supported by
modern SMT solvers were added.

Theories can be used alone or in arbitrary combinations. Besides the theory,
other parameters related to the syntax of formulas include whether or not to
enable quantifiers and whether to disallow or limit the use of certain theory
operations. In the SMT-LIB standard, and in solvers that support it, these pa-
rameters are configured by specifying a *logic*. A logic identifies the theory
(or theories) being used and optionally imposes syntactic restrictions on the
allowed formulas. Users can provide the SMT solver with a predefined *logic name*
(like |QF_LIA|, |QF_BV| and |UF| seen earlier) to specify which logic is to be
used. By default (i.e., if no logic name is provided), SMT solvers typically
enable all the theories they support and allow all operations. This is
equivalent to using the special logic name |ALL|. However, solvers are often
tuned with specific heuristics for specific logics. Thus, it is advisable to
provide the solver with the most specific logic name possible. In this section,
we discuss the most common theories and logics supported by SMT solvers, with
examples of each.

.. include:: theories/core
.. include:: theories/arith
.. include:: theories/arrays
.. include:: theories/bitvectors
.. include:: theories/datatypes
.. include:: theories/floating-point
.. include:: theories/strings
.. include:: theories/quantifiers
.. include:: theories/non-standard

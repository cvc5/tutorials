.. include:: macros.rst

.. _formal-foundations:

Formal Foundations
==================

The satisfiability modulo theories problem can be formalized in many-sorted
first-order logic with equality. We briefly outline the necessary concepts
here. Due to space constraints, we assume some familiarity with basic concepts
and notation from mathematical logic. More details can be found in [R21]_,
[R25]_.

Syntax
------

In first-order logic, one constructs formulas that are statements about
individuals in some domain of discourse and their relationships. Many-sorted
logic adds the possibility of talking about multiple, separate domains.
                
Signatures
^^^^^^^^^^

The language of formulas is determined by a vocabulary of
symbols, called a *signature*, which has three main components: *sort symbols*
(such as :math:`\mathsf{Int}`, :math:`\mathsf{Real}`, :math:`\mathsf{Person}`,
etc.)  which name, or *denote*, domains of interest; *function symbols* (such
as, :math:`+`, :math:`*`, :math:`\mathsf{log}`, :math:`\mathsf{mother}`,
:math:`\mathsf{father}`) which denote total functions over the domains; and
*relation symbols* (such as, :math:`=`, :math:`<`, :math:`\mathsf{even}`,
:math:`\mathsf{married}`) which denote total relations over the domains.  A
signature also specifies the *arity* of each function symbol :math:`f`, which
is the number of inputs :math:`f` takes, as well as its *rank*, which consists
of the sort of :math:`f`'s inputs and of :math:`f`'s output. [#]_  We say that
:math:`f` has arity :math:`n` and rank :math:`\sigma_1\cdots\sigma_n\sigma` in
a signature |sig| if :math:`f` takes :math:`n` inputs of respective sorts
:math:`\sigma_1, \ldots, \sigma_n` and returns an output of sort |sor|.  A
function symbol of arity 0 and rank \sigma (such as 0, 1,
:math:`\mathsf{true}`, etc.) is also called a *constant symbol* of sort \sigma.
It is convenient to consider only signatures that have a distinguished sort
|boolS|, for the Booleans, and treat relation symbols as function symbols whose
return type is |boolS|.  In addition, we assume that every signature contains a
distinguished function symbol :math:`\approx_\sigma` of rank
:math:`\sigma\sigma`\ |boolS|, denoting the identity relation, for each sort
|sor| of |sig|.

A signature |sig| is a *subsignature* of a signature :math:`\Omega`,
and :math:`\Omega` is a *supersignature* of |sig|, 
if all the sort and function symbols of |sig| are also in :math:`\Omega`
and the function symbols have the same rank in :math:`\Omega` as they do in |sig|.

Variables, terms and formulas
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To build formulas, in addition to fixing a
signature |sig|, we also fix a set |vset| of *sorted* variables,
each associated with a sort |sor| and standing for some element from (the set
denoted by) |sor|.  We can then build terms out of variables and function
symbols from |sig|.  Given a signature |sig|, a *well-sorted*
|sig|\ *-term*, or just *term* for short, is defined inductively as
follows: :math:`(i)` a variable or constant symbol of sort |sor| is a term of
sort |sor|; :math:`(ii)` if :math:`f` is a function symbol of rank
:math:`\sigma_1\cdots\sigma_n\sigma`, with :math:`n>0`, and :math:`t_1, \ldots,
t_n` are terms of sort :math:`\sigma_1\cdots\sigma_n`, respectively, then the
expression :math:`f(t_1, \ldots, t_n)` is a term of sort |sor|; :math:`(iii)`
if |form| is a term of sort |boolS| and :math:`x` is a variable of sort |sor|,
then the expressions :math:`\exists\, x : \sigma` |form| and :math:`\forall\, x :
\sigma` |form| are terms of sort |boolS|.  We then *identify formulas with
terms of sort* |boolS|.  The distinguished symbols :math:`\forall` and
:math:`\exists` are *quantifier symbols*.  We say that a variable :math:`x`
*occurs free* in a formula |form| if :math:`x` occurs in |form| and either
|form| contains no quantifier symbols or it has the form :math:`\exists\, y :
\sigma. \varphi'` or :math:`\forall\, y :\sigma. \varphi'`, for some variable
:math:`y`, where :math:`x` occurs free in :math:`\varphi'`.

Semantics
---------

For each signature |sig|, the meaning of |sor|\ -terms is provided 
by mathematical structures called interpretations.
A |sig|\ *-interpretation* |I| maps:


  - each sort |sor| of |sig| to a *non-empty* set :math:`\sigma^\mathcal{I}`,
    the *domain* of |sor| in |I|, with :math:`\mathsf{Bool}^\mathcal{I}` being
    the binary set :math:`\{\mathsf{true},\mathsf{false}\}`\ ;

  - each variable :math:`x \in` |vset| of sort |sor| to an element
    :math:`x^\mathcal{I} \in \sigma^\mathcal{I}`\ ;

  - each function symbol :math:`f` of rank :math:`\sigma_1\cdots\sigma_n\sigma` to
    a *total* function :math:`f^\mathcal{I}` of type :math:`\sigma_1^\mathcal{I} \times \cdots
    \times \sigma_n^\mathcal{I} \to \sigma^\mathcal{I}` (and, in particular, each constant symbol
    :math:`c` of sort |sor| to an element :math:`c^\mathcal{I} \in \sigma^\mathcal{I}`).

We say that |sor| (resp. :math:`x`, :math:`f`) *denotes* the set
:math:`\sigma^\mathcal{I}` (element :math:`x^\mathcal{I}`, function
:math:`f^\mathcal{I}`) in |I|.  Every |sig|\ -interpretation |I| extends from
variables and function symbols to |sig|\ -terms :math:`t` as follows:
:math:`(i)` a term :math:`f(t_1,\ldots,t_n)` *evaluates* in |I| to
:math:`f^\mathcal{I}(t_1^\mathcal{I},\ldots,t_n^\mathcal{I})`, the value
returned by function :math:`f^\mathcal{I}` when applied to the elements denoted
by :math:`t_1,\ldots,t_n`; :math:`(ii)` an *existentially quantified* formula
:math:`\exists\, x : \sigma. \varphi` evaluates to :math:`\mathsf{true}` in |I|
if and only if |form| evaluates to :math:`\mathsf{true}` in an interpretation
:math:`\mathcal{I}[x \mapsto a]` that maps :math:`x` to *some* suitable
:math:`a \in \sigma^\mathcal{I}` and is otherwise identical to |I|\ ;
:math:`(iii)` a *universally quantified* formula :math:`\forall\, x :
\sigma. \varphi` evaluates to :math:`\mathsf{true}` in |I| if and only if
|form| evaluates to :math:`\mathsf{true}` in :math:`\mathcal{I}[x \mapsto a]`
for *all* possible choices of values for :math:`x` in
:math:`\sigma^\mathcal{I}`\ .

An interpretation |I| *satisfies* a formula |form| if :math:`\varphi^\mathcal{I} = \mathsf{true}`
and *falsifies* it if :math:`\varphi^\mathcal{I} = \mathsf{false}`.  In the
former case, we also say that |I| is a *model* of |form|.

The *reduct* of an |supsig|\ -interpretation |I| to a subsignature |sig| of
|supsig| is the (unique) |sig|\ -interpretation that interprets the symbols of
|sig| exactly as |I|\ .  Intuitively, the reduct is obtained by *forgetting*
the symbols of |supsig| that are not in |sig|.

In the definition of interpretation above, we have not provided a meaning for
the usual Boolean connectives such as :math:`\lnot, \land, \lor, \Rightarrow` and
so on.  In SMT, specific interpretations of function symbols are provided by a
theory, as explained next.

Theories
--------

In general, we are not interested in arbitrary interpretations of terms and
formulas in a signature |sig| but in interpretations belonging to a specific
*theory* |T| that *constrain* the meaning of the symbols in |sig|; for
instance, that interpret :math:`\lnot` and :math:`\land` as logical negation
and conjunction, :math:`0, 1, 2, \ldots` as the natural numbers, and so on.
Traditionally in logic, a theory is defined by a set of formulas, called
*axioms*: one considers only |sig|\ -interpretations that satisfy all the axioms.
In SMT, a theory is, more generally, a class of interpretations that can be
specified axiomatically or in other ways.  More precisely, a |sig|\ *-theory* |T|
is a pair :math:`(\Sigma, \mathbf{I})` where |sig| is a signature and |IC| is a class of
|sig|\ -interpretations, however specified.  We describe and discuss several
examples of theories commonly used in SMT in the next section.

Given a theory |T| :math:`= (\Sigma, \mathbf{I})`, we consider not just |sig|\ -formulas
but |supsig|\ -formulas for some supersignature |supsig| of |sig|.

In the context of |T|, we refer to the symbols of |sig| as *theory* symbols and
to the additional symbols in |supsig| as *uninterpreted* symbols.  For
instance, in the theory of reals, we may write a formula of the form :math:`a +
1 > b` where :math:`a` and :math:`b` are uninterpreted, or *symbolic*,
constants of sort |realS|.  Intuitively, while the meaning of :math:`+` and
:math:`1` is fixed by the theory, the meaning of :math:`a` and :math:`b` is
not.  Hence, we consider the formula satisfiable if there are real values for
:math:`a` and :math:`b` which make the formula evaluate to |true|.  This idea is
formalized in the notion of *satisfiability in* |T|.

Satisfiability modulo a theory
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If |T| is a |sig|-theory, a |T|\ *-interpretation* is 
*any* |supsig|-interpretation |I| for some supersignature |supsig| of |sig|
whose restriction to |sig| differs from an interpretation of |T|
at most in the way it interprets the variables.

An :math:`\Omega`-formula |form| is *satisfiable in* |T| if it is satisfied by
*some* |T|-interpretation |I|---which may interpret the variables of |form| and
the sort, function, and predicate symbols not in |sig| arbitrarily.  The
formula is *valid in* |T| if it is satisfied by *all* |T|-interpretations.  A
set :math:`\Phi` of |supsig|-formulas *entails* |form| *in* |T|, written
:math:`\Phi \models_T \varphi`, if every |T|-interpretation that
satisfies all formulas in :math:`\Phi` satisfies |form| as well.  The set
:math:`\Phi` is *satisfiable in* |T| if there is a |T|-interpretation
that satisfies all of its formulas.


.. [#] For simplicity, we do not consider the more general case where function
       symbols can be overloaded by being assigned more than one arity and/or
       rank.
       

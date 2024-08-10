.. include:: macros.rst
   
.. _overview:

Overview
========

At an intuitive level, SMT solvers are general-purpose problem solving
tools. They are somewhat similar to calculators, in that the user provides the
problem of interest, and the tool does some calculation to produce an
answer. However, they are much more powerful than a simple calculator.

SMT solvers reason *symbolically*, as is done in grade school algebra. The user
provides a set of *assertions* that describe constraints to be satisfied, and the
solver produces a *solution* satisfying *all* of the constraints, if there is
one. Consider the following simple example, mimicking a typical algebra word
problem.

.. _Example 1:

  Example 1.  In 10 years, Alice will be twice as old as Bob is now, but in 22
  years, Bob will be twice as old as Alice is now. How old are Alice and Bob?
  
First, let’s see how to solve this using Python.

.. api-examples::
   <examples>/Example1.py

The Pythonic API is designed to be as simple and intuitive as possible. We
introduce the symbols we are using (SMT solvers always require that symbols be
introduced before they are used), and then we call solve, passing in the two
equations in much the same way we would write them naturally. The output is a
simple representation of the solution as a Python list.

.. code-block:: python

   [a = 18, b = 14]
   
Alternatively, SMT solvers can take as input a script written in the SMT- LIB
language [R5]_, a standard developed by the SMT community whose syntax is
similar to that of LISP. Below is the same example written in SMT-LIB.

.. api-examples::
   <examples>/Example1.smt2

The result is:

.. code-block:: smtlib

   sat
   (
   (define-fun a () Int 18)
   (define-fun b () Int 14)
   )

Notice that the solver replies |sat| before giving the solution. This is short
for “satisfiable,” a word meaning that there is at least one solution. SMT
solvers can also identify when a set of assertions has no solution. In this
case, the solver replies |unsat|, which is short for “unsatisfiable.”

Let’s take a closer look at the SMT-LIB input file, which is a sequence of
*commands*. The command in the first line tells the solver which *logic* we are
working in. In this case, we are using |QF_LIA| which stands for quantifier-free
linear integer arithmetic. We explain more about logics in :ref:`smt-theories`. The
second line tells the solver to produce *models*. A model assigns a concrete
meaning to every user-declared symbol. Without turning this option on, a
solver will still respond with |sat| or |unsat|, but it may not be able to provide
a model. The next two lines declare two *uninterpreted constants* called a
and b. Informally, we often refer to these as variables, because they play the
same role that variables do in math. However, in the automated reasoning
literature, a *variable* typically refers to a symbol that is bound by a
quantifier, whereas an uninterpreted constant is a symbol whose value is
determined by a model. SMT-LIB follows the the latter terminology. The next two
lines create *assertions*. An assertion is a way of telling the solver about a
formula that we would like to be true in the model that is produced. Note that
the formulas too are specified in a LISP-like prefix syntax. Finally, the
command |check-sat| tells the solver to check whether the set of assertions
made so far is satisfiable, and the command |get-model| (which is only legal if
the solver returns |sat|) prints values for each uninterpreted constant, with the
guarantee that assigning these values to the constants makes all the assertions
true. The values are printed using legal SMT-LIB syntax in case the user wants
to copy and paste them into a new SMT-LIB script.

.. _Exercise 1:

  Exercise 1. Consider a modification of :ref:`Example 1 <Example 1>`. The
  first assertion will stay the same, but for the second, let’s assert that Bob
  will be twice as old as Alice in only 20 years. Modify the Python program or
  SMT-LIB script to reflect the new set of constraints. What output does the
  SMT solver give?

  :ref:`Solution to Exercise 1 <Solution to Exercise 1>`

So far, we have seen the most basic use of an SMT solver. Given a set of
assertions, determine whether there is a solution for them. We now show that
this basic capability can be used to answer several similar questions.

Suppose we have a set :math:`X` of assumptions about the world, and we want to know
whether some hypothetical :math:`Y` is possible under those assumptions. If we can
express :math:`X` and :math:`Y` as SMT formulas, then an SMT solver can answer the question. In
fact, we simply assert each assumption in :math:`X` as well as the formula representing
:math:`Y` and check whether this set of assertions is satisfiable.

   _`Example 2`. Let :math:`x` and :math:`y` be 32-bit integers, with :math:`x` a multiple of 2. Is it
   possible for the machine arithmetic product of :math:`x` and :math:`y` to be 1?

For this problem, we’ll use *bit-vectors*. SMT solvers use bit-vectors to model
machine arithmetic and other operations on fixed-size vectors of bits.  The
SMT-LIB encoding and a corresponding Python script are shown below.  This time,
we use the Python API in a way that more closely resembles the SMT-LIB script.

.. api-examples::
    <examples>/Example2.smt2
    <examples>/Example2.py

We use the logic |QF_BV| which stands for quantifier-free bit-vectors. The
underscore symbol _ is used in SMT-LIB to indicate that the next symbol is
indexed by the following argument. It is used to specify the bit-vector size in
this example. The |bvmul| symbol represents bit-vector multiplication, and the
notation |bvX| is the bit-vector constant whose value, in decimal notation,
is |X|. Constant |z| names the value we must multiply by 2 to get |x|.  There is no
solution because an even number does not have a multiplicative inverse in
machine arithmetic (i.e., when doing arithmetic modulo a power of 2).  The
output of |cvcv| is shown below.

.. api-examples::
    <examples>/Example2.out.smt2
    <examples>/Example2.out.py

.. _Exercise 2:

  Exercise 2. Find the multiplicative inverse of 5 (mod :math:`2^8`).

  :ref:`Solution to Exercise 2 <Solution to Exercise 2>`

Another common situation is when we have a set :math:`X` of assumptions, and we
want to know whether some :math:`Y` *must* hold as a consequence. If so, we say
that :math:`Y` is *implied* or *entailed* by :math:`X`. Again, assuming we can represent
:math:`X` and :math:`Y` using formulas, we can start by asserting the formulas
representing :math:`X`. At this point, however, we do not assert the formula for :math:`Y`
. Instead, we assert its *negation*. If the result is |unsat|, then :math:`Y` must follow
from :math:`X`. The reasoning is that if it is not possible for the negation of :math:`Y` to be
true when :math:`X` is true, then :math:`Y` itself must be true. Let’s look at a version of the
well-known syllogism about Socrates.

.. _Example 3:

   Example 3. If all humans are mortal, and Socrates is a human, then must
   Socrates be mortal?

The SMT-LIB and Python versions are as follows.

.. api-examples::
   <examples>/socrates.smt2
   <examples>/socrates.py

This problem illustrates a few new encoding tools. First, we use the logic |UF|
which stands for “uninterpreted functions.” This logic allows us to declare new
function symbols. Note that it is also missing the |QF| prefix we’ve used above,
which means that quantifiers are also allowed. We declare a new uninterpreted
*sort* |S|. A sort is like a type in programming languages. We use an *uninterpreted*
sort to represent a class of individual objects that cannot be modeled with the
predefined sorts provided by SMT-LIB, (so far, we’ve seen the predefined sorts
for integers and bit-vectors). Next, we declare two functions, |Human| and
|Mortal|, each of which takes a single argument of sort |S| and returns a |Bool|, the
SMT-LIB Boolean sort. A function returning a Boolean is also called a
*predicate*. We then declare an uninterpreted constant called |Socrates| of
sort |S|. Now, we are ready to encode the first fact, namely that all humans are
mortal. To do so, we use the *universal quantifier* (:smt:`forall` in SMT-LIB,
|ForAll| in Python). The assertion states
that for every individual |x| of sort |S|, if the predicate |Human| holds for that
individual, then the predicate |Mortal| also holds. The next assertion states
that the |Human| predicate holds for |Socrates|. Finally, we want to see whether
the fact that Socrates is mortal necessarily follows from the assumptions. To
do this, we assert the negation of the statement and check for
satisfiability. Running the example confirms that the result is unsatisfiable
and thus, indeed, this statement is entailed.  The output of |cvcv| is shown
below.

.. api-examples::
   <examples>/socrates.out.smt2
   <examples>/socrates.out.py

What we have presented so far should provide a good high-level idea of what is
possible with SMT solvers. [#]_ We cover these ideas in more detail in the
following. In :ref:`formal-foundations`, we briefly describe the formal foundations for
SMT. Next, in :ref:`smt-theories`, we catalog the different theories supported by SMT
solvers and provide examples of how to use them. We cover the different outputs
produced by SMT solvers, including models and proofs, in :ref:`smt-solver-outputs`, and
conclude in :ref:`conclusion` with pointers to additional resources.

.. [#] More sophisticated features and use cases are beyond the scope of this
       tutorial, but we plan to provide additional tutorials on more advanced
       topics in the future.
       

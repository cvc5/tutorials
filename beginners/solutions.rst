.. include:: macros.rst

.. _solutions:

Solutions to Exercises
======================

.. _Solution to Exercise 1:

Solution to :ref:`Exercise 1 <Exercise 1>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. api-examples::
   <solutions>/Exercise1.smt2
   <solutions>/Exercise1.py

The output is as follows.

.. api-examples::
   <solutions>/Exercise1.out.smt2
   <solutions>/Exercise1.out.py

The SMT solver says |unsat| (or "no solution" for the Python version)
because there are no *integer* values that satisfy the constraints.
   
.. _Solution to Exercise 2:

Solution to :ref:`Exercise 2 <Exercise 2>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. api-examples::
   <solutions>/Exercise2.smt2
   <solutions>/Exercise2.py

The output is as follows.

.. api-examples::
   <solutions>/Exercise2.out.smt2
   <solutions>/Exercise2.out.py

The SMT solver gives a binary value of :smt:`x` as :smt:`#b11001101`.  This
equals :python:`205` in decimal.  And, indeed, :math:`5 \times 205 = 1025`, and
:math:`1025 \equiv 1\ \mathsf{mod}\ 256`.

.. _Solution to Exercise 3:

Solution to :ref:`Exercise 3 <Exercise 3>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

One way to modify :ref:`Example 4 <Example 4>` to make it satisfiable is to change the
hypothesis so that :smt:`f` is applied 2 and 4 times instead of 3 and 5 times.
In fact, any two number of applications that are not relatively prime will work.

.. api-examples::
   <solutions>/Exercise3a.smt2
   <solutions>/Exercise3a.py

The output from |cvcv| is as follows.

.. api-examples::
   <solutions>/Exercise3a.out.smt2
   <solutions>/Exercise3a.out.py

Notice that for the SMT-LIB example, |cvcv| uses a custom output format to describe how it has
interpreted the sort :smt:`U`: as a set with two elements, :smt:`@U_0` and
:smt:`@U_1`.  Furthermore, |cvcv| uses the :smt:`define-fun` command to
describe the value assigned to :smt:`f`.  In this case, the interpretation of
:smt:`f` maps :smt:`@U_1` to :smt:`@U_0` and everything else (i.e.,
:smt:`@U_0`) to :smt:`@U_1`.  Then, interpreting :smt:`x` as :smt:`@U_1`
satisfies the constraints.  The Python output gives the same model, but it uses
:python:`Lambda` to define the function.

We next consider how to modify :ref:`Example 5 <Example 5>`.  One way to do
this is to additionally require that :smt:`y` and :smt:`z`: are equal.

.. api-examples::
   <solutions>/Exercise3b.smt2
   <solutions>/Exercise3b.py

The output from |cvcv| is as follows.

.. api-examples::
   <solutions>/Exercise3b.out.smt2
   <solutions>/Exercise3b.out.py

.. _Solution to Exercise 4:

Solution to :ref:`Exercise 4 <Exercise 4>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the SMT-LIB solution, we make use of the :smt:`incremental` option, which
enables the commands :smt:`push` and :smt:`pop`.  These commands allow us to
temporarily add one or more assertions, check for satisfiability, and then 
return to the previous state.  The Python example demonstrates the power of
having the solver embedded in a general-purpose programming language: we can
use a loop to iterate until no better solution is found.

.. api-examples::
   <solutions>/Exercise4.smt2
   <solutions>/Exercise4.py

The output from |cvcv| is as follows.

.. api-examples::
   <solutions>/Exercise4.out.smt2
   <solutions>/Exercise4.out.py

.. _Solution to Exercise 5:

Solution to :ref:`Exercise 5 <Exercise 5>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. api-examples::
   <solutions>/Exercise5.smt2
   <solutions>/Exercise5.py

The output is as follows.

.. api-examples::
   <solutions>/Exercise5.out.smt2
   <solutions>/Exercise5.out.py

.. TODO

.. _Solution to Exercise 6:

Solution to :ref:`Exercise 6 <Exercise 6>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. TODO

.. _Solution to Exercise 7:

Solution to :ref:`Exercise 7 <Exercise 7>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. TODO

.. _Solution to Exercise 8:

Solution to :ref:`Exercise 8 <Exercise 8>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. TODO

.. _Solution to Exercise 9:

Solution to :ref:`Exercise 9 <Exercise 9>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. TODO

.. _Solution to Exercise 10:

Solution to :ref:`Exercise 10 <Exercise 10>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. TODO

.. _Solution to Exercise 11:

Solution to :ref:`Exercise 11 <Exercise 11>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. TODO

.. _Solution to Exercise 12:

Solution to :ref:`Exercise 12 <Exercise 12>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. TODO

.. _Solution to Exercise 13:

Solution to :ref:`Exercise 13 <Exercise 13>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. TODO


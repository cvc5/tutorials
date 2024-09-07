.. include:: macros.rst

.. _introduction:

Introduction
============
Great minds have long dreamed of creating machines that can reason deductively,
that is, from a set of assumptions, determine whether a particular conclusion
logically follows. The question of whether such a machine is possible
was posed formally as a grand challenge by the famous mathematician David
Hilbert in 1928, who called it the “Entscheidungsproblem” (decision problem)
[R24]_. In 1936, both Church and Turing showed that, in general, this is
impossible—the problem is undecidable [R13]_, [R42]_. Undeterred, researchers in
automated reasoning have searched for ways to solve either special cases of the
problem that are decidable or to find heuristics that work well in
practice. Satisfiability modulo theories (SMT) has emerged as an approach that
seems to fill a sweet spot in this search space. SMT leverages a rich
collection of decidable theories to provide considerable expressive power
without sacrificing decidability. SMT also permits some queries over problems
that are undecidable or whose decidability is unknown. For these, it employs
powerful heuristics that often work well in practice.

This tutorial is an introduction to SMT for new users. We explain what kinds of
problems are suitable for SMT solvers, describe the capabilities of modern
solvers, and provide guidance on how to encode problems as SMT queries.

Throughout the tutorial, we provide examples and exercises to illustrate the
concepts being explained. Unless otherwise stated, the exercises can be completed using either the |cvcv| [R3]_ or the |ziii| SMT solver [R32]_, through either
their Python interface or their textual interface based on the SMT-LIB 2 format
[R8]_. The |cvcv| website at `cvc5.github.io <http://cvc5.github.io>`_ contains
documentation that can be used as a reference to supplement the material in
this tutorial. An online version of the tutorial is also available on that site
by clicking on Tutorials. To work through the examples and exercises, we
recommend one of the following options.

A. To use a Python API for SMT, first create a virtual environment.

   .. code-block:: bash

      python3 -m venv smt-tutorial
      source smt-tutorial/bin/activate

   Next, install |cvcv|'s Python API or |ziii|'s Python API, or both.

   .. code-block:: bash

      python3 -m pip install cvc5
      python3 -m pip install z3-solver

   |cvcv| is distributed under the BSD 3-clause license. Some features, however,
   such as its finite field solver (see :ref:`finite-fields`), are only available in an
   extended version of |cvcv| distributed under the GNU General Public License
   (GPL).\
   [#]_
   Since GPL is a problem for some users, the GPL version is not built
   or distributed by default. To install the GPL version of |cvcv|, use:

   .. code-block:: bash

      python3 -m pip install cvc5-gpl

   Once a solver API is installed, you can copy example Python code into a
   script file, e.g., Example.py`, and then type:

   .. code-block:: bash

      python3 Example.py

   Note that, for the examples below, if you are using |ziii| instead of |cvcv|, you
   must replace the first line of each Python code snippet with:

   .. code-block:: python

      from z3 import *

B. Executables for |cvcv| and |ziii| are available for download. For |cvcv|, go to the
   |cvcv| website, click on `Downloads <https://cvc5.github.io/downloads.html>`_,
   and follow the link to the release page
   on GitHub. Alternatively, for |ziii|, go to the |ziii| releases page at
   `github.com/z3Prover/z3/releases
   <http://github.com/z3Prover/z3/releases>`_. From either release page,
   download the
   latest release compatible with your machine (for |cvcv|, choose a GPL download
   if you want support for finite fields). Once you unzip the downloaded
   archive, the executable will be in the bin directory. Thus, if the unzipped
   directory is called release-dir, and you have downloaded |cvcv|, you can run
   an SMT-LIB example called Example.smt2 by typing:

   .. code-block:: bash

      release-dir/bin/cvc5 Example.smt2

   from your shell’s command line. If you downloaded |ziii|, type instead:

   .. code-block:: bash

      release-dir/bin/z3 Example.smt2

C. From the |cvcv| website, click on `Try cvc5 online
   <https://cvc5.github.io/app/>`_. This links to a page that
   provides a web interface for running |cvcv| on scripts in the SMT-LIB format. 

               
This tutorial has been tested with |cvcv| 1.2.0, |ziii| 4.13.0, and Python 3.12.3,
but later releases should work as well. Solver outputs shown below are based on
|cvcv| version 1.2.0. Other versions or solvers should produce conceptually
similar results, but the outputs may not be exactly the same. The SMT-LIB
examples are based on version 2.6 of the format [R5]_. |cvcv|’s Python API was
designed to be a drop-in replacement for |ziii|’s Python API. The credit for the
design of the Python API thus goes to the |ziii| authors.

.. [#] The finite field solver uses the CoCoA library [R1]_, which has a GPL license.

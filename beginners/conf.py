# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys
import pathlib

# add path to enable extensions
basedir=pathlib.Path()
sys.path.insert(0, str(basedir.joinpath('ext').resolve()))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Satisfiability Modulo Theories: A Beginner's Tutorial"
copyright = '2024, Clark Barrett, Cesare Tinelli, Haniel Barbosa, Aina Niemetz, Mathias Preiner, Andrew Reynolds, Yoni Zohar'
author = 'Clark Barrett, Cesare Tinelli, Haniel Barbosa, Aina Niemetz, Mathias Preiner, Andrew Reynolds, Yoni Zohar'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx_tabs.tabs','examples','sphinx_copybutton','sphinxcontrib.googleanalytics']
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'navigation_depth': 5
}
html_static_path = [str(basedir.joinpath('_static').resolve())]
html_css_files = ['custom.css']
html_show_sourcelink = False

html_extra_path = []


# -- SMT-LIB syntax highlighting ---------------------------------------------

from smtliblexer import SmtLibLexer
from sphinx.highlighting import lexers
lexers['smtlib'] = SmtLibLexer()


# -- custom extension:: examples ---------------------------------------------

# Configuration for tabs: title, language and group for detecting missing files
examples_types = {
        '^<examples>.*\.py$': {
                'title': 'Python',
                'lang': 'python',
                'group': 'py'
        },
        '^<solutions>.*\.py$': {
                'title': 'Python',
                'lang': 'python',
                'group': 'py'
        },
        '\.smt2$': {
                'title': 'SMT-LIBv2',
                'lang': 'smtlib',
                'group': 'smt2'
        },
}
# Special file patterns
examples_file_patterns = {
        '^<examples>(.*)': {
                'local': '/examples{}',
                'url': 'https://github.com/cvc5/tutorials/tree/main/beginners/examples{}',
                'urlname': 'examples{}',
        },
        '^<solutions>(.*)': {
                'local': '/solutions{}',
                'url': 'https://github.com/cvc5/tutorials/tree/main/beginners/solutions{}',
                'urlname': 'solutions{}',
        },
}

# -- Google Analytics --------------------------------------------------------

googleanalytics_id = 'G-ML12X2V35B'
googleanalytics_enabled = True

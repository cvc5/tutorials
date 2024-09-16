# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	@echo ""
	@echo "Use 'make github' to make HTML files for GitHub pages"

.PHONY: help github Makefile

github:
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	@find _build/html -name "*.html" -exec sed -i 's/_static/static/g; s/_images/images/g' {} +
	@if [ -d "_build/html/_static" ]; then \
		rm -rf _build/html/static; \
		mv _build/html/_static _build/html/static; \
	fi
	@if [ -d "_build/html/_images" ]; then \
		rm -rf _build/html/images; \
		mv _build/html/_images _build/html/images; \
	fi

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

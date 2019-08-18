# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = build

SPHINXAPI = sphinx-apidoc
APIOUTDIR = modules
APISOURCEDIR = ../Grid

GHPAGESDIR= gh-pages

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile api html

api: 
	@$(SPHINXAPI) -f -o "$(APIOUTDIR)" "$(APISOURCEDIR)"

# target specifically for html so we can clone into gh-pages
html: api
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(GHPAGESDIR)" $(SPHINXOPTS) $(O)
# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile api
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

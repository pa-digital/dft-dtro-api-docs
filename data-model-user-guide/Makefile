# Minimal makefile for Sphinx documentation using sphinx-multiversion

SPHINXBUILD   = sphinx-multiversion
SOURCEDIR     = source
BUILDDIR      = build

.PHONY: help html clean livehtml

help:
    @echo "make html     - build multi-version docs"
    @echo "make clean    - remove build output"
    @echo "make livehtml - live rebuild (single-version only)"

html:
    $(SPHINXBUILD) "$(SOURCEDIR)" "$(BUILDDIR)"

clean:
    rm -rf "$(BUILDDIR)"

# livehtml uses sphinx-autobuild which only supports single-version
livehtml:
    sphinx-autobuild -E -a "$(SOURCEDIR)" "$(BUILDDIR)/html" \
        --host 0.0.0.0 --port 8002 --ignore "build/*"

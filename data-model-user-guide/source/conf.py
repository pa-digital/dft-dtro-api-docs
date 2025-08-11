# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Digital Traffic Regulation Orders"
subproject = "Data Model Documentation"
copyright = "2025, Department for Transport"
author = "Department for Transport"
release = "3.4.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "dft"
html_static_path = ["_static"]

html_sidebars = {
    "**": [
        "globaltoc.html",
        "localtoc.html",
        "relations.html",
    ]
}

html_context = {
    "subproject": subproject,
}

numfig = True
numfig_format = {
    "figure": "Figure %s",
    "code-block": "Listing %s",
}

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os

project = "Digital Traffic Regulation Orders"
subproject = "Technical API Documentation"
copyright = "2025, Department for Transport"
author = "Department for Transport"
release = "1.4.2"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx_tabs.tabs"]

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "dft"
html_static_path = ["_static"]

pygments_style = "sphinx"

from dft_theme.utils.copy_shared_pages import copy_shared_pages

copy_shared_pages()

pr_number = os.environ.get("PR_NUMBER")
if pr_number:
    html_baseurl = f"docs/pr-{pr_number}"
else:
    html_baseurl = "https://d-tro.dft.gov.uk"

html_context = {
    "subproject": subproject,
    "base_path": f"/dft-dtro-api-docs-staging/pr-{pr_number}/" if pr_number else "",
}

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os

project = "Digital Traffic Regulation Orders"
copyright = "2025, Department for Transport"
author = "Department for Transport"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "dft"
html_static_path = ["_static"]

pr_number = os.environ.get("PR_NUMBER")
if pr_number:
    html_baseurl = f"docs/pr-{pr_number}"
else:
    html_baseurl = "https://d-tro.dft.gov.uk"

html_context = {
    "is_landing_page": True,
    "base_path": (
        f"/dft-dtro-api-docs-staging/pr-{pr_number}/" if pr_number else html_baseurl
    ),
}

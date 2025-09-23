# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os

project = "Digital Traffic Regulation Orders"
subproject = "User Portal Documentation"
copyright = "2025, Department for Transport"
author = "Department for Transport"
release = "0.1.0"


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "dft"
html_static_path = ["_static"]
html_search_enabled = True

import os
import re


def get_title_from_rst(filepath):
    with open(filepath, encoding="utf-8") as f:
        lines = f.readlines()

    for i in range(1, len(lines)):
        if re.match(r"^[=-`^\"\-+]{3,}\s*$", lines[i]) and lines[i - 1].strip():
            return lines[i - 1].strip()

    return None


def build_page_title_map(src_dir):
    title_map = {}
    for root, _, files in os.walk(src_dir):
        for file in files:
            if file.endswith(".rst"):
                rst_path = os.path.join(root, file)
                rel_path = os.path.relpath(rst_path, src_dir)
                html_name = os.path.splitext(rel_path)[0]
                title = get_title_from_rst(rst_path)
                if title:
                    title_map[html_name.replace(os.sep, "/")] = title

    return title_map


pr_number = os.environ.get("PR_NUMBER")
if pr_number:
    html_baseurl = f"docs/pr-{pr_number}"
else:
    html_baseurl = "https://d-tro.dft.gov.uk"

html_context = {
    "subproject": subproject,
    "breadcrumb_titles": build_page_title_map(os.path.abspath(".")),
    "base_path": (
        f"/dft-dtro-api-docs-staging/pr-{pr_number}/"
        if pr_number
        else html_baseurl + "/"
    ),
}

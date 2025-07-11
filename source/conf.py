# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

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


html_context = {
    "subproject": subproject,
    "breadcrumb_titles": build_page_title_map(os.path.abspath(".")),
}

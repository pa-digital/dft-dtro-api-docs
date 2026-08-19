import os
import sys
sys.path.insert(0, os.path.abspath("."))
sys.path.insert(0, os.path.abspath('./_extensions'))

project = 'api-documentation'
copyright = '2026, Department for Transport'
author = 'Department for Transport'

extensions = [
    "sphinx_tabs.tabs",
    "_extensions.govuk_classes",
    "_extensions.govuk_table_translator",
    "inset_text",
    "warning_text"
]

templates_path = ['_templates']
exclude_patterns = []

html_static_path = ['_static']


html_css_files = [
    'css/govuk-frontend-6.3.0.min.css',
    'css/custom.css'
]

html_theme = 'basic'

html_sidebars = {
    '**': []
}

html_show_sphinx = False
html_show_copyright = False
numfig = True
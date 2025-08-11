from docutils import nodes
from docutils.parsers.rst import Directive, directives

class ButtonDirective(Directive):
    has_content = False
    required_arguments = 0
    optional_arguments = 0
    option_spec = {
        'text': directives.unchanged_required,
        'url': directives.unchanged_required,
        'download': directives.flag,
    }


    def run(self):
        text = self.options.get('text')
        url = self.options.get('url')

        download_attr = ' download' if 'download' in self.options else ''
        html = f"""
        <a class="button-container primary" href="{url}" target="_blank"{download_attr} style="text-decoration: none">
            <button>{text}</button>
            <svg class="govuk-button__start-icon govuk-!-display-none-print" xmlns="http://www.w3.org/2000/svg" width="17.5" height="19" viewBox="0 0 33 40" focusable="false" aria-hidden="true">
                <path fill="currentColor" d="M0 0h13l20 20-20 20H0l20-20z"></path>
            </svg>
        </a>
        """

        return [nodes.raw('', html, format='html')]

def setup(app):
    app.add_directive("button", ButtonDirective)


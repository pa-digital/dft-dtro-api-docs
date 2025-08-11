from docutils import nodes
from docutils.parsers.rst import Directive, directives

class ButtonNavDirective(Directive):
    has_content = False
    required_arguments = 0
    optional_arguments = 0
    option_spec = {
        'next-text': directives.unchanged_required,
        'next-url': directives.unchanged_required,
        'back-text': directives.unchanged,
        'back-url': directives.unchanged,
    }


    def run(self):
        next_text = self.options.get('next-text', 'Next')
        next_url = self.options.get('next-url')
        back_text = self.options.get('back-text', 'Back')
        back_url = self.options.get('back-url')

        back_button_html = ""
        if back_url:
            back_button_html = f"""
                <a class="button-container secondary" href="{back_url}" style="text-decoration: none">
                    <button>{back_text}</button>
                </a>
            """
            
        next_button_html = ""
        if next_url:
            next_button_html = f"""
                <a class="button-container primary" href="{next_url}" style="text-decoration: none">
                    <button>{next_text}</button>
                    <svg class="govuk-button__start-icon govuk-!-display-none-print" xmlns="http://www.w3.org/2000/svg" width="17.5" height="19" viewBox="0 0 33 40" focusable="false" aria-hidden="true">
                        <path fill="currentColor" d="M0 0h13l20 20-20 20H0l20-20z"></path>
                    </svg>
                </a>
            """

        html = f"""
        <div class="button-nav-container">
            {back_button_html}
           {next_button_html}
        </div>
        """

        return [nodes.raw('', html, format='html')]

def setup(app):
    app.add_directive("button-nav", ButtonNavDirective)


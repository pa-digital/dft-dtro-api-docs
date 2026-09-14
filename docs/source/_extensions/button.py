from docutils import nodes
from docutils.parsers.rst import Directive, directives


class ButtonDirective(Directive):
    has_content = False

    option_spec = {
        "text": directives.unchanged_required,
        "url": directives.unchanged_required,
        "download": directives.flag,
    }

    def run(self):
        text = self.options["text"]
        url = self.options["url"]

        download_attr = " download" if "download" in self.options else ""

        html = f"""
            <a href="{url}"
            class="govuk-button"
            data-module="govuk-button"
            target="_blank"
            {download_attr}>
                {text}
            </a>
        """

        return [nodes.raw("", html, format="html")]


def setup(app):
    app.add_directive("button", ButtonDirective)
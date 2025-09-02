from docutils import nodes
from docutils.parsers.rst import Directive, directives


class TagDirective(Directive):
    has_content = True
    required_arguments = 0
    optional_arguments = 0
    option_spec = {
        "text": directives.unchanged_required,
    }

    def run(self):
        self.assert_has_content()
        text = self.options.get("text")

        container = nodes.container(classes=["govuk-tag"])

        paragraph = nodes.paragraph()
        paragraph += nodes.Text(text)
        container += paragraph

        return [container]


def setup(app):
    app.add_directive("tag", TagDirective)

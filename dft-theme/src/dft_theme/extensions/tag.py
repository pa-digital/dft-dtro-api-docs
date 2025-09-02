from docutils import nodes
from docutils.parsers.rst import Directive


class TagDirective(Directive):
    has_content = True
    required_arguments = 0
    optional_arguments = 0

    def run(self):
        self.assert_has_content()
        text = "\n".join(self.content)

        container = nodes.container(classes=["govuk-tag"])
        paragraph = nodes.paragraph()
        paragraph += nodes.Text(text)
        container += paragraph

        return [container]


def setup(app):
    app.add_directive("tag", TagDirective)

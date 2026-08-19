from docutils import nodes
from docutils.parsers.rst import Directive

class InsetTextDirective(Directive):
    has_content = True

    def run(self):
        self.assert_has_content()

        container = nodes.container(classes=["govuk-inset-text"])

        self.state.nested_parse(self.content, self.content_offset, container)

        return [container]


def setup(app):
    app.add_directive("inset", InsetTextDirective)
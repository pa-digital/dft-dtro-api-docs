from docutils import nodes
from docutils.parsers.rst import Directive, directives


class NotificationDirective(Directive):
    has_content = True
    required_arguments = 0
    optional_arguments = 0
    option_spec = {
        "heading": directives.unchanged_required,
    }

    def run(self):
        self.assert_has_content()
        heading = self.options.get("heading")

        container = nodes.container(classes=["notification-container"])

        heading_node = nodes.paragraph(text=heading)
        container += heading_node
        content_node = nodes.container(classes=["notification-content"])
        self.state.nested_parse(self.content, self.content_offset, content_node)
        container += content_node

        return [container]


def setup(app):
    app.add_directive("notification", NotificationDirective)

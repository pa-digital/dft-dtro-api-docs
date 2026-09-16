from html import escape

from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst.directives import unchanged


class DtroTabsNode(nodes.General, nodes.Element):
    pass


class DtroTabNode(nodes.General, nodes.Element):
    pass


class DtroTabsDirective(Directive):
    """
    Container for one or more dtro-tab directives.

    Usage:

    .. dtro-tabs::

        .. dtro-tab:: curl

            .. code-block:: bash

                curl ...

        .. dtro-tab:: Response

            .. code-block:: json

                {}
    """

    has_content = True

    def run(self):
        self.assert_has_content()

        serial = self.env.new_serialno("dtro-tabset")
        tabset_id = f"dtro-tabset-{serial}"

        node = DtroTabsNode()
        node["tabset_id"] = tabset_id

        self.state.nested_parse(
            self.content,
            self.content_offset,
            node,
        )

        tab_number = 0

        for child in node.children:
            if not isinstance(child, DtroTabNode):
                continue

            child["tabset_id"] = tabset_id
            child["tab_number"] = tab_number
            child["tab_id"] = f"{tabset_id}-tab-{tab_number}"
            child["panel_id"] = f"{tabset_id}-panel-{tab_number}"
            child["selected"] = tab_number == 0

            tab_number += 1

        if tab_number == 0:
            return [
                self.state_machine.reporter.error(
                    "The dtro-tabs directive requires at least one "
                    "dtro-tab directive.",
                    line=self.lineno,
                )
            ]

        return [node]


class DtroTabDirective(Directive):
    """
    One tab within a dtro-tabs container.

    The directive argument is used as the visible tab label.
    Its body accepts normal reStructuredText content.
    """

    required_arguments = 1
    final_argument_whitespace = True
    has_content = True

    option_spec = {
        "name": unchanged,
    }

    def run(self):
        self.assert_has_content()

        node = DtroTabNode()
        node["title"] = self.arguments[0].strip()

        self.state.nested_parse(
            self.content,
            self.content_offset,
            node,
        )

        return [node]


def visit_dtro_tabs_html(self, node):
    tabset_id = escape(node["tabset_id"], quote=True)

    self.body.append(
        f'<div class="dtro-tabset" id="{tabset_id}">'
    )

    self.body.append(
        '<div class="dtro-tab-list" role="tablist">'
    )

    for child in node.children:
        if not isinstance(child, DtroTabNode):
            continue

        title = escape(child["title"])
        tab_id = escape(child["tab_id"], quote=True)
        panel_id = escape(child["panel_id"], quote=True)
        selected = child["selected"]

        selected_value = "true" if selected else "false"
        tab_index = "0" if selected else "-1"
        active_class = " dtro-tab--active" if selected else ""

        self.body.append(
            f'<button type="button"'
            f' class="dtro-tab{active_class}"'
            f' id="{tab_id}"'
            f' role="tab"'
            f' aria-selected="{selected_value}"'
            f' aria-controls="{panel_id}"'
            f' tabindex="{tab_index}">'
            f'{title}'
            f'</button>'
        )

    self.body.append("</div>")


def depart_dtro_tabs_html(self, node):
    self.body.append("</div>")


def visit_dtro_tab_html(self, node):
    tab_id = escape(node["tab_id"], quote=True)
    panel_id = escape(node["panel_id"], quote=True)
    selected = node["selected"]

    active_class = " dtro-tab-panel--active" if selected else ""

    self.body.append(
        f'<div'
        f' class="dtro-tab-panel{active_class}"'
        f' id="{panel_id}"'
        f' role="tabpanel"'
        f' aria-labelledby="{tab_id}"'
        f' tabindex="0">'
    )


def depart_dtro_tab_html(self, node):
    self.body.append("</div>")


def setup(app):
    app.add_node(
        DtroTabsNode,
        html=(
            visit_dtro_tabs_html,
            depart_dtro_tabs_html,
        ),
    )

    app.add_node(
        DtroTabNode,
        html=(
            visit_dtro_tab_html,
            depart_dtro_tab_html,
        ),
    )

    app.add_directive("dtro-tabs", DtroTabsDirective)
    app.add_directive("dtro-tab", DtroTabDirective)

    app.add_css_file("dtro-tabs.css")
    app.add_js_file("dtro-tabs.js")

    return {
        "version": "1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
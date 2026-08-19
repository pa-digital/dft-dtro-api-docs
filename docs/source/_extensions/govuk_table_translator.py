from docutils import nodes
from sphinx.writers.html5 import HTML5Translator


def replace_classes(node, remove=(), add=()):
    """
    Remove unwanted CSS classes and add the required classes.

    Existing Sphinx classes that are not explicitly removed are retained.
    This preserves useful classes such as row-odd, row-even and head.
    """
    classes = node.setdefault("classes", [])

    for css_class in remove:
        while css_class in classes:
            classes.remove(css_class)

    for css_class in add:
        if css_class not in classes:
            classes.append(css_class)


def is_header_entry(node):
    """
    Return True if an entry belongs to a table header.

    The normal Docutils hierarchy is:

        entry -> row -> thead
    """
    parent = node.parent

    while parent is not None:
        if isinstance(parent, nodes.thead):
            return True

        if isinstance(parent, nodes.tbody):
            return False

        if isinstance(parent, nodes.table):
            return False

        parent = parent.parent

    return False


class GovUkTableTranslator(HTML5Translator):
    """
    Sphinx HTML5 translator that emits GOV.UK table classes.

    All non-table rendering is inherited unchanged from Sphinx's
    HTML5Translator.
    """

    def visit_table(self, node):
        replace_classes(
            node,
            add=("govuk-table",),
        )

        super().visit_table(node)

    def visit_thead(self, node):
        replace_classes(
            node,
            add=("govuk-table__head",),
        )

        super().visit_thead(node)

    def visit_tbody(self, node):
        replace_classes(
            node,
            add=("govuk-table__body",),
        )

        super().visit_tbody(node)

    def visit_row(self, node):
        replace_classes(
            node,
            add=("govuk-table__row",),
        )

        super().visit_row(node)

    def visit_entry(self, node):
        if is_header_entry(node):
            replace_classes(
                node,
                remove=("govuk-table__cell",),
                add=("govuk-table__header",),
            )
        else:
            replace_classes(
                node,
                remove=("govuk-table__header",),
                add=("govuk-table__cell",),
            )

        super().visit_entry(node)

    def visit_title(self, node):
        """
        Render a table title as a GOV.UK table caption.

        Other titles, including document titles, section headings,
        admonition titles and figure captions, use Sphinx's normal
        rendering.
        """
        if not isinstance(node.parent, nodes.table):
            super().visit_title(node)
            return

        replace_classes(
            node,
            remove=("govuk-table",),
            add=(
                "govuk-table__caption",
                "govuk-table__caption--m",
            ),
        )

        self.body.append(
            self.starttag(
                node,
                "caption",
                "",
            )
        )

        self.body.append('<span class="caption-text">')
        self.context.append("</span></caption>\n")


def setup(app):
    app.set_translator(
        "html",
        GovUkTableTranslator,
        override=True,
    )

    return {
        "version": "0.3",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
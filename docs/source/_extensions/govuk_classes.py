from docutils import nodes


def add_class(node, *classes):
    """Add CSS classes without creating duplicates."""
    existing = set(node.get("classes", []))

    for css_class in classes:
        if css_class not in existing:
            node["classes"].append(css_class)
            existing.add(css_class)


def has_ancestor(node, ancestor_type):
    """Return True if the node has an ancestor of the specified type."""
    parent = node.parent

    while parent is not None:
        if isinstance(parent, ancestor_type):
            return True

        parent = parent.parent

    return False


def add_govuk_classes(app, doctree, docname):
    for node in doctree.findall(nodes.paragraph):
        if not has_ancestor(node, nodes.table):
            add_class(node, "govuk-body")

    # Section headings
    for node in doctree.findall(nodes.title):
        parent = node.parent

        if isinstance(parent, nodes.section):
            level = get_section_level(parent)

            if level == 1:
                add_class(node, "govuk-heading-xl")
            elif level == 2:
                add_class(node, "govuk-heading-l")
            elif level == 3:
                add_class(node, "govuk-heading-m")
            else:
                add_class(node, "govuk-heading-s")

    # Bullet lists
    for node in doctree.findall(nodes.bullet_list):
        add_class(
            node,
            "govuk-list",
            "govuk-list--bullet",
        )

    # Numbered lists
    for node in doctree.findall(nodes.enumerated_list):
        add_class(
            node,
            "govuk-list",
            "govuk-list--number",
        )

    # List items
    for node in doctree.findall(nodes.list_item):
        add_class(node, "govuk-list__item")


def get_section_level(section):
    """Return the nesting level of a section."""
    level = 1
    parent = section.parent

    while isinstance(parent, nodes.section):
        level += 1
        parent = parent.parent

    return level


def setup(app):
    app.connect(
        "doctree-resolved",
        add_govuk_classes,
    )

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
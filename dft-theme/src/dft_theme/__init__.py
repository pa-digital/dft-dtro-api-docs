import json
import os
from pathlib import Path
from sphinx.environment.adapters.toctree import TocTree
from docutils import nodes


def extract_subheadings(doctree):
    """Extract second-level headings from a page's doctree."""
    if not doctree:
        return []

    subheadings = []
    for section in doctree.traverse(nodes.section):
        title_node = section.next_node(nodes.title)
        if not title_node:
            continue

        anchor = section.get("ids", [None])[0]
        if not anchor:
            continue

        subheadings.append({"title": title_node.astext(), "href": f"#{anchor}"})

    return subheadings


def inject_custom_toc(app, pagename, templatename, context, doctree):
    env = app.builder.env
    toctree = TocTree(env)

    toc_root = toctree.get_toctree_for(
        app.config.master_doc, app.builder, collapse=False, maxdepth=1
    )
    if toc_root is None:
        context["toctree_data"] = []
        return

    toc_items = []
    for item in toc_root.traverse(condition=lambda n: n.tagname == "reference"):
        page_href = item.get("refuri")
        title = item.astext()
        docname = page_href.replace(".html", "")

        meta = env.metadata.get(docname, {})
        description = meta.get("description", "")

        try:
            page_doctree = env.get_doctree(docname)
        except Exception:
            page_doctree = None

        subitems = extract_subheadings(page_doctree)

        toc_items.append(
            {
                "title": title,
                "description": description,
                "href": page_href,
                "children": subitems,
            }
        )

    context["toctree_data"] = toc_items


def add_links(app, pagename, templatename, context, doctree):
    with open(
        os.path.join(os.path.dirname(__file__), "links.json"), "r", encoding="utf-8"
    ) as f:
        context["links"] = json.load(f)


def setup(app):
    from .extensions import button, button_nav, notification, toc, tag

    theme_path = Path(__file__).parent.resolve()
    app.add_html_theme("dft", str(theme_path))

    button.setup(app)
    button_nav.setup(app)
    notification.setup(app)
    toc.setup(app)
    tag.setup(app)

    app.connect("html-page-context", inject_custom_toc)
    app.connect("html-page-context", add_links)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }

from sphinx.environment.adapters.toctree import TocTree

def build_custom_toc(app, pagename, templatename, context, doctree):
    env = app.builder.env
    toctree = TocTree(env)

    master = app.config.master_doc
    toc_tree = toctree.get_toctree_for(master, app.builder, collapse=False, maxdepth=2)

    def walk_toc(node):
        items = []
        if node is None:
            return items

        for item in node.traverse(condition=lambda n: n.tagname == 'list_item'):
            ref = item.next_node(descend=True, condition=lambda n: n.tagname == 'reference')
            if ref is None:
                continue

            title = ref.astext()
            href = ref.get('refuri', '#')

            docname = href.split('#')[0].replace('.html', '')

            description = env.metadata.get(docname, {}).get('description', '')

            sublist = item.next_node(descend=True, condition=lambda n: n.tagname == 'bullet_list')
            children = walk_toc(sublist) if sublist else []

            items.append({
                'title': title,
                'href': href,
                'description': description,
                'children': children
            })

        return items


    toc_items = walk_toc(toc_tree)

    context['toctree_data'] = toc_items

def setup(app):
    app.connect("html-page-context", build_custom_toc)
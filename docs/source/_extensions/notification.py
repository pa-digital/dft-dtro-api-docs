from docutils import nodes
from docutils.parsers.rst import Directive, directives


class notification_banner(nodes.General, nodes.Element):
    pass


class NotificationDirective(Directive):
    has_content = True

    option_spec = {
        "heading": directives.unchanged_required,
    }

    def run(self):
        self.assert_has_content()

        banner = notification_banner()
        banner["heading"] = self.options["heading"]

        content = nodes.container()

        self.state.nested_parse(
            self.content,
            self.content_offset,
            content,
        )

        banner += content

        return [banner]


def visit_notification_html(self, node):
    heading = node.get("heading", "Important")

    self.body.append(
        f"""
<div class="govuk-notification-banner"
     role="region"
     aria-labelledby="govuk-notification-banner-title"
     data-module="govuk-notification-banner">

  <div class="govuk-notification-banner__header">
    <h2 class="govuk-notification-banner__title"
        id="govuk-notification-banner-title">
      {heading}
    </h2>
  </div>

  <div class="govuk-notification-banner__content">
"""
    )


def depart_notification_html(self, node):
    self.body.append(
        """
  </div>
</div>
"""
    )


def setup(app):
    app.add_node(
        notification_banner,
        html=(visit_notification_html, depart_notification_html),
    )

    app.add_directive(
        "notification",
        NotificationDirective,
    )

    return {
        "version": "1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
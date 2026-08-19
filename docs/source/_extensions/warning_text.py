from docutils import nodes
from docutils.parsers.rst import Directive


class WarningText(Directive):
    has_content = True

    def run(self):
        text = "\n".join(self.content)

        html = f"""
<div class="govuk-warning-text">
  <span class="govuk-warning-text__icon" aria-hidden="true">!</span>
  <strong class="govuk-warning-text__text">
    <span class="govuk-visually-hidden">Warning</span>
    {text}
  </strong>
</div>
"""

        return [nodes.raw('', html, format='html')]


def setup(app):
    app.add_directive("warning_text", WarningText)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
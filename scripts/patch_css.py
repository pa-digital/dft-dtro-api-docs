#!/usr/bin/env python3

from pathlib import Path
import re
import tinycss2

INPUT_FILE = Path(
    "docs/source/_static/css/govuk-frontend-6.3.0.min.css"
)

OUTPUT_FILE = Path(
    "docs/source/_static/css/govuk-scoped.css"
)

PREFIX = ".dtro-doc"

REMOVE_PREFIXES = (
    ".govuk-header",
    ".govuk-footer",
    ".govuk-template",
    ".govuk-template__body",
    ".govuk-service-navigation",
    ".govuk-cookie-banner",
    ".govuk-phase-banner",
)

# GOV.UK assumes a 16px root font size.
# ServiceNow is using 10px.
ROOT_FONT_SIZE = 10
GOVUK_ROOT_SIZE = 16

SCALE_FACTOR = (
    GOVUK_ROOT_SIZE /
    ROOT_FONT_SIZE
)

REM_PATTERN = re.compile(
    r"(-?\d*\.?\d+)rem\b"
)


def should_remove(selector):
    selector = selector.strip()

    return any(
        selector.startswith(prefix)
        for prefix in REMOVE_PREFIXES
    )


def prefix_selector(selector):
    selector = selector.strip()

    if selector in (
        "html",
        "body",
        ":root",
    ):
        return PREFIX

    if selector.startswith(PREFIX):
        return selector

    return f"{PREFIX} {selector}"


def scale_rem_units(css_text):

    def repl(match):

        original = float(
            match.group(1)
        )

        scaled = (
            original *
            SCALE_FACTOR
        )

        text = (
            f"{scaled:.4f}"
            .rstrip("0")
            .rstrip(".")
        )

        return f"{text}rem"

    return REM_PATTERN.sub(
        repl,
        css_text
    )


def scope_rule(rule):

    selector_text = tinycss2.serialize(
        rule.prelude
    )

    selectors = [
        s.strip()
        for s in selector_text.split(",")
    ]

    selectors = [
        s
        for s in selectors
        if not should_remove(s)
    ]

    if not selectors:
        return None

    scoped = [
        prefix_selector(s)
        for s in selectors
    ]

    rule.prelude = tinycss2.parse_component_value_list(
        ", ".join(scoped)
    )

    return rule


def process_rules(rules):

    output = []

    for rule in rules:

        if rule.type == "qualified-rule":

            processed = scope_rule(rule)

            if processed:
                output.append(processed)

            continue

        if (
            rule.type == "at-rule"
            and rule.content is not None
        ):

            if rule.lower_at_keyword in (
                "media",
                "supports",
                "layer",
                "container",
                "document",
            ):

                nested = tinycss2.parse_rule_list(
                    rule.content
                )

                rule.content = process_rules(
                    nested
                )

        output.append(rule)

    return output


def main():

    css = INPUT_FILE.read_text(
        encoding="utf-8"
    )

    rules = tinycss2.parse_stylesheet(
        css,
        skip_comments=False,
        skip_whitespace=False,
    )

    processed = process_rules(rules)

    css_out = tinycss2.serialize(
        processed
    )

    css_out = scale_rem_units(
        css_out
    )

    OUTPUT_FILE.write_text(
        css_out,
        encoding="utf-8"
    )

    print(
        f"Created {OUTPUT_FILE}"
    )


if __name__ == "__main__":
    main()
from pathlib import Path

rst_files = sorted(
    f.stem
    for f in Path("content").glob("*.rst")
)

toc = "\n".join(f"   generated/{name}" for name in rst_files)

template = Path("docs/source/index.rst.template").read_text()

output = template.replace("{{ TOC }}", toc)

Path("docs/source/index.rst").write_text(output)

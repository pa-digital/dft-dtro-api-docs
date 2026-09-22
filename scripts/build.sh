#!/usr/bin/env bash

set -euo pipefail

echo "Cleaning build directories..."

rm -rf docs/source/generated
mkdir -p docs/source/generated

rm -rf docs/build/html
rm -rf docs/output

mkdir -p docs/source/generated/images
mkdir -p docs/source/generated/table_data

TOC=""

echo "Processing marker files..."

shopt -s nullglob
markers=(to-build/*)
shopt -u nullglob

if (( ${#markers[@]} == 0 )); then
    echo "No marker files found in to-build/"
    exit 0
fi

for marker in "${markers[@]}"; do
    [[ "$(basename "$marker")" == ".gitkeep" ]] && continue
    doc="$(basename "$marker")"
    source_file="content/${doc}.rst"

    if [[ ! -f "$source_file" ]]; then
        echo "No matching document found: $source_file"
        exit 1
    fi

    echo "Including: $doc"

    cp "$source_file" docs/source/generated/

    TOC="${TOC}
   generated/${doc}"
done

echo "Generating index.rst..."

cat > docs/source/index.rst <<EOF
D-TRO Documentation
===================

.. toctree::
   :maxdepth: 2
$TOC
EOF

echo "Copying images..."

if [[ -d content/images ]]; then
    cp -R content/images/. docs/source/generated/images/
fi

echo "Copying table data..."

if [[ -d content/table_data ]]; then
    cp -R content/table_data/. docs/source/generated/table_data/
fi

echo "Building Sphinx..."

sphinx-build \
    -b html \
    docs/source \
    docs/build/html

echo "Patching CSS ..."
python ./scripts/patch_css.py

echo "Inlining assets..."

./scripts/inline_assets.sh

echo
echo "Build complete."
echo "Generated HTML files:"

find docs/output -name '*.html' -printf '  %f\n'

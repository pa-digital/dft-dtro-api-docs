#!/usr/bin/env bash

rm -rf docs/source/_static/images
mkdir -p docs/source/_static/images

cp content/*.rst docs/source
cp -r content/images docs/source/_static/images/

python3 ./scripts/generate_index.py
sphinx-build -b html docs/source docs/build/html

mkdir -p build/output



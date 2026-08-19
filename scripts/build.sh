#!/usr/bin/env bash

rm -rf docs/source/generated/
mkdir -p docs/source/generated/images
rm -rf docs/output

cp content/*.rst docs/source/generated/
cp -r content/images docs/source/generated/images/

sphinx-build -b html docs/source docs/build/html

mkdir -p build/output
./scripts/inline_assets.sh

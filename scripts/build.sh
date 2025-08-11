#!/bin/bash

set -e

rm -rf docs

mkdir -p docs/api-documentation
mkdir -p docs/data-model-user-guide
mkdir -p docs/user-portal-documentation
mkdir -p docs/portal-access

docker exec -it $(docker ps --filter="name=api-documentation" -q) /bin/bash -c "redocly build-docs specs/openapi.yaml -o source/_static/redoc.html && make html"
docker exec -it $(docker ps --filter="name=data-model-user-guide" -q) /bin/bash -c "make html"
docker exec -it $(docker ps --filter="name=user-portal-documentation" -q) /bin/bash -c "make html"
docker exec -it $(docker ps --filter="name=landing" -q) /bin/bash -c "make html"

cp -r api-documentation/build/html/* docs/api-documentation
cp -r data-model-user-guide/build/html/* docs/data-model-user-guide
cp -r user-portal-documentation/build/html/* docs/user-portal-documentation
cp -r portal-access/build/html/* docs
cp index.html docs
cp CNAME docs
cp .nojekyll docs

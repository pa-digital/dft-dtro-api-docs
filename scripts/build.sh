#!/bin/bash

set -e

rm -rf docs

mkdir -p docs/api-documentation
mkdir -p docs/data-model-user-guide
mkdir -p docs/user-portal-documentation

docker exec -it $(docker ps --filter="name=api-documentation" -q) bash -c "redocly build-docs specs/openapi.yaml -o source/_static/redoc.html && make html"
docker exec -it $(docker ps --filter="name=data-model-user-guide" -q) bash -c "make html"
docker exec -it $(docker ps --filter="name=user-portal-documentation" -q) bash -c "make html"
docker exec -it $(docker ps --filter="name=landing" -q) bash -c "make html"

cp -r api-documentation/build/html/* docs/api-documentation
cp -r data-model-user-guide/build/html/* docs/data-model-user-guide
cp -r data-model-user-guide/source/Data\ Model\ HTML\ Guide docs/data-model-user-guide
cp -r user-portal-documentation/build/html/* docs/user-portal-documentation
cp -a portal-access/build/html/* docs
cp -a docs/api-documentation/shared/*.html docs
cp CNAME docs
cp .nojekyll docs
cp robots.txt docs

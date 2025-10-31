#!/bin/bash

set -e

docker exec -e PR_NUMBER=$PR_NUMBER $(docker ps --filter="name=api-documentation" -q) bash -c "redocly build-docs specs/openapi.yaml -o source/_static/redoc.html && make html"
docker exec -e PR_NUMBER=$PR_NUMBER $(docker ps --filter="name=data-model-user-guide" -q) bash -c "make html"
docker exec -e PR_NUMBER=$PR_NUMBER $(docker ps --filter="name=user-portal-documentation" -q) bash -c "make html"
docker exec -e PR_NUMBER=$PR_NUMBER $(docker ps --filter="name=landing" -q) bash -c "make html"

mkdir -p docs/api-documentation
mkdir -p docs/data-model-user-guide
mkdir -p docs/user-portal-documentation
mkdir -p docs/api-documentation

cp -r api-documentation/build/html/* docs/api-documentation
cp -r api-documentation/collections/dtro-integration.postman_collection.json docs/api-documentation/_static/dtro-integration.postman_collection.json
cp -r api-documentation/collections/dtro-production.postman_collection.json docs/api-documentation/_static/dtro-production.postman_collection.json
cp -r data-model-user-guide/build/html/* docs/data-model-user-guide
cp -r data-model-user-guide/source/Data\ Model\ HTML\ Guide docs/data-model-user-guide
cp -r user-portal-documentation/build/html/* docs/user-portal-documentation
cp -a portal-access/build/html/* docs
cp -a docs/api-documentation/shared/*.html docs
cp -r docs/api-documentation/_static/tabs.* docs/_static/

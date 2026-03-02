#!/bin/bash

set -e

BRANCH=$(git rev-parse --abbrev-ref HEAD)

# docker system prune -af
# docker compose up -d --build

# rm -rf api-documentation/build
# rm -rf data-model-user-guide/build
# rm -rf portal-access/build
# rm -rf user-portal-documentation/build
rm -rf docs

# docker exec -e PR_NUMBER=$PR_NUMBER $(docker ps --filter="name=api-documentation" -q) bash -c "redocly build-docs specs/openapi.yaml -o source/_static/redoc.html && make html"

# docker exec -e PR_NUMBER=$PR_NUMBER $(docker ps --filter="name=data-model-user-guide" -q) bash -c "cd /workspace/data-model-user-guide && make html"

# docker exec -e PR_NUMBER=$PR_NUMBER $(docker ps --filter="name=user-portal-documentation" -q) bash -c "make html"

# docker exec -e PR_NUMBER=$PR_NUMBER $(docker ps --filter="name=landing" -q) bash -c "make html"

mkdir -p docs/api-documentation
mkdir -p docs/data-model-user-guide
mkdir -p docs/user-portal-documentation
mkdir -p docs/api-documentation

cp -r api-documentation/build/html/* docs/api-documentation
cp -r api-documentation/collections/dtro-integration.postman_collection.json docs/api-documentation/_static/dtro-integration.postman_collection.json
cp -r api-documentation/collections/dtro-production.postman_collection.json docs/api-documentation/_static/dtro-production.postman_collection.json
cp -r data-model-user-guide/build/* docs/data-model-user-guide
cp -r user-portal-documentation/build/html/* docs/user-portal-documentation
cp -a portal-access/build/html/* docs
cp -a docs/api-documentation/shared/*.html docs
cp -r docs/api-documentation/_static/tabs.* docs/_static/

# Copy HTML Data Model User Guides from respective branches
for d in docs/data-model-user-guide/release/*/; do
    dirname="${d%/}"
    dirname="${dirname##*/}"
    rm -rf "data-model-user-guide/source/Data Model HTML Guide"
    git checkout "release/$dirname" -- "data-model-user-guide/source/Data Model HTML Guide"
    mv "data-model-user-guide/source/Data Model HTML Guide" "docs/data-model-user-guide/release/$dirname/"
done

# Copy all shared pages from latest version to previous versions
base="docs/data-model-user-guide/release"

versions=()
for d in "$base"/*/; do
    versions+=("${d%/}")
done

names=()
for v in "${versions[@]}"; do
    names+=("${v##*/}")
done

IFS=$'\n' sorted=($(printf "%s\n" "${names[@]}" | sort -V))
latest="${sorted[-1]}"

echo "Latest version detected: $latest"

src="$base/$latest"

for version in "${names[@]}"; do
    if [[ "$version" == "$latest" ]]; then
        echo "Skipping $version (this *is* the latest)."
        continue
    fi

    dest="$base/$version"
    echo "Copying files into: $version"
    cp -r "$src/releases.html" "$dest/"
done



# docker compose down --volumes

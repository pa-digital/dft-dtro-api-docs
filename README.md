# D-TRO Service API Documentation

DfT have recently decided to bring all the D-TRO service documentation sources into Service Now, and migrate away from where they are currently hosted, on GitHub Pages. This repository contains the versioned public-facing documentation, as well as a pipeline for building the docs as static HTML for import into Service Now.

### Documentation Content

All documentation is held under `content/`. Documentation should be written as ReStructured Text. Images should be placed under `content/images/`.

Each ReStructured Text file is compiled and output as its own HTML file.

### Building

In order to build the docs, the following must happen:

1. A document must be added to the `content` directory
2. A blank marker file with the same name as the document must be added to the `to-build` directory
3. The files must be pushed to the remote repository

For example, if adding a new 'Getting Started' document:

1. Create a file named `getting_started.rst` in `content`. Fill it out with the desired content to standard ReStructured Text conventions
2. Add a blank file named `getting_started` in `to-build/`
3. Push the changes to the remote repository

Each push to the repository will check for changes to the following files and directories:

* `to-build/**`
* `content/**`
* `docs/**`
* `scripts/**`
* `requirements.txt`

If changes are detected, the pipeline will start a documentation build.

**Note: only docs that have a marker file in the `to-build/` directory actually get built.**

Once the pipeline runs, the static HTML output is uploaded as an artifact in GitHub, and can be downloaded.
# D-TRO Service API Documentation

This repository contains technical documentation for the D-TRO service. It consists of three sources of documentation:

* **Technical API documentation**, providing a quickstart guide on interfacing with the D-TRO API, as well as Swagger documentation on API usage
* The **Data Model User Guide**, which provides an in-depth look at the D-TRO data model
* The **User Portal Documentation**, which explains how to get started with creating an account and applications to interact with the D-TRO service

The documentation itself is served here: https://d-tro.dft.gov.uk/

This repository also contains the `dft-theme` Sphinx theme, and a landing page that directs users to the necessary documentation.

## Local Development

Developing locally can be achieved with Docker. The `docker-compose.yml` file allows you to run the documentation. The Dockerfile will create containers with `sphinx-autobuild` installed, along with the `dft-theme` and other required packages. `api_documentation` will expose port 8001, `data_model_user_guide` will expose port 8002 and `user_portal_documentation` will expose port 8003.

The containers are set to do nothing when run; this is by design, and allows ytou to exec into them and run whatever you need, e.g. `sphinx-autobuild` for live editing of the documentation, `make html` to build the documentation, etc.

If any changes are made to the underlying `dft-theme`, you will need to rebuild the Docker containers for these changes to take effect.

## Documentation Building

The helper script `scripts/build.sh` is provided to automate the build process. Note that the Docker containers need to be running for this script to work. This script does the following:

* deletes existing build files
* execs into each Docker container and runs `make html` to generate the build files (in the `api_documentation` project it will also run redoc to generate the interactive API documentation)
* copies the outputs to the `docs` folder

## Documentation Serving

The documentation is served through GitHub Pages, which serves the content of the `docs` folder. Currently this is served form the `main` branch, meaning source and build files exist together. At a future point the build files will be on a separate branch, and GitHub pages will serve the content of this branch, allowing the source and build files to be separated. Github Actions will then build the files from the `main` branch, and commit them to this other branch.